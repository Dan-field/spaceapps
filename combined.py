from Tkinter import *

root = Tk()

#update image label
def get_year():
    sliderVal = slider.get()
    pic = imageArray[sliderVal-1]

    myLabel.configure(image = pic)
    myLabel.image = pic

#array of images
imageNames = ['australia1.gif', 'australia2.gif', 'australia3.gif', 'australia4.gif']
imageArray = []
for name in imageNames:
    imageArray.append(PhotoImage(file=name))

#image label
pic = imageArray[0]
myLabel = Label(root, compound = CENTER, image=pic)
myLabel.pack(side="right")


#slider
slider = Scale(root, from_=1, to=4,tickinterval=1, length = 500, orient=HORIZONTAL)
slider.set(1)
slider.pack()


#button
B = Button(root, text='Go to', command=get_year)
B.pack()



root.mainloop()

