import pygal
import matplotlib.pyplot as plt
from die import Die

#创建两个骰子
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(10):
    result = die_1.roll() * die_2.roll()
    results.append(result)
print(results)
#计算各种乘积的可能性，乘积，也就是X轴的下标
nfs = set()
for v1 in range(1, die_1.num_sides+1):
    for v2 in range(1, die_2.num_sides+1):
        nfs.add(v1*v2)    

sorted_nfs = list(sorted(nfs))

#统计各乘积出现的频率
frequencies = []
for value in sorted_nfs:
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化结果
hist = pygal.Bar()

xlabel = []
for xmark in sorted_nfs:
    xlabel.append(str(xmark))
#print(xlabel)
hist._title = "Result of rolling 2 D6 1000 times."
#hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = xlabel
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6*D6', frequencies)
hist.render_to_file('die_visual.svg')

#plt.hist(results,color='red',rwidth=0.2)
plt.bar(sorted_nfs,frequencies)
plt.show()