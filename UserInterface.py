from tkinter import *
from PIL import Image, ImageTk
import cmd
import time


class App:
    scale = 0.4

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(side=RIGHT)
        button = Button(frame, text='获取截图', command=self.screen_cap)
        button.pack()
        button = Button(frame, text='滑动', command=cmd.swipe_threading)
        button.pack()

        self.label_frame = Frame(master)
        self.label_frame.pack(side=LEFT)
        try:
            image = Image.open(cmd.screen_name)
            image = image.resize((int(image.size[0] * self.scale), int(image.size[1] * self.scale)))
            self.photo = ImageTk.PhotoImage(image)
        except:
            self.photo = None
        self.label = Label(self.label_frame, image=self.photo)
        self.label.bind('<Key>', self.key)
        self.label.bind('<Button-1>', self.click)
        self.label.pack()

    def click(self, event):
        self.label.focus_set()
        x, y = int(event.x / self.scale), int(event.y / self.scale)
        cmd.click(x, y)
        # time.sleep(1)
        # self.screen_cap()

    def key(self, event):
        print(event)
        if event.keysym == 'Up':
            cmd.walk('up-1')
        if event.keysym == 'Down':
            cmd.walk('down-1')
        if event.keysym == 'Right':
            cmd.walk('right-1')
        if event.keysym == 'Left':
            cmd.walk('left-1')
        if event.keysym == 'a':
            cmd.walk('retreat')
        if event.keysym == 's':
            cmd.walk('receive')
        if event.keysym == 'd':
            cmd.walk('attack')
        if event.keysym == 'q':
            cmd.walk('quit')

    def screen_cap(self):
        cmd.screen_cap()
        image = Image.open(cmd.screen_name)
        image = image.resize((int(image.size[0] * self.scale), int(image.size[1] * self.scale)))
        self.photo = ImageTk.PhotoImage(image)
        self.label.configure(image=self.photo)


root = Tk()
app = App(root)
root.mainloop()
root.destroy() 
