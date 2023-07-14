import PIL.Image as IMG
from tkinter import *
from tkinter import filedialog
import math
import re
import os

root1 = Tk()
root1.state("zoomed")
bg = PhotoImage( file = "bg.png")
logo = PhotoImage( file = "logo.png")

label1 = Label( root1, image=bg)
label1.place(x = 0,y = 0)

labellogo = Label( root1, image = logo)
labellogo.place(in_=label1, relx = 0.70, rely = 0.02)

labelinfo = Label( root1, text="Done by: \n Kethamreddy Karthikeya Reddy \n CH.EN.U4CYS20038 \n Amrita School Of Computing")
labelinfo.place(in_=label1, relx = 0.87, rely = 0.9)
label2 = Label( root1, text = "AVV CYS Tools: ", font =("Arial", 50))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)

p1_pt = StringVar()
p1_key = StringVar()
p2_key = StringVar()
p2_ct = StringVar()
p3_pt = StringVar()
p3_key = StringVar()
p4_ct = StringVar()
p4_key = StringVar()
p5_pt = StringVar()
p5_key = StringVar()
p6_ct = StringVar()
p6_key = StringVar()

def col_encrypt():
    msg = p1_pt.get().upper()
    key = p1_key.get()
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
    lab1_p1_ct_txt.insert(0, cipher)
    
def col_decrypt():
    cipher = p2_ct.get().upper()
    key = p2_key.get()
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    msg = ''.join(sum(dec_cipher, []))
    null_count = msg.count('_')
    if null_count > 0:
        lab1_p2_pt_txt.insert(0, msg[: -null_count])
    else:
        lab1_p2_pt_txt.insert(0, msg)


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def vig_encrypt():
    string = p3_pt.get().upper()
    key = generateKey(string,p3_key.get().upper())
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    lab1_p3_ct_txt.insert(0,"" . join(cipher_text))

def vig_decrypt():
    cipher_text = p4_ct.get().upper()
    key = generateKey(cipher_text, p4_key.get().upper())
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    lab1_p4_pt_txt.insert(0,"" . join(orig_text))

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m

def affine_encrypt():
    key = p5_key.get()
    text = p5_pt.get().upper()
    key = list(key.split(','))
    key = [eval(i) for i in key]
    lab1_p5_ct_txt.insert(0,''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]))
 

def affine_decrypt():
    key = p6_key.get()
    cipher = p6_ct.get().upper()
    key = list(key.split(','))
    key = [eval(i) for i in key]
    lab1_p5_pt_txt.insert(0,''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))% 26) + ord('A')) for c in cipher ]))

frame_p1 = Frame(root1)
frame_p1.place(relx=0.55, rely=0.3)

lab1_p1 = Label(frame_p1, text="Columnar Transposition \n Cipher encryption")
lab1_p1_pt = Label(frame_p1, text="Plain Text: ")
lab1_p1_pt_txt = Entry(frame_p1, textvariable = p1_pt)
lab1_p1_key = Label(frame_p1, text=" Key: ")
lab1_p1_key_txt = Entry(frame_p1, textvariable = p1_key)
lab1_p1_ct = Label(frame_p1, text="Cipher Text: ")
lab1_p1_ct_txt = Entry(frame_p1)
but_p1=Button(frame_p1, text="Encrypt", command=col_encrypt)

lab1_p1.grid(row=0, padx=5, pady=5)
lab1_p1_pt.grid(row=1, column=0, padx=5, pady=5)
lab1_p1_pt_txt.grid(row=1, column=1, padx=5, pady=5)
lab1_p1_key.grid(row=2, column=0, padx=5, pady=5)
lab1_p1_key_txt.grid(row=2, column=1, padx=5, pady=5)
lab1_p1_ct.grid(row=3, column=0, padx=5, pady=5)
lab1_p1_ct_txt.grid(row=3, column=1, padx=5, pady=5)
but_p1.grid(row=4, column=1, padx=5, pady=5)

frame_p2 = Frame(root1)
frame_p2.place(relx=0.75, rely=0.3)

lab1_p2 = Label(frame_p2, text="Columnar Transposition \n Cipher decryption")
lab1_p2_ct = Label(frame_p2, text="Cipher Text: ")
lab1_p2_ct_txt = Entry(frame_p2, textvariable = p2_ct)
lab1_p2_key = Label(frame_p2, text="Key: ")
lab1_p2_key_txt = Entry(frame_p2, textvariable = p2_key)
lab1_p2_pt = Label(frame_p2, text="plain Text: ")
lab1_p2_pt_txt = Entry(frame_p2)
but_p2=Button(frame_p2, text="Decrypt", command=col_decrypt)

lab1_p2.grid(row=0, padx=5, pady=5)
lab1_p2_ct.grid(row=1, column=0, padx=5, pady=5)
lab1_p2_ct_txt.grid(row=1, column=1, padx=5, pady=5)
lab1_p2_key.grid(row=2, column=0, padx=5, pady=5)
lab1_p2_key_txt.grid(row=2, column=1, padx=5, pady=5)
lab1_p2_pt.grid(row=3, column=0, padx=5, pady=5)
lab1_p2_pt_txt.grid(row=3, column=1, padx=5, pady=5)
but_p2.grid(row=4, column=1, padx=5, pady=5)

frame_p3 = Frame(root1)
frame_p3.place(relx=0.55, rely=0.5)

