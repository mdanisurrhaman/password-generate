from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_chracters=string.punctuation

    all1=small_alphabets+capital_alphabets+numbers+special_chracters


    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all1,password_length))

##    password=random.sample(all1,password_length)
##    passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

    
root=Tk()
root.config(bg="gray20")

choice=IntVar()
##Font=("arial",20,"bold")

passwordLabel=Label(root,text="Password Generate",font=('times new romans',40,'bold'),bg="gray20",fg="white")
passwordLabel.grid()

weakradioButton=Radiobutton(root,text="weak",value=1,variable=choice,font=("arial",20,"bold"))
weakradioButton.grid(pady=10)

mediumradioButton=Radiobutton(root,text="Medium",value=2,variable=choice,font=("arial",20,"bold"))
mediumradioButton.grid(pady=10)

strongradioButton=Radiobutton(text="Strong",value=3,variable=choice,font=("arial",20,"bold"))
strongradioButton.grid(pady=10)

lengthLabel=Label(root,text="Password Length",font=("arial",20,"bold"),bg="gray20",fg='white')
lengthLabel.grid()

length_Box=Spinbox(root,from_=4,to_=18,width=5,font=("arial",20,"bold"))
length_Box.grid()

generateButton=Button(root,text="Generate",font=("arial",20,"bold"),command=generator)
generateButton.grid(pady=10)

passwordField=Entry(root,width=25,bd=2,font=("arial",20,"bold"))
passwordField.grid()

copyButton=Button(root,text="Copy",font=("arial",20,"bold"),command=copy)
copyButton.grid(pady=10)





root.mainloop()
