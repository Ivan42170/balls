# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:20:03 2020

@author: vptws
"""


from tkinter import *
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
    col =  ["green", "red", "blue", "orange", "yellow"] 
    
    def __init__ (self, x, y, radious, canvas, vx = 1, vy = 1, color = "undefined") :
        
        if color == "undefined" :
            color = random.choices(self.col, k=1)
         
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
        col =  ["green", "red", "blue", "orange", "yellow"]
        if self.y - 10 - self.radious <= 0 :
            self.vy = -self.vy
            self.change_color(random.choices(col, k=1))
            self.change_size(random.randint(10, 50))
        #if self.change_size >= 35 :
            
            
           
        if 490 - self.y - self.radious <= 0 :
            self.vy = -self.vy
            self.change_color(random.choices(col, k=1))
            
        if 490 - self.x - self.radious <= 0 :
            self.vx = -self.vx
            self.change_color(random.choices(col, k=1))
            
        if self.x - 10 - self.radious <= 0 :
            self.vx = -self.vx
            self.change_color(random.choices(col, k=1))
            

    def change_color(self, color):
        self.color = color
        #self.image = self.canvas.create_oval(self.x - self.radious, self.y - self.radious, self.x + self.radious, self.y + self.radious, outline = 'black', fill = color)
        self.canvas.itemconfig(self.image, fill = color)

    def change_size(self, radious):
        self.canvas.coords(self.image, self.x - radious, self.y - radious, self.x + radious, self.y + radious)
        self.radious = radious         
        
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Закрыть'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side = RIGHT)



class addButton(Button):
    def __init__(self, parent, canvas, balls):
        Button.__init__(self, parent)
        self['text'] = 'Добавить'
        self.canvas = canvas
        self.balls = balls
        self['command'] = self.add_balls
        self.pack(side = BOTTOM)

    def add_balls(self) :
        Ball = ball(random.randint(40, 460), random.randint(40, 460), random.randint(10, 30), self.canvas, random.randint(-10, 10), random.randint(-10, 10))
        self.balls.append(Ball)

def main():
    
    root = Tk()
    b2 = quitButton(root)
    w = Canvas(root, width=600, height=600)
    w.pack()
    w.create_rectangle(10, 10, 490, 490, outline = "red", width = 5)
    
    ball1 = ball(50, 50, 15, w, 15, 10)
    ball2 = ball(70, 70, 10, w, 10, 20)
    balls = [ball1, ball2]
    root.update()
    #b1 = Button(text="Изменить", width=15, height=3, command = add_balls(w, balls))
    b1 = addButton(root, w, balls)
   
    while True:
        for e in balls :
            e.move()

    
           
       
        root.update()

    root.mainloop()
    
 
if __name__ == '__main__':
    main()