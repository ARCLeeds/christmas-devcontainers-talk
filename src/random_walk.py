import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI


def main():

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    x = []
    n = 1000

    if rank == 0:

        limits = [100, 100]

        santa_warehouse = np.zeros(limits)

        santa = (np.random.randint(limits[0]), np.random.randint(limits[0]))

        start = np.asarray([0, 0])

    else:
        limits, santa_warehouse, santa = (
            None,
            None,
            (np.empty(1, dtype="i"), np.empty(1, dtype="i")),
        )
        start = np.empty([1, 1], dtype="i")

    limits = comm.bcast(limits, root=0)
    santa_warehouse = comm.bcast(santa_warehouse, root=0)
    santa = comm.bcast(santa, root=0)
    start = comm.bcast(start, root=0)

    print("Running markov chain on rank: ", rank)
    for i in range(n):
        step = np.asarray([random_step(), random_step()])
        start = start + step
        if any(start < 0):
            start[start < 0] = random_step(1.0)
        elif any(start > limits[0]):
            start[start > limits[0]] = random_step(0)
        else:
            start
        x.append(start)

    x = list(x)

    data = comm.gather(x, root=0)

    if rank == 0:
        plot_walk(data, santa)

    return 0


def random_step(prob=0.5):
    return np.random.choice([-1, 1], p=[1 - prob, prob])


def plot_walk(data: list, santa: tuple):

    for item in data:
        item = np.vstack(item)
        plt.plot(item[:, 0], item[:, 1])
    plt.plot(santa[0], santa[1], marker="x", color="red")
    plt.xlabel("lon", fontsize=20)
    plt.ylabel("lat", fontsize=20)
    plt.title("Santa's elves walks")

    plt.savefig("figures/random_walks.png", dpi=300)


if __name__ == "__main__":
    main()
