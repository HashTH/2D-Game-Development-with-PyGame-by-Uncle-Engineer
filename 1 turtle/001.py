import turtle

def squares():
    for i in range(4):
        tao.forward(160)
        tao.left(100)

def walk(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

tao = turtle.Pen()
screen = turtle.Screen()
tao.shape('turtle')
tao.color('white','lightblue')
screen.bgcolor('black')

pen = ['white','green','yellow','lightblue','lightgreen','lightyellow'
       ,'white','green','yellow']
fill = ['lightblue','lightgreen','lightyellow','white','green','yellow'
        ,'lightblue','lightgreen','lightyellow']

for i in range(9):
    tao.pencolor(pen[i])
    tao.fillcolor(fill[i])
    tao.begin_fill()
    tao.circle(20)
    squares()
    walk(-1*i,-1*i)
    tao.end_fill()

turtle.done()