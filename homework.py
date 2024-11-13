from tkinter import *
top=Tk()
top.title("Best desserts")
top.geometry("300x150")
listbox=Listbox(top , height=8,width=20,bg="lightblue",activestyle="dotbox",font="TimesNewRoman",fg="black")

#Define a label for the list.
label = Label(top, text="DESSERT ITEMS")
listbox.insert(1, "Cake")
listbox.insert(2, "Chocolate")
listbox.insert(3, "Ice-cream")
listbox.insert(4, "Tiramisu")
listbox.insert(5, "Cupcake")

frame=Frame(top)
frame.pack()
w=Label(top, text='Types of desserts', font="40")
w.pack()

bottomframe = Frame(top)
bottomframe.pack(side=BOTTOM)

b1_button = Button(frame , text = "Cakes" , fg="purple" , bg="lightblue")
b1_button.pack(side=LEFT)

b2_button = Button(frame, text="Chocolate cake", fg="pink", bg="beige")
b2_button.pack(side=LEFT)

b3_button = Button(frame, text= "Vanilla cake", fg="blue",bg="orange")
b3_button.pack(side=LEFT)

b4_button = Button(bottomframe, text="Tiramisu", fg="black",bg="lightgreen")
b4_button.pack(side=BOTTOM)

b5_button = Button(bottomframe, text="cupcake", fg="red",bg="yellow")
b5_button.pack(side=BOTTOM)
b6_button = Button(bottomframe, text="icecream", fg="grey",bg="blue")
b6_button.pack(side=BOTTOM)

listbox.pack()
top.mainloop()