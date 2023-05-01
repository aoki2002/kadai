from module.screen import main
import sqlite3
import tkinter

def show(canvas):
    canvas.place_forget()

    canvas_list = tkinter.Canvas(width=800, height=400)
    canvas_list.place(x=0, y=0)

    btn1_list = tkinter.Button(canvas_list, text='Top', command=lambda: main.show(canvas_list))
    btn1_list.place(x=0, y=0)

    box1_list = tkinter.Entry(canvas_list, width=10)
    box1_list.place(x=300, y=100)

    btn2_list = tkinter.Button(canvas_list, text='検索', command=lambda: back())
    btn2_list.place(x=400,y=100)

    box2_list = tkinter.Text(canvas_list, width=50, height=50)
    box2_list.place(x=150, y=150)

    def back():
        db = "company.db"
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        for row in cur.execute(f"SELECT * from abc"):
            box2_list.insert(tkinter.END, f"{row}\n")

        conn.commit()
        conn.close()

    