import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def getImage(path):
   return OffsetImage(plt.imread(path, format="png"), zoom=.1)

x = [8, 4, 3, 6]
y = [5, 3, 4, 7]
fig, ax = plt.subplots()

ab = AnnotationBbox(getImage("static/santa-claus.png"), (2, 3), frameon=False)
ax.add_artist(ab)
plt.xticks(range(10))
plt.yticks(range(10))
plt.savefig("./testfig.png", dpi=300)