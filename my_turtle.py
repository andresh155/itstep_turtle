import turtle as t 
import random as r
def select_task():
    task = input("виберіть задавдання: 1-3 ")
    match task:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
def task1():
    t.color("black")
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.penup()
    t.forward(150)
    t.pendown()
    t.color("green")
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.penup()
    t.left(180)
    t.forward(350)
    t.pendown()
    t.color("blue")
    for _ in range(5):
        t.forward(100)
        t.left(72)
    t.done()
def task2():
    t.color("black")
    for _ in range(5):
        t.forward(100)
        t.left(144)
    t.done()
def task3():
    for _ in range(36):
        t.color(r.random(), r.random(), r.random())
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.left(10)
    t.done()
while True:
    select_task()
