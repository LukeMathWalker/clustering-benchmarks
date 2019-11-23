# Run server

```
cargo run --release -- --model=../data/rust_k_means_model.json
```

# Run client

```
cargo run --bin client
```

# Benchmark 

```
ghz --proto=protos/centroids.proto --call=ml.ClusteringService.Predict --insecure --data-file=../data/observations.json localhost:8000
```

# Generate samples

```
cargo run --bin gentestdata -- --features=2 --samples=10000
```
OR
```
cargo run --bin gentestdata -- batch --batches=1000 --samples=10
```

# Train and serialise model 

```
cargo run --bin train_model -- --features=2 --centroids=100 --output=../data/rust_k_means_model.json
```