Bootstrap: docker
From: condaforge/mambaforge
Stage: spython-base

%files
    --chown=conda /app/
    ./ /app/

%post

    apt update -y && apt install -y openssh-client

    useradd -m conda

    su -  conda # USER conda


    mkdir -p /app/
    cd /app/

    mamba env create -f /app/environment.yml

    chmod +x /app/entrypoint.sh

%runscript
    cd /app/
    exec /app/entrypoint.sh /app/entrypoint.sh mpiexec -np 4 python /app/src/random_walk.py "$@"
    %startscript
    cd /app/
    exec /app/entrypoint.sh /app/entrypoint.sh mpiexec -np 4 python /app/src/random_walk.py "$@"