import turtle

def draw_square(t, sz):
    t.color('violet')
    t.width(3)
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor("lightgreen")
wn.title("Exercise 1: ")

a = turtle.Turtle()

for j in range(6):
    if j == 1:
        draw_square(a, 20)
    else:
        a.penup()
        a.left(180)
        a.forward(10)
        a.left(90)
        a.forward(10)
        a.left(90)
        a.pendown()
        draw_square(a, 20*j)

wn.mainloop()