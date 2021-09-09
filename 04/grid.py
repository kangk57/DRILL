import turtle

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

a = 0
while (a < 5):
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500-a*100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500-a*100)
    turtle.left(90)
    a += 1

b = 0
while (b < 5):
    turtle.forward(500-b*100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500-b*100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    b += 1
    
turtle.exitonclick()
