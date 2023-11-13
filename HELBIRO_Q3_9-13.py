import turtle

wn = turtle.Screen()

t = turtle.Turtle()

y1 = 50
y2 = 50
for i in range(2):
    t.up()
    t.setpos(-50, y1)
    t.down()
    t.circle(100, extent=None, steps=6)
    y1 -= 100

for i in range(2):
    t.up()
    t.setpos(50, y2)
    t.down()
    t.circle(50, extent=None, steps=6)
    y2 -= 100

def buttonClick(x, y):
    print(f"Coordinate ({x}, {y})")

wn.onscreenclick(buttonClick, 1)

turtle.done()