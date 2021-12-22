from tkinter import *
from PIL import Image,ImageTk
#main window

root = Tk()
root.title("rock paper scissor")
root.configure(background="#9b59b6")

# pictures

rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("comp_rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("comp_paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("comp_scissors.png"))

# insert picture

user_label =  Label(root,image=scissors_img, bg="#9b59b6")
comp_label =  Label(root,image=scissors_img_comp, bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


root.mainloop()
