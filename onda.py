import seaborn as sns
from numpy import sin

x = [x*0.1 for x in range(100)]

sns.set()

y = sin(x)

plt.plot(x,y)

plt.show()

