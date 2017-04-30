from tkinter import *
import os

root = Tk()
root.wm_title("Terra Farmer")

#Initialising images in Array
mapImages= ["agriculturalLand.gif", "artesianBasinMap.gif", "populationMap.gif","rainfallMap.gif", "riverMap.gif", "sunshineHoursMap.gif", "temperatureMap.gif"]
mapArray = []
for name in mapImages:
    mapArray.append(PhotoImage(file=name))

#Initialising Map text files
mapText = ["agriculturalLand.txt", "artesianBasinMap.txt", "populationMap.txt", "rainfallMap.txt","riverMap.txt","sunshineHoursMap.txt","temperatureMap.txt"]
mtArray = []
for name in mapText:
    with open(name) as f:
    	mtArray.append(f.read())

#Initialising Projection images in an Array
projImages = ["australia1.gif", "australia2.gif", "australia3.gif", "australia4.gif"]
projArray = []
for name in projImages:
    projArray.append(PhotoImage(file=name))

#Intialising Projection Text Files
projText = ["a1.txt", "a2.txt", "a3.txt", "a4.txt"]
ptArray = []
for name in projText:
    with open(name) as p:
        ptArray.append(p.read())

#Changing Projection Image
def set_year(new_value):
    new_value = int(new_value)
    global pic, myLabel, text
    pic = None
    pic = projArray[new_value - 1]

    myLabel.configure(image = pic)
    myLabel.image = pic

    words = ptArray[new_value - 1]
    text.delete(1.0, END)
    text.insert(INSERT, words)

#Change map and relevant analysis
def radio_btns():
    rVal = int(var.get())
    
    pic = None
    pic = mapArray[rVal-1]
    
    myLabel.configure(image=pic)
    myLabel.image = pic
    
    words = mtArray[rVal - 1]
    text.delete(1.0, END)
    text.insert(INSERT, words)

var = IntVar()
#Make Radio buttons to change selection of what information is being looked at
R1 = Radiobutton(root, text = "Agricultural Land Map", variable = var, value = 1, command = radio_btns)
R1.pack(anchor = W)
R2 = Radiobutton(root, text = "Artesian Basin Map", variable = var, value = 2, command = radio_btns)
R2.pack(anchor = W)
R3 = Radiobutton(root, text = "Population Map", variable = var, value = 3, command = radio_btns)
R3.pack(anchor = W)
R4 = Radiobutton(root, text = "Rainfall Map", variable = var, value = 4, command = radio_btns)
R4.pack(anchor = W)
R5 = Radiobutton(root, text = "River Map", variable = var, value = 5, command = radio_btns)
R5.pack(anchor = W)
R6 = Radiobutton(root, text = "Sunshine Hours Map", variable = var, value = 6, command = radio_btns)
R6.pack(anchor = W)
R7 = Radiobutton(root, text = "Temperature Map", variable = var, value = 7, command = radio_btns)
R7.pack(anchor = W)

#image label
pic = projArray[0]
myLabel = Label(root, compound = CENTER, image=pic)
myLabel.pack(side="right")


#slider
slider = Scale(root, from_=1, to=4,tickinterval=1, length = 500, orient=HORIZONTAL, command=set_year)
slider.set(1)
slider.pack()

#text
text = Text(root, font=('Arial', 32), fg = 'dark blue', padx = 6, pady = 6, wrap = 'word', width = 20, height = 12)
text.insert(INSERT, ptArray[0])
text.pack()

root.mainloop()
