import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(0,10,10)#生成【0-100】之间的100个数据,即 数据集
print(x)
#bins=np.arange(0,101,10)#设置连续的边界值，即直方图的分布区间[0,10],[10,20]...
#直方图会进行统计各个区间的数值
plt.hist(x,color='fuchsia')#alpha设置透明度，0为完全透明
#
plt.xlabel('scores')
plt.ylabel('count')
plt.xlim(0,10)#设置x轴分布范围

plt.show()