# code=utf-8
import xlwings as xw
import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



xlsx_market_name = "大华南测试1.xlsx"
xlsx_sop_name = "现有客户&锁定客户去重8.4.xlsx"

#打开市场收集回来的潜客名称表
app = xw.App(visible=False, add_book=False)
market_book = app.books.open(xlsx_market_name)
sheet_market_name = market_book.sheets[1]
total_rows = sheet_market_name.used_range.last_cell.row
print('--------------------------------------------------')
print('本次收集客户总数：',total_rows)
#获取市场部名单表中的客户名称
market_customer_names = sheet_market_name.range((3,6),(total_rows,6)).value
market_customer_full_names = sheet_market_name.range((3,4),(total_rows,4)).value

#xlsx_market = xlrd.open_workbook_xls(xlsx_market_name)
#sheet_market_name = xlsx_market.sheet_by_index(1)
#print(sheet_market_name)
#print(market_customer_names)

#打开现有存量名称表
#app = xw.App(visible=False, add_book=False)
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n存量客户总数：',total_sop_rows,'\n')
print('--------------------------------------------------')
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,6),(total_sop_rows,6)).value



#计算模糊关联度
for i in range(len(market_customer_names)):
    mkt_name = market_customer_names[i]
    full_name = market_customer_full_names[i]
    print(full_name)
    #print("客户全称：" + full_name + "\n")
    print("客户名称简称： " + str(mkt_name) + "\n")
    
    max_corr = 0
    most_likely_sop_name = ''
    for sop_name in sop_customer_names:
        corr = fuzz.ratio(mkt_name, sop_name)
        #print(corr)
        if corr > max_corr:
            max_corr = corr
            most_likely_sop_name = sop_name
            
    if max_corr == 100:
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<命 中 现 网 客 户>>>>>>>>>>>>>>>>>>>>>>>>>>>>：',most_likely_sop_name)
        sheet_market_name.range(i,8).value = "在网客户"
    elif max_corr > 70:
        print('\n--------------------------------------------------------------------------------\n')
        print('             最佳匹配现网客户名称：',most_likely_sop_name)
        print('匹配度(百分制) = ', max_corr,'\n')
        print('--------------------------------------------------------------------------------\n')
    else:
        #print('未找到相对匹配客户，可能是新客户\n')
        pass


market_book.save()
market_book.close()
sop_book.close()
app.quit()

