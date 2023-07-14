from tkinter import *
from tkinter import filedialog
import hashlib
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
label2 = Label( root1, text = "Hashing", font =("Arial", 50))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)
  
frame_md5= Frame(root1)
frame_md5.place(relx=0.55, rely=0.3)

frame_sha1 = Frame(root1)
frame_sha1.place(relx=0.7, rely=0.3)

frame_sha2 = Frame(root1)
frame_sha2.place(relx=0.85, rely=0.3)

frame_sha256 = Frame(root1)
frame_sha256.place(relx=0.55, rely=0.475)

frame_sha512 = Frame(root1)
frame_sha512.place(relx=0.7, rely=0.475)

frame_NTLM = Frame(root1)
frame_NTLM.place(relx=0.85, rely=0.475)

md5_in = StringVar()
sha1_in = StringVar()
sha2_in = StringVar()
sha256_in = StringVar()
sha512_in = StringVar()
NTLM_in = StringVar()


def md5_calc():
    txt = md5_in.get()
    res = hashlib.md5(txt.encode('utf8'))
    md5_txt_out.insert(0,res.hexdigest())

def md5_file_calc():
    inp_file = str(filedialog.askopenfile(initialdir="/Home"))
    BLOCK_SIZE = 65536
    inp_file=inp_file.split("'")[1]
    file_hash = hashlib.md5()
    with open(inp_file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    md5_txt_out.insert(0,file_hash.hexdigest())

md5 = Label( frame_md5, text = "MD5", font=("Arial",10, 'bold'))
md5_txt_label = Label(frame_md5, text = "Enter the text:", font=('calibre', 10))
md5_txt_entry = Entry(frame_md5, textvariable = md5_in, font=('calibre',10))
md5_txt_label2 = Label(frame_md5, text = "MD5 hash :", font=('calibre',10))
md5_file_but = Button(frame_md5, text = "Browse", command = md5_file_calc)
md5_txt_out = Entry(frame_md5, font=('calibre',10))
md5_sub = Button(frame_md5, text = 'Submit', command = md5_calc)

md5.grid(row=0, column=0, pady=10)
md5_txt_label.grid(row=1, column=0)
md5_txt_entry.grid(row=1, column=1, padx=10, pady=10)
md5_txt_label2.grid(row=2, column=0)
md5_txt_out.grid(row=2, column=1, padx=10)
md5_sub.grid(row=3, column=0, pady=10)
md5_file_but.grid(row=3, column=1, padx=10, pady=10)


def sha1_calc():
    txt = sha1_in.get()
    res = hashlib.sha1(txt.encode('utf8'))
    sha1_txt_out.insert(0,res.hexdigest())

def sha1_file_calc():
    inp_file = str(filedialog.askopenfile(initialdir="/Home"))
    BLOCK_SIZE = 65536
    inp_file=inp_file.split("'")[1]
    file_hash = hashlib.sha1()
    with open(inp_file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    sha1_txt_out.insert(0,file_hash.hexdigest())

sha1 = Label( frame_sha1, text = "SHA1", font=("Arial",10, 'bold'))
sha1_txt_label = Label(frame_sha1, text = "Enter the text:", font=('calibre', 10))
sha1_txt_entry = Entry(frame_sha1, textvariable = sha1_in, font=('calibre',10))
sha1_txt_label2 = Label(frame_sha1, text = "SHA1 hash :", font=('calibre',10))
sha1_txt_out = Entry(frame_sha1, font=('calibre',10))
sha1_file_but = Button(frame_sha1, text = "Browse", command = sha1_file_calc)
sha1_sub = Button(frame_sha1, text = 'Submit', command = sha1_calc)

sha1.grid(row=0, column=0, pady=10)
sha1_txt_label.grid(row=1, column=0)
sha1_txt_entry.grid(row=1, column=1, padx=10, pady=10)
sha1_txt_label2.grid(row=2, column=0)
sha1_txt_out.grid(row=2, column=1, padx=10)
sha1_sub.grid(row=3, column=0, pady=10)
sha1_file_but.grid(row=3, column=1, padx=10, pady=10)


def sha2_calc():
    txt = sha2_in.get()
    res = hashlib.sha224(txt.encode('utf8'))
    sha2_txt_out.insert(0,res.hexdigest())

def sha2_file_calc():
    inp_file = str(filedialog.askopenfile(initialdir="/Home"))
    BLOCK_SIZE = 65536
    inp_file=inp_file.split("'")[1]
    file_hash = hashlib.sha224()
    with open(inp_file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    sha2_txt_out.insert(0,file_hash.hexdigest())

sha2 = Label( frame_sha2, text = "SHA224", font=("Arial",10, 'bold'))
sha2_txt_label = Label(frame_sha2, text = "Enter the text:", font=('calibre', 10))
sha2_txt_entry = Entry(frame_sha2, textvariable = sha2_in, font=('calibre',10))
sha2_txt_label2 = Label(frame_sha2, text = "SHA224 hash :", font=('calibre',10))
sha2_txt_out = Entry(frame_sha2, font=('calibre',10))
sha2_file_but = Button(frame_sha2, text = "Browse", command = sha2_file_calc)
sha2_sub = Button(frame_sha2, text = 'Submit', command = sha2_calc)

sha2.grid(row=0, column=0, pady=10)
sha2_txt_label.grid(row=1, column=0)
sha2_txt_entry.grid(row=1, column=1, padx=10, pady=10)
sha2_txt_label2.grid(row=2, column=0)
sha2_txt_out.grid(row=2, column=1, padx=10)
sha2_sub.grid(row=3, column=0, pady=10)
sha2_file_but.grid(row=3, column=1, padx=10, pady=10)


def sha256_calc():
    txt = sha256_in.get()
    res = hashlib.sha256(txt.encode('utf8'))
    sha256_txt_out.insert(0,res.hexdigest())

def sha256_file_calc():
    inp_file = str(filedialog.askopenfile(initialdir="/Home"))
    BLOCK_SIZE = 65536
    inp_file=inp_file.split("'")[1]
    file_hash = hashlib.sha256()
    with open(inp_file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    sha256_txt_out.insert(0,file_hash.hexdigest())

sha256 = Label( frame_sha256, text = "SHA256", font=("Arial",10, 'bold'))
sha256_txt_label = Label(frame_sha256, text = "Enter the text:", font=('calibre', 10))
sha256_txt_entry = Entry(frame_sha256, textvariable = sha256_in, font=('calibre',10))
sha256_txt_label2 = Label(frame_sha256, text = "SHA256 hash :", font=('calibre',10))
sha256_txt_out = Entry(frame_sha256, font=('calibre',10))
sha256_file_but = Button(frame_sha256, text = "Browse", command = sha256_file_calc)
sha256_sub = Button(frame_sha256, text = 'Submit', command = sha256_calc)

sha256.grid(row=0, column=0, pady=10)
sha256_txt_label.grid(row=1, column=0)
sha256_txt_entry.grid(row=1, column=1, padx=10, pady=10)
sha256_txt_label2.grid(row=2, column=0)
sha256_txt_out.grid(row=2, column=1, padx=10)
sha256_sub.grid(row=3, column=0, pady=10)
sha256_file_but.grid(row=3, column=1, padx=10, pady=10)


def sha512_calc():
    txt = sha512_in.get()
    res = hashlib.sha512(txt.encode('utf8'))
    sha512_txt_out.insert(0,res.hexdigest())

def sha512_file_calc():
    inp_file = str(filedialog.askopenfile(initialdir="/Home"))
    BLOCK_SIZE = 65536
    inp_file=inp_file.split("'")[1]
    file_hash = hashlib.sha512()
    with open(inp_file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    sha1_txt_out.insert(0,file_hash.hexdigest())
    
sha512 = Label( frame_sha512, text = "SHA512", font=("Arial",10, 'bold'))
sha512_txt_label = Label(frame_sha512, text = "Enter the text:", font=('calibre', 10))
sha512_txt_entry = Entry(frame_sha512, textvariable = sha512_in, font=('calibre',10))
sha512_txt_label2 = Label(frame_sha512, text = "SHA512 hash :", font=('calibre',10))
sha512_txt_out = Entry(frame_sha512, font=('calibre',10))
sha512_file_but = Button(frame_sha512, text = "Browse", command = sha512_file_calc)
sha512_sub = Button(frame_sha512, text = 'Submit', command = sha512_calc)

sha512.grid(row=0, column=0, pady=10)
sha512_txt_label.grid(row=1, column=0)
sha512_txt_entry.grid(row=1, column=1, padx=10, pady=10)
sha512_txt_label2.grid(row=2, column=0)
sha512_txt_out.grid(row=2, column=1, padx=10)
sha512_sub.grid(row=3, column=0, pady=10)
sha512_file_but.grid(row=3, column=1, padx=10, pady=10)


def NTLM_calc():
    txt = NTLM_in.get()
    res = hashlib.new('md4', txt.encode('utf8'))
    NTLM_txt_out.insert(0,res.hexdigest())

NTLM = Label( frame_NTLM, text = "NTLM", font=("Arial",10, 'bold'))
NTLM_txt_label = Label(frame_NTLM, text = "Enter the text:", font=('calibre', 10))
NTLM_txt_entry = Entry(frame_NTLM, textvariable = NTLM_in, font=('calibre',10))
NTLM_txt_label2 = Label(frame_NTLM, text = "NTLM hash :", font=('calibre',10))
NTLM_txt_out = Entry(frame_NTLM, font=('calibre',10))
NTLM_sub = Button(frame_NTLM, text = 'Submit', command = NTLM_calc)

NTLM.grid(row=0, column=0, pady=10)
NTLM_txt_label.grid(row=1, column=0)
NTLM_txt_entry.grid(row=1, column=1, padx=10, pady=10)
NTLM_txt_label2.grid(row=2, column=0)
NTLM_txt_out.grid(row=2, column=1, padx=10)
NTLM_sub.grid(row=3, column=0, pady=10)


root1.mainloop()