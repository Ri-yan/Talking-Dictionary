from tkinter import *  # predefined clss

root = Tk()  # an object of tkinter for gui
root.geometry('1000x626+100+30')  # defining the height and width and fixing its x,y position
root.title('Taking Dictionary by Mohd Riyan')  # Giving title to program
root.resizable(False, False)  # disable the resizability of wondows

bgimage = PhotoImage(file='./assets/bg.png')  # an object is made with imported  asset
bgLable = Label(root, image=bgimage)  # object of lable
bgLable.place(x=0, y=0)  # placing bg from 0,0

enterwordlable = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
# label with object with text
# font should be passed as tuple foreground or fg is for font color with tkinter color
# bg or backgroung for background
enterwordlable.place(x=530, y=20)  # place for positioning the label

enterword=Entry(root, font=('arial', 23, 'bold'), justify=CENTER, bd=8, relief=GROOVE)
#justify for centering the cusor
#relief for border style
#bd for border
enterword.place(x=510, y=80)

searchimage = PhotoImage(file='./assets/search.png')  # from flaticon.com
searchButton = Button(root, image=searchimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke')
#Button class for button
searchButton.place(x=620, y=150)

micimage = PhotoImage(file='./assets/mic.png')
micButton = Button(root, image=micimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke')
micButton.place(x=700, y=153)

meaninglable = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')   # label objext with text
meaninglable.place(x=580, y=240)  # positioning the label

textarea=Text(root, width=34,height=8,font=('arial', 18, 'bold'),bd=8,relief=GROOVE)
textarea.place(x=460, y=300)

audioimage = PhotoImage(file='./assets/microphone.png')
audioButton = Button(root, image=micimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke')
audioButton.place(x=530, y=555)

clearimage = PhotoImage(file='./assets/clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke',cursor='hand2', activebackground='whitesmoke')
clearButton.place(x=660, y=555)

exitimage = PhotoImage(file='./assets/exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke')
exitButton.place(x=790, y=555)



root.mainloop()  # to hold window everything before mainloop will be in loop and nothing will execute after it
