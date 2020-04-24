import turtle

wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor("lightgreen")
wn.title("Exercise 2: ")

a = turtle.Turtle()
a.color('violet')
a.width(3)
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)




draw_poly(a, 8, 50)

wn.mainloop()