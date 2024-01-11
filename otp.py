import random
from tkinter import *
from tkinter import ttk

class otp:
    def __init__(self,window):
        self.window = window
        self.window.title("One Time Password Generator")
        self.window.geometry("1920x1080+0+0")
        
        title = Label(self.window,text="One Time Password Generator",bd=0,font=("Lucida Bright",30,"bold"),bg="#409AE0",fg="black")
        title.pack(side=TOP,fill=X)

        def generate_OTP():
            otp = random.randint(1000, 9999)         
            label2 = Label(frame1,text=otp,bg="white",fg="black",font=("Lucida Bright",20,"bold"))
            label2.grid(row=6,column=2,padx=600,pady=50)

        frame1 = Frame(self.window,bd=3,relief=RIDGE,bg="#F97FFF")
       
        frame1.place(x=20,y=70,height=550,width=1230)
        
        label1 = Label(frame1,text="Click on the button to generate OTP ",bg="white",fg="black",font=("Lucida Bright",20))
        label1.grid(row=4,column=2,padx=380,pady=60)

        generate_button = Button(frame1,text="Generate OTP",height=1,width=11,bg="white",fg="black",font=("Lucida Bright",10), command=generate_OTP)
        generate_button.grid(row=5, column=2,pady=10,padx=10)
window = Tk()
ob = otp(window)
window.mainloop()
