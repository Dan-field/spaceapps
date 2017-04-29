from Tkinter import *
import os

root = Tk()

#Initialising images in Array
imageNames = ["australia1.gif", "australia2.gif", "australia3.gif", "australia4.gif"]
imageArray = []
for name in imageNames:
    imageArray.append(PhotoImage(file=name))

#Initialising text files
textFileNames = ["a1.txt", "a2.txt", "a3.txt", "a4.txt"]
textArray = []
for name in textFileNames:
    with open(name) as f:
    	textArray.append(f.read())


#update image label
def get_year():
    sliderVal = slider.get()

    pic = None
    pic = imageArray[sliderVal - 1]

    myLabel.configure(image = pic)
    myLabel.image = pic

    words = textArray[sliderVal - 1]
    text.insert(INSERT, words)


#image label
pic = imageArray[0]
myLabel = Label(root, compound = CENTER, image=pic)
myLabel.pack(side="right")
#myLabel2 = Label(root, text =  )


#slider
slider = Scale(root, from_=1, to=4,tickinterval=1, length = 500, orient=HORIZONTAL)
slider.set(1)
slider.pack()


#button
B = Button(root, text='Go to', command=get_year)
B.pack()

#text
text = Text(root, font=('Arial', 32), fg = 'dark blue', padx = 6, pady = 6)
text.insert(INSERT, textArray[0])
text.pack()

root.mainloop()
