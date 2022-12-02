import numpy as np
import matplotlib.pyplot as plt

def main():

    santa_warehouse = np.zeros([100,100])

    santa = (np.random.randint(100), np.random.randint(100))

    start = np.asarray([0,0])
    x = []
    n = 10_000

    for i in range(n):
        step = np.asarray([random_step(), random_step()])
        start = start + step 
        while any(start < 0 ) or any(start > 100):
            step = np.asarray([random_step(), random_step()])
            start = start + step 
        x.append(start)

    plot_walk(x)

    return 0

def random_step(prob=0.5):
    return np.random.choice([-1,1], p=[prob,prob])

def plot_walk(data: list):

    plt.plot(data)
    plt.xlabel("Steps", fontsize=20)
    plt.ylabel(r"$S_{n}$")
    plt.title("Santa's elves walks")

    plt.savefig("figures/random_walks.png", dpi=300)


if __name__ == "__main__":
    main()