import matplotlib.pyplot as plt

x = [1,2,3,4,5]
squares = list(i**2 for i in x)
plt.plot(x,squares,linewidth=5)
plt.show()