# 海龟作图实现分型树
import turtle

t = turtle.Turtle()

def drawSpiral(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen-5)

# drawSpiral(t, 100)

# turtle.done()
        
def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len * 0.75)
        t.left(40)
        tree(branch_len * 0.75)
        t.right(20)
        t.backward(branch_len)

t.left(90)
t.up()
t.backward(100)
t.down()
t.color('green')
tree(75)
t.hideturtle()
t.done()