import matplotlib.pyplot as plt

#x = [1,2,3,4,5]
#y = [1,4,9,16,25]
x = list(range(1,1001))
y = [i**2 for i in x]
plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolors='none', s=40)
plt.title("Square numbers", fontsize=20)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()