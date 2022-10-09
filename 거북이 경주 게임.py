import turtle
import random

screen = turtle.Screen()


t1 = turtle.Turtle()
t1.color("pink")
t1.shape("circle")
t1.shapesize(5)
t1.pensize(5)
t1.penup()
t1.goto(-300, 0)

t2 = turtle.Turtle()
t2.color("blue")
t2.shape("turtle")
t2.shapesize(3)
t2.pensize(3)
t2.penup()
t2.goto(-300, -100)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)


def Result():
    print("파란 거북이가 분홍 원보다 더 빨리 뛸 것이다.")

Result()

for (i) in range(100):
    d1 = random.randint(1, 60)
    t1.fd(d1)
    d2 = random.randint(1, 60)
    t2.fd(d2)

# 결과는 분홍 원이 파란 거북이보다 더 빨리 뛰었다.
