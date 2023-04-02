import turtle
def polygon(length, n):
    t.pendown()
    for i in range(n): 
        t.forward(length)
        t.right(360/n)
    t.penup()
def polygon_recursive(length, n, level):
    if level<1:
        return None
    else:
        t.pendown()
        t.forward(length)
        t.right(360/n)
        polygon_recursive(length, n, level-1)
