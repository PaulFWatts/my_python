'''
Title: Widgets Demo: Hello person
Week 11: Tutorial 10

'''

from tkinter import *

class HelloName:
    
    def __init__(self):
        window = Tk() # Create a window 
        window.title("Widgets Demo") # Set a title
        window.geometry("300x200") # Set the size
        
        self.lb = Label(window, text="Enter your name") # Create a label
        
        self.name = StringVar() # Create a string variable
        self.tb = Entry(window,textvariable=self.name) # Create a text box
        
        self.bt = Button(window, text="Get Name",command=self.sayHello) # Create a button
        
        self.ms = Message(window, text="It is a widget demo") # Create a message
        
        self.lb.grid(row=1, column=1) # Place the label
        self.tb.grid(row=1, column=2) # Place the text box
        self.bt.grid(row=1, column=3) # Place the button
        self.ms.grid(row=2, column=1,rowspan=1,columnspan=4) # Place the message
        
        window.mainloop() # Start the GUI event loop
    def sayHello(self):
        enteredName = self.name.get() # Get the name entered in the text box
        self.ms.config(text="Hello " + enteredName) # Set the message to say hello       
    
myGUI = HelloName()
