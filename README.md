# Clustering benchmarks

K-means is a clustering algorithm - we compare the reference implementation provided by 
`scikit-learn` with the Rust implementation provided by `linfa-clustering`, including its
Python wrapper, `linfa-k-means`.

In particular, we compare:
- training times;
- inference time, as measured when the model is exposed as a gRPC microservice.

This repository contains all the source code required to reproduce the benchmarks as well as
instructions to do so.

Results are reported in the context of each benchmark.

## Training benchmark

We compare how long it takes to train a K-means model for:
- `scikit-learn`, with `init="random"`, `algorithm="full"` (Lloyds' algorithm);
- `linfa-k-means` (Lloyds' algorithm, Python wrapper around the `linfa-clustering` Rust implementation).
  
We use the same hyperparameters for all models:
- maximum number of iterations, `100`;
- tolerance, `1e-4`;
- number of clusters, `3`.

The comparison is run from Python using `pytest`'s benchmarking functionality.

### Running the benchmark

```bash

```

### Results

The results.

## Inference benchmark 

We compare the inference performance of the K-Means model exposed as a gRPC microservice.
The following setups are compared:
- `scikit-learn` exposed with Python's [`grpcio`](https://grpc.io/docs/quickstart/python/);
- `linfa-k-means` exposed with Python's [`grpcio`](https://grpc.io/docs/quickstart/python/);
- `linfa-clustering` exposed with Rust's [`tonic`](https://github.com/hyperium/tonic).

The comparison is run using [`ghz`](https://ghz.sh/).

### Test data

The data used for the inference benchmark can be found in the `data` folder.

The utils under `rust-grpc/src/bin` can be used to generate additional/different test data. Check 
`rust-grpc/README.md` for more details.

### Launching the gRPC microservices

Launch Python's microservice on port `5001`, serving `scikit-learn`'s model:
```bash
cd python-grpc
# Install the required packages in a virtual environment
poetry install
poetry run python src/main.py
```

Launch Python's microservice on port `5001`, serving `linfa`'s model (Python wrapper over Rust):
```bash
cd python-grpc
# Install the required packages in a virtual environment
poetry install
RUST=true poetry run python src/main.py
```

Launch Rust's microservice on port `5001`, serving `linfa`'s model (Rust):
```bash
cd rust-grpc 
cargo run --release -- --port 5001 --model=../data/rust_k_means_model.json
```

### Running the benchmark

### Results

The results.

 
## Machine specs

All the benchmarks have been run on the same machine, with following specifics:
- CPU: _AMD Ryzen 7 1700 Eight-Core Processor_
- RAM: _4x8GB DDR4_

