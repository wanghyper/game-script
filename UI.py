from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as messageBox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.tkImage = ImageTk.PhotoImage(image=Image.open('./screen.png'))
        self.label = Label(self, image=self.tkImage)
        self.label.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()