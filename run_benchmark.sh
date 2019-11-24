#!/bin/bash
set -ex

function launch_rust_server {
  cd rust-grpc
  cargo run --release -- --port 5001 --model=../data/rust_k_means_model.json
}

function launch_rust_on_python_server {
  cd python-grpc
  RUST=true poetry run python src/main.py
}

function launch_python_server {
  cd python-grpc
  poetry run python src/main.py
}

for server in "rust" "python" "rust_on_python"; do
  for concurrency in 2 4 8 16 32 64 128 256 512 1024 2048 4096; do
    # Launch the server in a separate process
    case "$server" in
      rust)
        launch_rust_server &
        SERVER_PID=$!
        ;;
      python)
        launch_python_server &
        SERVER_PID=$!
        ;;
      rust_on_python)
        launch_rust_on_python_server &
        SERVER_PID=$!
        ;;
    esac

    echo "Launched server with PID ${SERVER_PID}."

    # Sleep just to make sure the server is up and running before we start the benchmark
    sleep 10s

    echo "Start testing"

    ghz \
        --proto=protos/centroids.proto \
        --call=ml.ClusteringService.Predict \
        --insecure \
        --data-file=data/observations.json \
        --duration 30s \
        --concurrency $concurrency \
        --format json \
        localhost:5001 \
        | jq 'del(.options)' | jq 'del(.details)' > "grpc-benchmark-outputs/${server}_${concurrency}.json"
        # ^ Clean up the output, removing some huge fields from the JSON

    echo "Finished testing, killing the server with PID ${SERVER_PID}."
    pkill -P "${SERVER_PID}"
  done
done
