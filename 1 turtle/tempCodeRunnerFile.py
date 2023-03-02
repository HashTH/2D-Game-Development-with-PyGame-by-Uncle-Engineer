    tao.begin_fill()    
        tao.fillcolor(col[i])
        tao.circle(10*i,20*i)
        tao.forward(200)
        tao.left(170)
        if abs(turtle.pos()) < 1:
            break
        tao.end_fill()