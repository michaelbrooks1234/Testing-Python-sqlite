from src.setup import *
from tkinter import *

def main():
    
    path = "test.db"

    connection = create_connection(path)
    cursor = connection.cursor()

    database = DataBase(connection, cursor)

    database.setup_database()



main()

height = 600
width = 800

root = Tk()
root.geometry(f"{width}x{height}")
root.resizable(False, False)

canvas = Canvas(root, height=height, width=width)
canvas.pack()

frame = Frame(root)
frame.place(relheight=1, relwidth=1)

for i in range(10):
    container = Frame(frame)
    container.grid(column=0, row=i)
    label = Label(container, text="hello World!", height=2, width=10)
    label.grid(column=0, row=0)
    button = Button(container, text="quit", command=root.destroy, height=1, width=5)
    button.grid(column=1, row=0)


root.mainloop()