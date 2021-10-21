import pygal
from die import Die

#create a D6
die = Die()

#掷骰子，将结果保存在列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
#print(results)
#分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
hist = pygal.Bar()

hist._title = "Result of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')