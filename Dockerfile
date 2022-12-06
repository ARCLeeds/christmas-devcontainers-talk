FROM condaforge/mambaforge

RUN apt update -y && apt install -y openssh-client

RUN useradd -m conda 

USER conda

COPY --chown=conda ./ /app/

WORKDIR /app/

RUN mamba env create -f /app/environment.yml

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh","mpiexec","-np","4","python","/app/src/random_walk.py"]
ENTRYPOINT [ "/app/entrypoint.sh" ]