import turtle
m = turtle.Turtle()
m.width(5)
sc = turtle.Screen()
sc.title("Shakl")

m.penup()
m.left(90)
m.forward(100)
m.right(90)
m.back(100)
m.pendown()

a = int(input("Nechta tomonli shakl chizilishini xohlaysiz? (Masalan: 3, 4, 5, 6)"))

b = input("Shakl qanday rangda bo'lishini xohlaysiz? (Qizil, Qora, Yashil, Oq)")

d = input("Qalam qanday rangda chizishini xohlaysiz? (Qizil, Qora, Yashil, Oq)")

if d == "Qizil":
    m.color("red")
elif d == "Qora":
    m.color("black")
elif d == "Yashil":
    m.color("green")
elif d == "Oq":
    m.color("white")
else:
    print("Bunday rang qila olmaymiz")

if b == "Qizil":
    sc.bgcolor("red")
elif b == "Qora":
    sc.bgcolor("black")
elif b == "Yashil":
    sc.bgcolor("green")
elif b == "Oq":
    sc.bgcolor("white")
else:
    print("Bunday rang qila olmaymiz")

s = int(360/a)

for n in range(a):
    m.forward(50)
    m.right(s)
        
