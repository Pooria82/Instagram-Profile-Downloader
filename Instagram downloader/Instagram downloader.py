from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image , ImageTk
import io

def get_image():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context , f"{username.get()}")
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image = pic
    label.pack()

window = Tk()
window.geometry("600x600")
window.maxsize(800 ,800)
window.minsize(400 , 400)

window.title('Instagram Profile Downloader')

#label 1:
Label(window , text= 'Enter your instagram username' , bg='orange').pack()

#Inputs:
username = Entry(window , width=50)
username.pack()

#Button:
button = Button(window , text="Start Download" , fg= 'green' , bg= 'light blue' , )
# button.place(x=195 , y=50)
button.pack()
button.config(command=get_image)

#label 2:
label = Label(window)

window.mainloop()

#pyinstaller --onefile -w '.\<file name>'  <== گرفتن exe برای خروجی به صورت





