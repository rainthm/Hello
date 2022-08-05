# code=utf-8
import xlwings as xw
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#用于根据字典表，将市场收集到的公司文件名，进行主体词提取，并存在源文件的第6列

dict = {'(',')','（','）'}
try:
    fR = open('..\dict.txt', 'r', encoding='UTF-8')
    with fR:
        for line in fR:
            line = line.strip('\n');
            dict.add(line)
except FileNotFoundError:
    print("打开字典文件失败！请检查dict.txt文件是否存在。")
  

############################################################################################################################
#打开现有存量名称表
app = xw.App(visible=False, add_book=False)
xlsx_sop_name = "现有客户&锁定客户去重8.4.xlsx"
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n存量客户总数：',total_sop_rows,'\n')
print('--------------------------------------------------')
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,6),(total_sop_rows,6)).value
for i in range(0, total_sop_rows-1):
    print(sop_customer_names[i])

sop_book.close()
app.quit()
