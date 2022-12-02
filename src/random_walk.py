import numpy as np
import matplotlib.pyplot as plt

def main():

    start = 0
    x = []
    n = 10_000

    for i in range(n):
        step = np.random.choice([-1,1], p=[0.5,0.5])
        start = start + step 
        x.append(start)

    plot_walk(x)

    return 0


def plot_walk(data: list):

    plt.plot(data)
    plt.xlabel("Steps", fontsize=20)
    plt.ylabel(r"$S_{n}$")
    plt.title("Santa's elves walks")

    plt.savefig("figures/random_walks.png", dpi=300)


if __name__ == "__main__":
    main()