import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI


def main():

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    x = []
    n = 10_000

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
    
    santa_found = None

    limits = comm.bcast(limits, root=0)
    santa_warehouse = comm.bcast(santa_warehouse, root=0)
    santa = comm.bcast(santa, root=0)
    start = comm.bcast(start, root=0)

    print("Running markov chain on rank: ", rank)
    for i in range(n):
        if santa_found == True:
            print("Santa found breaking rank: ", rank)
            break
        else: 
            step = np.asarray([random_step(), random_step()])
            test_step = start + step
            if any(test_step < 0):
                step[test_step < 0] = random_step(1.0)
                start = start + step
            elif any(test_step > limits[0]):
                step[test_step > limits[0]] = random_step(0)
                start = start + step
            else:
                start = start + step
            x.append(start)

            if all(start == santa):
                santa_status = True
                found_rank = rank
                print("Rank ", found_rank, " found santa!")
            else:
                santa_status = False
                found_rank = 0

            santa_found = comm.bcast(santa_status, root=found_rank)

    x = list(x)

    data = comm.gather(x, root=0)

    if rank == 0:
        plot_walk(data, santa)
        for idx, item in enumerate(data):
            item = np.vstack(item)
            np.savetxt(f"figures/data_{idx}.txt", item, fmt="%1f")

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
