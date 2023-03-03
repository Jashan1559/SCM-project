import requests,webbrowser
from bs4 import BeautifulSoup
from tkinter import  *
from PIL import ImageTk, Image
import os

structure=Tk() ##Making the container##
structure.geometry("1920x1080")
structure.title("The Cosgo Search Engine")
structure.config(background="teal")
## The position of the name of engine ##
# img = ImageTk.PhotoImage(Image.open("Galactic Wolf.png"))
# label=Label(structure,image=img)
# label.pack(side=TOP)
label=Label(structure,text="Cosgo Engine",bg='teal',fg="gold",font=("ComicSans",60,"italic"))
label.pack(side=TOP)
label.place(x=600,y=350)
text=StringVar()

def searches():
        data=requests.get('https://www.google.com/search?q='+text.get())
        soup=BeautifulSoup(data.content,"html.parser")
        result=soup.select(".kCrYT a")
        for ans in result[:6]:
                global search
                search=ans.get("href")
                search=search[7:]
                search=search.split("&")
                print(search)
                webbrowser.open(search[0])
searches()
# def op():
#         bro=webbrowser.open(a)
# op()
label=Label(structure,font=("Times",15,"bold"),text="Enter here to search",bg="teal",fg="dark green")
label.place(x=510,y=540)
enter=Entry(structure,font=("Times",15,"bold"),textvar=text,width=70,bd=2,bg="white")
enter.place(x=500,y=500)       #The input box#
button=Button(structure,text="Search",font=("Times",15,"bold"),width=10,bd=2,bg="white",command=searches)
button.place(x=1100,y=550)     # Click on the button to search #

# lab=Button(structure,font=("ComicSans",15,"bold"),text=f"Your results: {searches}",bg="dark green",fg="cyan",command=op)
# lab.place(x=515,y=580)

structure.mainloop()

