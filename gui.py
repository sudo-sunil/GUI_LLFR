import lbp_face_recognition

from Tkinter import *
import tkFileDialog
from Tkinter import Label,Tk
from PIL import Image, ImageTk

class home:
    def __init__(self,master):

        lbp_face_recognition.train()

        

        self.master=master
        self.f=Frame(master,width=1000,height=600)
        self.f.propagate(0)
        self.f.pack()
        self.f["bg"]='#2874A6'
        heading=Label(self.f,text="Low Light Facial Recognition",bg='#2874A6',font=('Times new Roman',-50,'bold')).grid(row=1,column=2,padx=20,pady=50)
        #heading.place(x=350,y=200)
        buttonchoose=Button(self.f,text="Choose Test Image",command=self.choose,font=('times new roman',-20),width=15,height=3).grid(row=6,column=1,padx=20,pady=50)
        buttontest=Button(self.f,text="Find Match",command=self.test,font=('times new roman',-20),width=15,height=3).grid(row=7,column=1,padx=20,pady=50)
        

    def choose(self):
        global path
        path=tkFileDialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        im2 = im.resize((250, 250), Image.ANTIALIAS)
        
        tkimage = ImageTk.PhotoImage(im2)
        
        myvar1=Label(self.f,image = tkimage).grid(row=6,column =2)
        myvar1.image = tkimage
        myvar1.pack()

    def test(self):
        match_path = lbp_face_recognition.hist_get(path)
        im = Image.open(match_path)
        im2 = im.resize((250, 250), Image.ANTIALIAS)
        
        tkimage = ImageTk.PhotoImage(im2)
        
        myvar2=Label(self.f,image = tkimage).grid(row=7,column =2)
        myvar2.image = tkimage
        myvar2.pack()
    

        

root=Tk()
home=home(root)
root.mainloop()
