import os
import xlwings as xw
import time
"""
需求：
    1. 将若干个Excel表合并成一个表里
    2. 不管你用什么方法，实现效果就行
"""
"""
思路分析：
    1. 创建一个空表名叫"总表"，表格形式须和合并表的一样
    2. 获取需要合并文件夹中的所有excel表的名字（文件名)
    3. 开始遍历excel表
    4. 先读取数据，然后写入事先创建好总表中
    5. 当读取完下一个待合并表的数据，然后准备写入到总表时，必须先获取到总表的行数，不然之前的数据将会被覆盖掉。
    6. 遍历结束，保存总表的数据
"""
"""
项目运行：
    1. 将所有需要合并的表放到一个文件夹中，名叫excels
    2. autoMerge.py文件和excels文件夹同级
    3. 运行该.py文件，会在把合并表放到destDir夹中
"""
def initExcel(dest_path, sourceExcel_path,total_sheet_name):
    """
    :param destExcel_path: 合并总表excel的路径
    :param sourceExcel_path: 需要合并excel的路径
    :param total_sheet_name: 合并总表后sheet的名字
    :return: 返回False or True
    """
   # try:
    #创建一个工作簿用于要存放汇总结果
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    #创建一个表单
    #sht = wb.sheets.add(name=total_sheet_name)
    sht = wb.sheets[0]
    #获取待需合并的excel的所有文件
    excel_name_list = get_All_Excelname(sourceExcel_path)
    #第一个待合并的excel文件的路径
    excel_path = sourceExcel_path + excel_name_list[0]
    print(excel_path)
    # 获取excel的sheet
    epp = xw.App(visible=False,add_book=False)
    e_b = epp.books.open(excel_path)
    e_s = e_b.sheets[1]
    # 获取excel表头的数据
    first_row = e_s.range('A1').expand('right').value
    #将表的名字拷贝过来
    sht.name = e_s.name
    #将表头的名字拷贝过来
    sht.range(1,1).expand('right').value = first_row

    #保存汇总表的名字
    wb.save(dest_path)
    wb.close()

    e_b.save()
    e_b.close()

    app.quit()
    epp.quit()
    return True
    #except Exception as e:
    #    return True
# 创建文件夹
def makeDir(path):
    """
    :param path: 传入需要创建文件夹的路径
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)
# 2.获取需要合并的所有的excel文件名
def get_All_Excelname(path):
    """
    :param path: 待合并excel文件的路径
    :return:
    """
    excelName_list = os.listdir(path)
    # print(excelName_list)
    return excelName_list
# 返回excel表的sheet对象

def get_excel_sheet(path):
    """[summary]

    Args:
        path ([字符串]]): [存放待合并文件]

    Returns:
        [type]: [description]
    """
    #打开制定路径的excel表
    app = xw.App(visible=True, add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    wb = app.books.open(path)
    #获取excel中的表单
    #wb = app.books.open(r'd:\test1.xlsx')
    sheet = wb.sheets[1]
    wb.save()
    wb.close()
    app.quit()
    return sheet

def writeExcel(destExcel_path,source_path,excelName_list):
    """

    :param destExcel_path: 合并总表存放的路径
    :param source_path: 需要合并excel的路径
    :param excelName_list: 需要合并excel表的文件名称
    :return:
    """

    #获取总表行数
    app = xw.App(visible=False, add_book=False)
    total_book = app.books.open(destExcel_path)
    total_sheet = total_book.sheets[0]
    total_rows = total_sheet.used_range.last_cell.row
    #循环获取列表中的表单
    for excel_name in excelName_list:
        # 文件路径
        excel_path = source_path + excel_name
        print("###正在合并表格《"+excel_path+"》,请稍等……")
        # 获取表的sheet对象
        e_b = app.books.open(excel_path)
        # 默认合并的是sheet[1],不是合并sheet[0]
        e_s = e_b.sheets[1]
        #循环拷贝sheet中除首行外的各行
        for i in range(2,e_s.used_range.last_cell.row):
            line = e_s.range(f'A{i}').expand('right').value
            total_sheet.range(i+total_rows-1,1).expand('right').value = line
        #一个表单合并完成，则总表的行数增加
        total_rows += i
        e_b.save()
        e_b.close()
    #合并完成，关闭总表文件
    print("###合并结束！")
    total_book.save()
    total_book.close()
    app.quit()



def main():
    # 待需合并的excel文件夹路径
    source_excel_path = "./excels/"
    # 存放合并后的excel表文件夹路径
    dest_dir = "./destDir"
    # 创建文件夹
    makeDir(dest_dir)
    # 合并excel表名
    total_excel_name = "总表.xlsx"
    # 合并表存放路径
    total_excel_path = dest_dir + "/" + total_excel_name
    # 合并总表中的sheet的名字
    total_excel_sheet_name = "汇总表"
    # 初始化表
    flag = initExcel(total_excel_path,source_excel_path,total_excel_sheet_name)
    if flag:
        print("###总表空表建立完成")
    else:
        print("@@初始化总表失败")
    
    #开始合并
    excelName_list = get_All_Excelname("./excels")
    writeExcel(total_excel_path,source_excel_path,excelName_list)

if __name__ == '__main__':
    main()
    time.sleep(3)        