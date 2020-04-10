from Tkinter import *
from PIL import Image, ImageTk
gui = Tk()
c = Canvas(gui, width=500, height=700, bg="white")
c.pack()
MyTjaLogo = ImageTk.PhotoImage(Image.open("mytja.png"))
c.create_image(20,20, anchor=NW, image=MyTjaLogo)
c.create_text(100, 300, text="Hello! I'm your voice assistant My!")
c.create_text(100, 320, text="I'm here to help! Just say 'Hey, My'")
mainloop()
