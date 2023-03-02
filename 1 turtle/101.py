from turtle import *
speed(0)
begin_fill()
while True:
    color('red','yellow')
    circle(10)    
    forward(200)
    color('pink','white')
    circle(20)
    left(170)
    circle(40)
    color('blue','purple')
    if abs(pos()) < 1:
        break
end_fill()
done()