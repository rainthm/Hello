# First, let's import the packages that we"ll use in this chapter
import datetime as dt
import xlwings as xw
import pandas as pd
import numpy as np

# Let's create a DataFrame based on pseudorandom numbers and
# with enough rows that only the head and tail are shown
df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Trial {i}" for i in range(1, 6)])
print(df)

# View the DataFrame in Excel
xw.view(df)

# Create a new empty workbook and print its name. This is the
# book we will use to run most of the code samples in this chapter.
book = xw.Book()
print(book.name)


# # Accessing the sheets collection
print(book.sheets)

# # Get a sheet object by index or name. You will need to adjust
# # "Sheet1" if your sheet is called differently.
sheet1 = book.sheets[0]
sheet1 = book.sheets["Sheet1"]

print("A1=",end='')
print(sheet1.range("A1").value)


# # Most common tasks: write values...
sheet1.range("A1").value = [[1, 2],
                            [3, 4]]
sheet1.range("A4").value = "Hello!"


# # ... and read values
print(sheet1.range("A1:B2").value)

# # Slicing
print(sheet1.range("A1:B2")[:, 1])


# # Single cell: A1 notation
print(sheet1["A1"])

# # Multiple cells: A1 notation
# sheet1["A1:B2"]


# # Single cell: indexing
# sheet1[0, 0]


# # Multiple cells: slicing
# sheet1[:2, :2]

# # D10 via sheet indexing
# sheet1[9, 3]

# # D10 via range object
# sheet1.range((10, 4))

# # D10:F11 via sheet slicing
# sheet1[9:11, 3:6]

# # D10:F11 via range object
# sheet1.range((10, 4), (11, 6))

# sheet1["A1"].sheet.book.app

# # Get one app object from the open workbook
# # and create an additional invisible app instance
visible_app = sheet1.book.app
invisible_app = xw.App(visible=False)

# # List the book names that are open in each instance
# # by using a list comprehension
[book.name for book in visible_app.books]

[book.name for book in invisible_app.books]

# # An app key represents the process ID (PID)
xw.apps.keys()

# # It can also be accessed via the pid attribute
xw.apps.active.pid


# # Work with the book in the invisible Excel instance
invisible_book = invisible_app.books[0]
invisible_book.sheets[0]["A1"].value = "Created by an invisible app."

# # Save the Excel workbook in the xl directory
invisible_book.save("destDir/invisible.xlsx")

# # Quit the invisible Excel instance
invisible_app.quit()

app=xw.App(visible=True,add_book=False)
test_book = app.books.open("destDir/invisible.xlsx")
#test_book.open("destDir/invisible.xlsx")

