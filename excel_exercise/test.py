import xlwings as xw
import pandas as pd 
import os.path
import numpy as np
import matplotlib.pyplot as plt


app=xw.App(visible=True,add_book=False)
app.display_alerts=False   #不显示Excel消息框
app.screen_updating=False  #关闭屏幕更新,可加快宏的执行速度
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
path = 'D:/Python/excels/1.xlsx'
#wb=app.books.open('1.xlsx')
wb=app.books.open(path)
print(wb.fullname)       # 输出打开的excle的绝对路径

# 在A1单元格写入值
# 实例化一个工作表对象
sheet1 = wb.sheets["sheet1"]
# 或者
# sheet1 =xw.books['1.xlsx'].sheets['sheet1']
# print(sheet1.name) 输出工作簿名称
# 写入值
sheet1.range('A1').value = 'python知识学堂'
# 读值并打印
print('value of A1:',sheet1.range('A1').value)
# 清空单元格内容,如果A1中是图片，此方法没有效果
sheet1.range('A1').clear()
# 传入列表写入多行值
sheet1.range('A1').value = [['a','b','c'],[1,2,3]]
print('value of A1:',sheet1.range('A1:B3').value)

# 当然也可以将pandas的DataFrame数据写入

# df = pd.DataFrame([[1,2], [3,4]], columns=['A', 'B'])
# sheet1.range('A1').value = df
# # 读取数据，输出类型为DataFrame
# print(sheet1.range('A1').options(pd.DataFrame, expand='table').value)


# 支持添加图片的操作
fig = plt.figure()
x = range(1,5)
plt.plot(x, np.log(x))
sheet1.pictures.add(fig, name='MyPlot', update=True)

n =65
n = chr(n)# ASCII字符
pos ='%s%d' % (n,2)
print(pos)#A2
print(sheet1.range(pos).value)

wb.save()
wb.close()
app.quit()  # 退出excel程序，
# app.kill() 通过杀掉进程强制Excel app退出​
# 以第一种方式创建Book时，打开文件的操作可如下
#wb = xw.Book('1.xlsx')