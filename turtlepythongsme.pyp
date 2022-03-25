import turtle
import random
import time

t = turtle.Turtle()
t.ht()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)

# поле
for i in range(0,16):
    t.write(i)
    t.right(90)
    t.forward(200)
    t.left(180)  
    t.forward(200)
    t.right(90)
    t.forward(20)

####первая черепашка
first = turtle.Turtle()
first.shape("turtle")
first.color("green")
first.up()
first.goto(-120,70)
first.down()

####вторая черепашка
second=turtle.Turtle()
second.shape("turtle")
second.color("blue")
second.up()
second.goto(-120,40)
second.down()

####третья черепашка
third=turtle.Turtle()
third.shape("turtle")
third.color("red")
third.up()
third.goto(-120,10)
third.down()
bolCount = random.randint(5,10)
for i in range(0, bolCount):
    bol =  turtle.Turtle()
    bol.shape("turtle")
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    bol.color(color1,color2,color3)
    bol.penup()
    bol.goto(-90+30*i,-120)
    bol.pendown()
    bol.left(90)
    
win = input("Какая черепаха победит:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("Ты считаешь, что победит " + win + " черепашка" ,font = ("Arial", 12, "bold"))

time.sleep(2)

x_first=0
x_second=0
x_third=0

while True:
    if x_first>305 or x_second>305 or x_third>305:
        break;
    first_step = random.randint(1,5)
    x_first += first_step
    first.forward(first_step)
    
    second_step = random.randint(1,5)
    x_second += second_step
    second.forward(second_step)
    
    third_step = random.randint(1,5)
    x_third += third_step
    third.forward(third_step)
    
if x_first >= x_second and x_first >= x_third:
    turtle_win = 1
elif x_second >= x_first and x_second >= x_third:
    turtle_win = 2
else:
    turtle_win = 3


if x_first >= 305:
    first.up()
    first.forward(30)
    first.write("Я победила")
    first.backward(30)
    x = input("Победила первая черепашка")
elif x_second >= 305:
    second.up()
    second.forward(30)
    second.write("Я победила")
    second.backward(30)
    x = input("Победила вторая черепашка")
elif x_third >= 305:
    third.up()
    third.forward(30)
    third.write("Я победила")
    third.backward(30)
    x = input("Победила третья черепашка")
elif x_fourth >= 305:
    fourth.up()
    fourth.forward(30)
    fourth.write("Я победила")
    fourth.backward(30)
    x = input("Победила четвертая черепашка")
elif x_fifth >= 305:
    fifth.up()
    fifth.forward(30)
    fifth.write("Я победила")
    fifth.backward(30)
    x = input("Победила пятая черепашка")




















