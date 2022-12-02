import numpy as np
import matplotlib.pyplot as plt

def main():

    limits = [1000,1000]

    santa_warehouse = np.zeros(limits)

    santa = (np.random.randint(limits[0]), np.random.randint(limits[0]))

    start = np.asarray([0,0])
    x = []
    n = 10_000

    for i in range(n):
        step = np.asarray([random_step(), random_step()])
        start = start + step 
        while any(start < 0 ) or any(start > limits[0]):
            step = np.asarray([random_step(), random_step()])
            start = start + step 
        x.append(start)

    x = np.vstack(x)
    plot_walk(x, santa)

    return 0

def random_step(prob=0.5):
    return np.random.choice([-1,1], p=[prob,prob])

def plot_walk(data: list, santa: tuple):

    plt.plot(data[:,0], data[:,1])
    plt.plot(santa[0], santa[1], marker="x", color="red")
    plt.xlabel("lon", fontsize=20)
    plt.ylabel("lat", fontsize=20)
    plt.title("Santa's elves walks")

    plt.savefig("figures/random_walks.png", dpi=300)


if __name__ == "__main__":
    main()
