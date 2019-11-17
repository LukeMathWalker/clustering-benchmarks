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

### Running the benchmark

```bash

```

### Results

The results.

 
## Machine specs

All the benchmarks have been run on the same machine, with following specifics:
- CPU: _AMD Ryzen 7 1700 Eight-Core Processor_
- RAM: _4x8GB DDR4_

