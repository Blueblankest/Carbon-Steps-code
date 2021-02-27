import tkinter
#setting up the grid
master=tkinter.Tk()
master.title("place() method")
master.geometry("100x100")




button1=tkinter.Button(master, text="+1")
button1.place(x=25, y=25)

button2=tkinter.Button(master, text="-1")
button2.place(x=25, y=60)




master.mainloop()


