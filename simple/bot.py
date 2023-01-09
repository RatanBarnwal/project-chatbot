from tkinter import *
root=Tk()
def send():
    send="You -> "+e.get()
    txt.insert(END,"\n" + send)
    if(e.get()=="Hello"):
        txt.insert(END,"\n" + "Bot -> Hi")
    elif(e.get()=="Hi"):
        txt.insert(END,"\n" + "Bot -> Hello")
    elif(e.get()=="How are you ?"):
        txt.insert(END,"\n" + "Bot -> Fine and what about you?")
    elif(e.get()=="Fine"):
        txt.insert(END,"\n" + "Bot -> Nice to hear")
    elif(e.get()=="Who are you ?"):
        txt.insert(END,"\n" + "Bot -> I am Chat Bot at your service")
    elif(e.get()=="Who created you ?"):
        txt.insert(END,"\n" + "Bot -> Saurabh, Ratan and Anurag.")
    elif(e.get()=="In which language you are based on ?"):
        txt.insert(END,"\n" + "Bot -> Python")
    elif(e.get()=="For how many hours you are available ?"):
        txt.insert(END,"\n" + "Bot -> 24*7 ")
    elif(e.get()=="How many people can you speak to at once"):
        txt.insert(END,"\n" + "Bot -> Only 1 at a time ")
    elif(e.get()==" What is your date of birth ?"):
        txt.insert(END,"\n" + "Bot -> 15,November,2021")
    else:
        txt.insert(END,"\n"+"Bot -> Sorry I did'nt get you")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("ChatBot")
root.mainloop()