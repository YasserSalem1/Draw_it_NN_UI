from tkinter import *
from tkinter import ttk
from PIL import ImageGrab
import win32gui
from tensorflow import keras
import pyttsx3

engine = pyttsx3.init()
import time

model = keras.models.load_model('QuickDraw.h5')
import cv2 as cv

import numpy as np


def btn_clicked1():
    canvas2.delete("all")
    # canvas3.delete(widget)  # Deletes the rectangle
    note.select(1)


def btn_clicked():
    exit(0)


import cv2


def keras_process_image(img):
    image_x = 28
    image_y = 28
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    # img /= 255.0
    return img


"""
def getter(widget):

    x=window.winfo_rootx()+widget.winfo_x()
    y=window.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()







"""
import matplotlib.pyplot as plt


def save():
    HWND = canvas2.winfo_id()  # get the handle of the canvas
    rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas

    # ImageGrab.grab(rect).save("lol.PNG") # get image of the current location

    ImageGrab.grab(rect).crop((300, 200, 500, 400)).save("new.PNG")

    import imageio

    im = imageio.v2.imread('new.PNG')
    im1 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im2 = cv2.resize(im1, (28, 28))

    plt.figure()
    plt.imshow(im2, cmap='gray')
    plt.show()

    new_img = keras_process_image(im)

    class_names = ['sun', 'ocean', 'shorts', 'ice cream', 'fish', 'palm tree', 'sailboat', 'tent', 'pineapple']
    pred_prob = model.predict(new_img)[0]
    print(pred_prob)
    #pred_prob = np.argmax(pred_prob,axis=0)
    pred_class=list(pred_prob).index(max(pred_prob))
    out=class_names[pred_class]



    note.select(2)

    # label = Label(canvas3, text='Sure that it is', font=("Courier", 30)).place(x=440, y=150)

    # label = Label(canvas3, text='or maybe it is', font=("Courier", 30)).place(x=440, y=250)

    label = Label(canvas3, text=out, font=("Courier", 30)).place(x=440, y=200)

    #label = Label(canvas3, text=class_names[pred_class], font=("Courier", 30)).place(x=440, y=300)


"""
    engine.say("The model is sure it is a drawing of")
    engine.runAndWait()
    engine.say(class_names[pred_class])
    engine.runAndWait()
    engine.say("Or maybe it is a drawing of")
    engine.runAndWait()
    engine.say(class_names[pred_prob[1]])
    engine.runAndWait()
"""

"""

"""


def select():
    note.select(1)


def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y
    print(current_x, current_y)
    # NIIIIIIIIIIIIIIIIIICEEEEEEEEEEEEEEEEEEE


def addline(event):
    global current_x, current_y
    canvas2.create_line(current_x, current_y, event.x, event.y, width=10, fill='Black',
             capstyle=ROUND, smooth=TRUE, splinesteps=36)
    #canvas2.create_oval(current_x, current_y, event.x, event.y, width=10, )

    # UPDATEE STARTING VALUE
    current_x, current_y = event.x, event.y


window = Tk()

note = ttk.Notebook(window)
note.pack()
window.geometry("1000x800")
window.configure(bg="#fcc32e")
canvas = Canvas(
    window,
    bg="#fcc32e",
    height=800,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    window,
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=select,
    relief="flat")

b0.place(
    x=314, y=304,
    width=285,
    height=77)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    860.5, 375.0,
    image=background_img)

canvas2 = Canvas(
    bg="#ffffff",
    height=800,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas2.place(x=0, y=0)

img02 = PhotoImage(file=f"img02.png")
b0 = Button(
    canvas2,
    image=img02,
    borderwidth=0,
    highlightthickness=0,
    command=save,
    relief="flat")

b0.place(
    x=385, y=674,
    width=229,
    height=55)

canvas2.bind('<Button-1>', locate_xy)
canvas2.bind('<B1-Motion>', addline)

canvas3 = Canvas(
    window,
    bg="#fb676a",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas3.place(x=0, y=0)

last1 = PhotoImage(file=f"againn.png")
b012 = Button(
    canvas3,
    image=last1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked1,
    relief="flat")

b012.place(
    x=536, y=422,
    width=229,
    height=100)

img12 = PhotoImage(file=f"quitt .png")
b12 = Button(
    canvas3,
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b12.place(
    x=218, y=426,
    width=229,
    height=78)

background_img_l = PhotoImage(file=f"backk.png")
background_l = canvas3.create_image(
    500.0, 146.0,
    image=background_img_l)

"""image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)
"""
note.add(canvas)
note.add(canvas2)
note.add(canvas3)

window.mainloop()