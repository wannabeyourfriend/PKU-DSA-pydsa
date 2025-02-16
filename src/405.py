# 海龟作图实现谢尔斯宾三角形
import turtle as t
def sierpinski(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree-1, {'left': points['left'],
                              'top': getMid(points['left'], points['top']),
                              'right': getMid(points['left'], points['right'])})
        sierpinski(degree-1, {'left': getMid(points['left'], points['top']),
                              'top': points['top'],
                              'right': getMid(points['top'], points['right'])})
        sierpinski(degree-1, {'left': getMid(points['left'], points['right']),
                              'top': getMid(points['top'], points['right']),
                              'right': points['right']})
        
def drawTriangle(points, color):
    t.fillcolor(color)
    t.up()
    t.goto(points['top'])
    t.down()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def getMid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def main():
    t.setup(800, 800)
    points = {'left': (-200, -100),
              'top': (0, 200),
              'right': (200, -100)}
    sierpinski(6, points)
    t.hideturtle()
    t.done()

main()