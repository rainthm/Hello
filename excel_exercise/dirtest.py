import os.path
import xlwings as xw
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
path = '.\excel\\'
print(path)
if not os.path.exists(path):
        os.mkdir(path)

origin_path = current_path + path
print(origin_path)

file_name = 'test.txt'
file_name = origin_path+'\\'+file_name
with open(file_name,'w') as file_object:
    file_object.write("I love you.")
    
app = xw.App(visible=True, add_book=False)
app.display_alerts=False   #不显示Excel消息框
app.screen_updating=False  #关闭屏幕更新,可加快宏的执行速度


excel_file_name = '1.xlsx'
excel_file_name = origin_path + '\\' + excel_file_name

wb = app.books.open(excel_file_name)
print(wb.fullname)       # 输出打开的excle的绝对路径

sheet = wb.sheets["sheet1"]
sheet.range('A1:C1').value = ['I','Love','You']
print('value of A1:C1:',sheet.range('A1:C1').value)

wb.save()
wb.close()
app.quit()