from tkinter import *
import os

def launch_hash():
    os.startfile('dist\hashing.exe')
    
def launch_stego():
    os.startfile('dist\steg0.exe')

def launch_tools():
    os.startfile('dist\_tool_main.exe')

root = Tk()
root.state("zoomed")

# Add image file
bg = PhotoImage( file = "bg.png")
logo = PhotoImage( file = "logo.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

labellogo = Label( root, image = logo)
labellogo.place(in_=label1, relx = 0.70, rely = 0.02)

labelinfo = Label( root, text="Done by: \n Kethamreddy Karthikeya Reddy \n CH.EN.U4CYS20038 \n Amrita School Of Computing")
labelinfo.place(in_=label1, relx = 0.87, rely = 0.9)
# Add text
label2 = Label( root, text = "Forensics Tools", font =("Arial", 32))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)
  
frame1= Frame(root)
frame1.pack(side=RIGHT, padx=300, pady=300)


# Add buttons
label_pckt = Label(frame1, text = "AVV CYS Tools: ", font =("Arial",16))
button1 = Button( frame1, text = "Launch!!!", command = launch_tools)
label3 = Label( frame1, text = "Steganography: ", font =("Arial", 16))
button2 = Button( frame1, text = "Launch!!!", command = launch_stego)
label_hash = Label(frame1, text = "Hashing : ", font =("Arial",16))
button4 = Button( frame1, text = "Launch!!!", command = launch_hash)


label_pckt.grid(row = 0, column = 0, padx=5, pady=10)
button1.grid(row=0, column=1, padx=5, pady=10)
label3.grid(row=1, column=0, padx=5, pady=10)
button2.grid(row=1, column=1, padx=5, pady=10)
label_hash.grid(row = 2, column = 0, padx=5, pady=10)
button4.grid(row=2, column=1, padx=5, pady=10)

root.mainloop()