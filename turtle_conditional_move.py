import turtle
bob = turtle.Turtle()
edge_count = 0
while edge_count < 20:
    bob.forward(20)
    if (edge_count % 2 ==1):
        bob.left(90)
    else:
        bob.right(90)
    edge_count = edge_count + 1

turtle.done()