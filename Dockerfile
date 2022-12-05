FROM condaforge/mambaforge

COPY ./ /app/

RUN mamba env create -f /app/environment.yml

ENTRYPOINT ["conda run -n devcontainers","mpiexec","-np","4","python","/app/src/random_walk.py"]