lab1_p3 = Label(frame_p3, text="Vigenere \n Cipher encryption")
lab1_p3_pt = Label(frame_p3, text="Plain Text: ")
lab1_p3_pt_txt = Entry(frame_p3, textvariable = p3_pt)
lab1_p3_key = Label(frame_p3, text=" Key: ")
lab1_p3_key_txt = Entry(frame_p3, textvariable = p3_key)
lab1_p3_ct = Label(frame_p3, text="Cipher Text: ")
lab1_p3_ct_txt = Entry(frame_p3)
but_p3=Button(frame_p3, text="Encrypt", command=vig_encrypt)

lab1_p3.grid(row=0, padx=5, pady=5)
lab1_p3_pt.grid(row=1, column=0, padx=15, pady=5)
lab1_p3_pt_txt.grid(row=1, column=1, padx=15, pady=5)
lab1_p3_key.grid(row=2, column=0, padx=15, pady=5)
lab1_p3_key_txt.grid(row=2, column=1, padx=15, pady=5)
lab1_p3_ct.grid(row=3, column=0, padx=15, pady=5)
lab1_p3_ct_txt.grid(row=3, column=1, padx=15, pady=5)
but_p3.grid(row=4, column=1, padx=15, pady=5)

frame_p4 = Frame(root1)
frame_p4.place(relx=0.75, rely=0.5)

lab1_p4 = Label(frame_p4, text="Vigenere \n Cipher decryption")
lab1_p4_ct = Label(frame_p4, text="Cipher Text: ")
lab1_p4_ct_txt = Entry(frame_p4, textvariable = p4_ct)
lab1_p4_key = Label(frame_p4, text="Key: ")
lab1_p4_key_txt = Entry(frame_p4, textvariable = p4_key)
lab1_p4_pt = Label(frame_p4, text="plain Text: ")
lab1_p4_pt_txt = Entry(frame_p4)
but_p4=Button(frame_p4, text="Decrypt", command=vig_decrypt)

lab1_p4.grid(row=0, padx=5, pady=5)
lab1_p4_ct.grid(row=1, column=0, padx=15, pady=5)
lab1_p4_ct_txt.grid(row=1, column=1, padx=15, pady=5)
lab1_p4_key.grid(row=2, column=0, padx=15, pady=5)
lab1_p4_key_txt.grid(row=2, column=1, padx=15, pady=5)
lab1_p4_pt.grid(row=3, column=0, padx=15, pady=5)
lab1_p4_pt_txt.grid(row=3, column=1, padx=15, pady=5)
but_p4.grid(row=4, column=1, padx=15, pady=5)

frame_p5 = Frame(root1)
frame_p5.place(relx=0.55, rely=0.7)

lab1_p5 = Label(frame_p5, text="Affine \n Cipher encryption")
lab1_p5_pt = Label(frame_p5, text="Plain Text: ")
lab1_p5_pt_txt = Entry(frame_p5, textvariable = p5_pt)
lab1_p5_key = Label(frame_p5, text=" Key: ")
lab1_p5_key_txt = Entry(frame_p5, textvariable = p5_key)
lab1_p5_ct = Label(frame_p5, text="Cipher Text: ")
lab1_p5_ct_txt = Entry(frame_p5)
but_p5=Button(frame_p5, text="Encrypt", command=affine_encrypt)

lab1_p5.grid(row=0, padx=5, pady=5)
lab1_p5_pt.grid(row=1, column=0, padx=15, pady=5)
lab1_p5_pt_txt.grid(row=1, column=1, padx=15, pady=5)
lab1_p5_key.grid(row=2, column=0, padx=15, pady=5)
lab1_p5_key_txt.grid(row=2, column=1, padx=15, pady=5)
lab1_p5_ct.grid(row=3, column=0, padx=15, pady=5)
lab1_p5_ct_txt.grid(row=3, column=1, padx=15, pady=5)
but_p5.grid(row=4, column=1, padx=15, pady=5)

frame_p6 = Frame(root1)
frame_p6.place(relx=0.75, rely=0.7)

lab1_p6 = Label(frame_p6, text="Affine \n Cipher decryption")
lab1_p6_ct = Label(frame_p6, text="Cipher Text: ")
lab1_p6_ct_txt = Entry(frame_p6, textvariable = p6_ct)
lab1_p6_key = Label(frame_p6, text="Key: ")
lab1_p6_key_txt = Entry(frame_p6, textvariable = p6_key)
lab1_p6_pt = Label(frame_p6, text="plain Text: ")
lab1_p6_pt_txt = Entry(frame_p6)
but_p6=Button(frame_p6, text="Decrypt", command=affine_decrypt)

lab1_p6.grid(row=0, padx=5, pady=5)
lab1_p6_ct.grid(row=1, column=0, padx=15, pady=5)
lab1_p6_ct_txt.grid(row=1, column=1, padx=15, pady=5)
lab1_p6_key.grid(row=2, column=0, padx=15, pady=5)
lab1_p6_key_txt.grid(row=2, column=1, padx=15, pady=5)
lab1_p6_pt.grid(row=3, column=0, padx=15, pady=5)
lab1_p6_pt_txt.grid(row=3, column=1, padx=15, pady=5)
but_p6.grid(row=4, column=1, padx=15, pady=5)

root1.mainloop()