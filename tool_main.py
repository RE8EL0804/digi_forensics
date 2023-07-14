from tkinter import *
import os

def launch_s1():
    os.startfile("dist\s1.exe")
    
def launch_s2():
    os.startfile("dist\s2.exe")
    
def launch_s3():
    os.startfile("")
def launch_s4():
    os.startfile("")
def launch_s5():
    os.startfile("")
def launch_s6():
    os.startfile("")
    
root1 = Tk()
root1.state("zoomed")
# Add image file
bg = PhotoImage( file = "bg.png")
logo = PhotoImage( file = "logo.png")

# Show image using label
label1 = Label( root1, image=bg)
label1.place(x = 0,y = 0)

labellogo = Label( root1, image = logo)
labellogo.place(in_=label1, relx = 0.70, rely = 0.02)

labelinfo = Label( root1, text="Done by: \n Kethamreddy Karthikeya Reddy \n CH.EN.U4CYS20038 \n Amrita School Of Computing")
labelinfo.place(in_=label1, relx = 0.87, rely = 0.9)
# Add text
label2 = Label( root1, text = "AVV CYS Tools: ", font =("Arial", 50))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)
  
frame= Frame(root1)
frame.place(relx=0.6, rely=0.4)



label_s1 = Label(frame, text = "SEM 1 tools: ", font =("Arial", 16))
button_s1 = Button(frame, text="Launch!!!", command = launch_s1)
label_s2 = Label(frame, text = "SEM 2 tools: ", font =("Arial", 16))
button_s2 = Button(frame, text="Launch!!!", command = launch_s2)
label_s3 = Label(frame, text = "SEM 3 tools: ", font =("Arial", 16))
button_s3 = Button(frame, text="Launch!!!", command = launch_s3)
label_s4 = Label(frame, text = "SEM 4 tools: ", font =("Arial", 16))
button_s4 = Button(frame, text="Launch!!!", command = launch_s4)
label_s5 = Label(frame, text = "SEM 5 tools: ", font =("Arial", 16))
button_s5 = Button(frame, text="Launch!!!", command = launch_s5)
label_s6 = Label(frame, text = "SEM 6 tools: ", font =("Arial", 16))
button_s6 = Button(frame, text="Launch!!!", command = launch_s6)

label_s1.grid(row = 0, column = 0, padx=10, pady=10)
button_s1.grid(row = 0, column = 1, padx=10, pady=10)
label_s2.grid(row = 1, column = 0, padx=10, pady=10)
button_s2.grid(row = 1, column = 1, padx=10, pady=10)
label_s3.grid(row = 2, column = 0, padx=10, pady=10)
button_s3.grid(row = 2, column = 1, padx=10, pady=10)
label_s4.grid(row = 3, column = 0, padx=10, pady=10)
button_s4.grid(row = 3, column = 1, padx=10, pady=10)
label_s5.grid(row = 4, column = 0, padx=10, pady=10)
button_s5.grid(row = 4, column = 1, padx=10, pady=10)
label_s6.grid(row = 5, column = 0, padx=10, pady=10)
button_s6.grid(row = 5, column = 1, padx=10, pady=10)
root1.mainloop()