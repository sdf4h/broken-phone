
from tkinter import Tk, Canvas, OptionMenu, StringVar
import tkinter
from tkinter import messagebox as mbox
import os
from tkinter import colorchooser
from tkinter.ttk import *
import PIL
from PIL import Image, ImageDraw

root = Tk()
root.geometry("1200x800")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cn = Canvas(root, bg='white', height=30, width=30)
canvas = Canvas(root, bg='white', height=screen_height, width=screen_width)
root.title('Paint')
hx = None
value_color = None
rgb = None
col = (255, 255, 255)


def draw(event):
    value = variable.get()
    if value and hx:
        canvas.create_oval((event.x - int(value) // 2, event.y - int(value) // 2),
                           (event.x + int(value) // 2, event.y + int(value) // 2), fill=hx, outline=hx)

        drawer.ellipse((event.x - int(value) // 2, event.y - int(value) // 2,
                  event.x + int(value) // 2, event.y + int(value) // 2), hx)
    else:
        mbox.showerror("Ошибка", "Выберите цвет для рисования!")


def dalate():
    global image, drawer
    pixels = image.load()
    x, y = image.size
    for i in range(x):
        for j in range(y):
            pixels[i, j] = (255, 255, 255)
    canvas.config(bg='white')
    canvas.delete("all")


def zal():
    global image, col, drawer
    if hx:
        canvas.config(bg=hx)
        im = PIL.Image.new('RGB', (screen_width, screen_height), color=hx)
        pixels = image.load()
        pixels2 = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r1, g1, b1 = pixels[i, j]
                if (r1, g1, b1) != col:
                    pixels2[i, j] = int(r1), int(g1), int(b1)
        image = im
        drawer = ImageDraw.Draw(image)
        del im
        col = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    else:
        mbox.showerror("Ошибка", "Выберите цвет заливки!")


def save():
    if not os.path.exists(f'{text.get()}.png'):
        image.save(f'{text.get()}.png')
    else:
        mbox.showerror("Ошибка", "Файл с таким именем существует!")


def color():
    global hx, rgb
    (rgb, hx) = colorchooser.askcolor()
    cn.config(bg=hx)


image = PIL.Image.new('RGB', (screen_width, screen_height), 'white')
drawer = ImageDraw.Draw(image)

variable = StringVar(root)
shr = OptionMenu(root, variable, 15, 1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100)

bytton = tkinter.ttk.Button(root, text='Выбрать цвет', command=color)
btn = tkinter.ttk.Button(root, text='Очистить всё', command=dalate)
btno = tkinter.ttk.Button(root, text='Заливка', command=zal)
lable = tkinter.ttk.Label(root, text='Размер кисти:')
lable_2 = tkinter.ttk.Label(root, text='Цвет кисти (заливки):')
lable_3 = tkinter.ttk.Label(root, text='Название файла:')
btn2 = tkinter.ttk.Button(root, text='Save', command=save)
text = tkinter.ttk.Entry()
canvas.bind("<B1-Motion>", draw)
canvas.bind('<Button-1>', draw)

bytton.grid(column=59, row=1)
lable_3.grid(column=1, row=0, pady=7)
text.grid(column=3, row=0)
btn2.grid(column=9, row=0)
btn.grid(column=19, row=0, padx=100)
btno.grid(column=29, row=0, padx=50)
lable.grid(column=39, row=0, padx=50)
shr.grid(column=39, row=1, padx=50)
lable_2.grid(column=59, row=0, padx=25)
canvas.place(x=0, y=70)
cn.grid(column=69, row=1)

root.mainloop()