# Devcontainers talk for Christmas Conference 2022

This is a toy repository that includes some MPI-enabled Markov chain random walks to search a 2D space for Santa 🎅!

It's intention is to showcase using containers to enable portable and scalable code reuse.

## Usage

### Docker

This repository contains a Dockerfile for creating a container image and running locally.

```bash
$ docker build . -t find-santa:latest

$ mkdir santa-search-outputs

$ docker run -v $(pwd)/santa-search-outputs:/app/figures find-santa:latest
```

You can then check inside `santa-search-outputs` directory to find the data visualisation plot.

### Apptainer

This repository includes an [Apptainer](https://apptainer.org/) definition file that can be built using Apptainer.

```bash
$ apptainer build find-santa.sif Singularity.def

$ mpiexec -np 4 apptainer exec find-santa.sif conda run -n devcontainers python /app/src/random_walk.py

```


