import turtle
import math
def star(size, n, d=2):
    t.pendown()
    if n%2==1:
        for i in range(n):
            t.forward(size)
            if n == 5:
                t.right(360*d/n)
            elif 11>n>=7:
                t.right(720*d/n)
            else:
                t.right(1080*d/n)
            t.forward(2*size)
    else:
        for j in range(d):
            t.pendown()
            for i in range(n // d):
                t.right(360*(d-1)/n)
                t.forward(size)
                t.right(360*(d-1)/n)
            t.penup()
            t.circle(-size/(2 * math.sin((math.pi/(n // d)))), 360/n)    
      
def star_recursive(size, n, alpha, d=2):
    if alpha>0: 
        t.forward(size)
        t.right(d*360/n)
        star_recursive(size, n, alpha-1, d)  
