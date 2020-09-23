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
    col = ["green", "red", "blue", "orange", "yellow"] 
    
    def __init__ (self, x, y, radious, canvas, vx = 1, vy = 1, color = "undefined") :
        
        if color == "undefined" :
            color = random.choices(self.col, k=1)
            #l1.config(text="red")
        self.color = color
        self.radious = radious
        self.vy = vy
        self.vx = vx
        self.x = x
        self.y = y
        self.canvas = canvas
        self.image = canvas.create_oval(x - radious, y - radious, x + radious, y + radious, outline = 'black', fill = color)
        #self.l1 = Label(text = "")
        #self.l1.pack()
    def move(self):
        self.canvas.move(self.image, self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        
        self.check_boundaries()

    def check_boundaries(self):
        col = self.col 
        if self.y - 10 - self.radious <= 0 :
            self.vy = -self.vy
            #self.change_color(random.choices(col, k=1))
            #self.change_size(random.randint(10, 50))
            
        if 490 - self.y - self.radious <= 0 :
            self.vy = -self.vy
            #self.change_color(random.choices(col, k=1))
            #self.change_size(random.randint(10, 50))
            
        if 490 - self.x - self.radious <= 0 :
            self.vx = -self.vx
            #self.change_color(random.choices(col, k=1))
            #self.change_size(random.randint(10, 50))
            
        if self.x - 10 - self.radious <= 0 :
            self.vx = -self.vx
            #self.change_color(random.choices(col, k=1))
            #self.change_size(random.randint(10, 50))
                       

    def change_color(self, color):
        self.color = color
        #self.image = self.canvas.create_oval(self.x - self.radious, self.y - self.radious, self.x + self.radious, self.y + self.radious, outline = 'black', fill = color)
        self.canvas.itemconfig(self.image, fill = color)
        #self.l1.config(text = balls[-1].color)
        
        
    def change_size(self, radious):
        size = self.radious
        self.canvas.coords(self.image, self.x - radious, self.y - radious, self.x + radious, self.y + radious)
        self.radious = radious
        dif = self.radious - size
        if self.y - 10 - self.radious <= 0 :
            self.canvas.move(self.image, 0, dif)
            self.y += dif
    
        if 490 - self.y - self.radious <= 0 :
            self.canvas.move(self.image, 0, -dif)
            self.y -= dif
            
        if 490 - self.x - self.radious <= 0 :
            self.canvas.move(self.image, -dif, 0)
            self.x -= dif
            
        if self.x - 10 - self.radious <= 0 :
            self.canvas.move(self.image, dif, 0)
            self.x += dif
            
class colorButton(Button):
    def __init__(self, parent, lbox, rbutton):
        Button.__init__(self, parent)
        self['text'] = 'change color'
        self.place(x = 400, y = 0)
        self.lbox = lbox
        self.rbutton = rbutton
        self['command'] = self.change
   
    def change(self) :
        current_ball = self.lbox.dictballs[self.lbox.get(ACTIVE)]
        color = self.rbutton.r_var.get()
        #i = self.lbox.balls.index(current_ball)
        #self.lbox.canvas.delete(self.lbox.balls[i].image)
        #self.lbox.balls[i].image = current_ball.canvas.create_oval(current_ball.x - current_ball.radious, current_ball.y - current_ball.radious, current_ball.x + current_ball.radious, current_ball.y + current_ball.radious, outline = 'black', fill = color)
        current_ball.change_color(color)
        
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Закрыть'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.place(x = 250, y = 0) 


class addButton(Button):
    def __init__(self, parent, canvas, balls):
        Button.__init__(self, parent)
        
        self['text'] = 'add ball'
        self.canvas = canvas
        self.balls = balls
        self['command'] = self.add_balls
        self.place(x = 30, y = 0)
        self.lbox = listballs(parent, canvas, balls)

    def add_balls(self) :
        Ball = ball(random.randint(40, 460), random.randint(40, 460), random.randint(10, 30), self.canvas, random.randint(-10, 10), random.randint(-10, 10))
        self.balls.append(Ball)
        self.lbox.dictballs['Ball_' + str(len(self.balls)-1)] = Ball
        self.lbox.insert("end", 'Ball_' + str(len(self.balls)-1))
        self.lbox.label["text"] = "Number of balls : " + str(len(self.lbox.dictballs)) 
        
#class change_label():
class speed_scal(Scale) :
    def __init__(self, parent, lbox) :
        Scale.__init__(self, parent) 
        
        self["from_"] = 10 
        self["to"] = 50
        self.size_var = IntVar()
        self.size_var.set(30)
        self["variable"] = self.size_var
        self.pack()
        self.button = Button(text = "change", width = 10, height = 2, command = self.resize)  
        self.button.pack()
        self.lbox = lbox
    def resize(self) :
        size = self.size_var.get()
        ball = self.lbox.dictballs[self.lbox.get(ACTIVE)]
        ball.change_size(size)
    

class color_radiobox(Radiobutton) :
    def __init__(self, parent) :
        self.r_var = StringVar()
        self.r_var.set("cyan")
        self.r1 = Radiobutton(text='Black', width=10, height=1, variable=self.r_var, value="black")
        self.r2 = Radiobutton(text='Purple', width=10, height=1, variable=self.r_var, value="purple")
        self.r3 = Radiobutton(text='Cyan', width=10, height=1, variable=self.r_var, value="cyan")
        self.r1.pack(anchor=S)
        self.r2.pack(anchor=S)
        self.r3.pack(anchor=S)
        
class listballs(Listbox) :
    dictballs = {}    
    def __init__(self, parent, canvas, balls) :
        Listbox.__init__(self, parent)
        for i, ball in enumerate(balls) :
            self.dictballs['Ball_'+str(i)] = ball
       
        self["width"] = 50
        self['height'] = 20
        self.canvas = canvas
        self.balls = balls
        self.pack(side = RIGHT)
        self.label = Label(text = "Number of balls : " + str(len(self.dictballs)))
        self.label.pack(side = LEFT)
        for e in self.dictballs :
            self.insert("end", e)
    def remove_ball(self) :
        current = self.get(ACTIVE)
        self.canvas.delete(self.dictballs[current].image)
        self.delete(ANCHOR)
        del self.dictballs[current]
        self.label["text"] = "Number of balls : " + str(len(self.dictballs)) 
       
root = Tk()
b2 = quitButton(root)
w = Canvas(root, width=600, height=600)
w.pack(side = LEFT)
w.create_rectangle(10, 10, 490, 490, outline = "red", width = 5)
#l1 = Label()
ball1 = ball(50, 50, 15, w, 10, 15)
ball2 = ball(70, 70, 10, w, -15, -15)
balls = [ball1, ball2]
root.update()
#b1 = Button(text="Изменить", width=15, height=3, command = add_balls(w, balls))
b1 = addButton(root, w, balls)
b1.lbox.bind('<Double-1>', lambda x : b1.lbox.remove_ball())
s = speed_scal(root, b1.lbox)
r1 = color_radiobox(root)
#l1 = Label(text = balls[-1].color)
#l1.pack()
b3 = colorButton(root, b1.lbox, r1)

def motion() :
     for e in balls :
        e.move()
     root.after(50, motion)

    
motion()
           


       
   
    

root.mainloop()

 
