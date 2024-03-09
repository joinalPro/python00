"""
result = 0
for num in range(5, 101, 5):
    print(num)
    result += num
print("Sum is: " result)
"""

import turtle
turtle.speed(1)

for i in range (20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()