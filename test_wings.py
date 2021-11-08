import xlwings as xw

app = xw.App(visible=False, add_book=False)
save_app = xw.App(visible=False)
save_book = save_app.books[0]
print(save_book)
save_sheet1 = save_book.sheets[0]
#app.display_alerts=False
#app.screen_updating=False
#wb = app.books.open(path)
#获取excel中的表单
path = 'd:/test1.xlsx'
#wb = app.books.open('d:/test1.xlsx')
wb = app.books.open(path)
#wb = xw.Book(path)
sheet1 = wb.sheets[1]
print(sheet1)

print("A1=",end='')
print(sheet1.range("A1").value)

total_rows = sheet1.used_range.last_cell.row
total_cols = sheet1.used_range.last_cell.column
print(f"There are {total_rows} rows in the sheet")

# for row_num in range(1,total_rows+1):
#     value = sheet1.range(f'A{row_num}').expand('right').value
#     print(value)


first_row = sheet1.range('A1').expand('right').value
#for i in range(0,len(first_row)):
    #save_sheet1.range(1,i).value = first_row[i]
#    print(first_row[i])
save_sheet1.range(1,1).expand('right').value = first_row

wb.save()
wb.close()

save_book.save('d:/test2.xlsx')
save_book.close()
app.quit()

