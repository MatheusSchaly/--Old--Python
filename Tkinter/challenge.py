import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry("155x185")
mainWindow["padx"] = 8

# Screen
screen = tkinter.Entry(mainWindow)
screen.grid(row=0, column=0, ipadx=25)

# Buttons frame
numberButtonsFrame = tkinter.Frame(mainWindow)
numberButtonsFrame.grid(row=2, column=0, ipadx=9)

# Upper buttons
tkinter.Button(numberButtonsFrame, text="C").grid(row=0, column=0, ipadx=12)
tkinter.Button(numberButtonsFrame, text="CE").grid(row=0, column=1, ipadx=9)

# Number buttons
number = 1
for row in range(4, 1, -1):
    for column in range(0, 3):
        tkinter.Button(numberButtonsFrame, text=number).grid(row=row, column=column, ipadx=13)
        number += 1

# Rightmost buttons
tkinter.Button(numberButtonsFrame, text="+").grid(row=2, column=3, ipadx=11)
tkinter.Button(numberButtonsFrame, text="-").grid(row=3, column=3, ipadx=13)
tkinter.Button(numberButtonsFrame, text="*").grid(row=4, column=3, ipadx=13)

# Bottommost buttons
tkinter.Button(numberButtonsFrame, text="0").grid(row=5, column=0, ipadx=13)
tkinter.Button(numberButtonsFrame, text="=").grid(row=5, column=1, columnspan=2, ipadx=33)
tkinter.Button(numberButtonsFrame, text="/").grid(row=5, column=3, ipadx=13)

mainWindow.update()
mainWindow.minsize(height=155, width=185)
mainWindow.maxsize(height=200, width=230)
mainWindow.mainloop()
