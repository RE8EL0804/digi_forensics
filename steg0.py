import PIL.Image as IMG
from tkinter import *
from tkinter import filedialog
import os

def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
            # pix[j] -= 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


def encode():
    img = str(filedialog.askopenfile(initialdir="/Home"))
    img = img.split("'")[1]
    image = IMG.open(img, 'r')
    text = hid_img_text.get()
    newimg = image.copy()
    encode_enc(newimg, text)
    new_img_name = img.split(".")[0]+"_enc."+img.split(".")[1]
    newimg.save(new_img_name)

def decode():
    img = str(filedialog.askopenfile(initialdir="/Home"))
    img = img.split("'")[1]
    image = IMG.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            ext_img_ip.insert(0,data)
            break

root = Tk()
root.state("zoomed")


hid_img_text = StringVar()
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
label2 = Label( root, text = "Hide data", font =("Arial", 32))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)
  
frame1= Frame(root)
frame1.place(relx=0.6, rely = 0.45)

hid_img = Label(frame1, text="Hide Text", font=("Arial",10, 'bold'))
hid_img_ip = Entry(frame1, textvariable=hid_img_text, font=("Arial", 10))
sel_img = Label(frame1, text="Select the image: ", font=("Arial",10))
sel_img_but = Button(frame1, text="Browse", font=("Arial",10), command=encode)
hid_img_txt = Label(frame1, text="Enter text to hide: ", font=("Arial",10))

hid_img.grid(row=0, column=0, padx=10, pady=5)
hid_img_txt.grid(row=1, column=0, padx=15, pady=5)
hid_img_ip.grid(row=1, column=1, padx=10, pady=5)
sel_img.grid(row=2, column=0, padx=10, pady=5 )
sel_img_but.grid(row=2, column=1, padx=10, pady=5)

frame2= Frame(root)
frame2.place(relx=0.6, rely=0.6)

ext_img = Label(frame2, text="Extract Text", font=("Arial",10, 'bold'))
ext_sel_img = Label(frame2, text="Select the image: ", font=("Arial",10))
ext_sel_img_but = Button(frame2, text="Browse", font=("Arial",10), command=decode)
ext_img_txt = Label(frame2, text="Hidden text is: ", font=("Arial",10))
ext_img_ip = Entry(frame2, font=("Arial", 10))

ext_img.grid(row=0, column=0, padx=10, pady=5)
ext_img_txt.grid(row=2, column=0, padx=10, pady=5)
ext_img_ip.grid(row=2, column=1, padx=15, pady=8)
ext_sel_img.grid(row=1, column=0, padx=10, pady=5)
ext_sel_img_but.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()