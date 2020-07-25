# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:20:03 2020

@author: vptws
"""


from tkinter import Tk, Canvas, Frame, BOTH, PhotoImage
import time, math, random

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Lines")        
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)
        

class ball():
    def __init__ (self, color, x, y, radious, canvas, vx = 1, vy = 1) :
        self.color = color
        self.radious = radious
        self.vy = vy
        self.vx = vx
        self.x = x
        self.y = y
        self.canvas = canvas
        self.image = canvas.create_oval(x - radious, y - radious, x + radious, y + radious, outline = 'black', fill = color)
    
    def move(self):
        self.canvas.move(self.image, self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        time.sleep(0.1)
        self.check_boundaries()

    def check_boundaries(self):
        if self.y - 10 - self.radious <= 0 :
            self.vy = -self.vy
            self.change_color("green")
        if 490 - self.y - self.radious <= 0 :
            self.vy = -self.vy
        if 490 - self.x - self.radious <= 0 :
            self.vx = -self.vx
        if self.x - 10 - self.radious <= 0 :
            self.vx = -self.vx 

    def change_color(self, color):
        pass

    def change_size(self, radious):
        pass

            
        
 
 
def main():
    root = Tk()
    w = Canvas(root, width=600, height=600)
    w.pack()
    w.create_rectangle(10, 10, 490, 490, outline = "red", width = 5)
    ball1 = ball("orange", 50, 50, 15, w, 3, 4)
    ball2 = ball("red", 70, 70, 10, w, 20, 25)
    root.update()
    
    while True: 
       
        ball1.move()
        ball2.move()
        root.update()

    root.mainloop()
    
 
if __name__ == '__main__':
    main()