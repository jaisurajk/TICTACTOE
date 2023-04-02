import turtle
def SetTurtle():
    s = turtle.Screen()
    s.bgcolor("white")
    s.setup(1000, 1000)
    s.title("Tree Program")
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    return t, s

def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=100)
    return t
def draw_tree(t, branch, angle, n):
    if n > 0: 
        t.color('brown')
        t.forward(branch)
        t.right(1.25*angle)
        draw_tree(t, branch*0.9, angle, n - 1)
        t.left(2.5*angle)
        draw_tree(t, branch*0.9, angle, n - 1)
        t.right(1.25*angle)
        t.backward(branch)
    else: 
        t.pendown()
        t.dot(10)


