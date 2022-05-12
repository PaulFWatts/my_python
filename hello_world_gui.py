'''
Title: Process Button Event
Purpose: To demonstrate the processing of button events with functions
in a class
'''

from tkinter import *

class HelloWorldGUI:
    
    def __init__(self):
        window = Tk() # Create a window  

        self.btOK = Button(window, text="OK", highlightbackground="green", fg="red", command = self.SayHello)   

        self.lb = Label(window, text="Hello World")  

        self.btOK.pack() 
        self.lb.pack()
        
        window.mainloop() # Start the GUI event loop
        
    def SayHello(self):
        self.lb.config(text="Hello World")
    
    
myGUI = HelloWorldGUI()
