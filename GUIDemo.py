from tkinter import *
import os

root = Tk()

#Initialising images in Array
imageNames = ["australia1.gif", "agriculturalLand.gif", "artesianBasinMap.gif", "populationMap.gif","rainfallMap.gif", "riverMap.gif", "sunshineHoursMap.gif", "temperatureMap.gif"]
imageArray = []
for name in imageNames:
    imageArray.append(PhotoImage(file=name))

#Initialising text files
textFileNames = ["australia1.txt", "agriculturalLand.txt", "artesianBasinMap.txt", "populationMap.txt", "rainfallMap.txt","riverMap.txt","sunshineHoursMap.txt","temperatureMap.txt"]
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
    text.delete(1.0, END)
    text.insert(INSERT, words)


#image label
pic = imageArray[0]
myLabel = Label(root, compound = CENTER, image=pic)
myLabel.pack(side="right")


#slider
slider = Scale(root, from_=1, to=8,tickinterval=1, length = 500, orient=HORIZONTAL)
slider.set(1)
slider.pack()


#button
B = Button(root, text='Go to', command=get_year)
B.pack()

#text
text = Text(root, font=('Arial', 32), fg = 'dark blue', padx = 6, pady = 6, wrap = 'word', width = 20, height = 12)
text.insert(INSERT, textArray[0])
text.pack()

root.mainloop()
