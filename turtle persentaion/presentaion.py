from turtle import *
import turtle as t
import time


win = t.Screen()                                     #To create window.
win.title("Abdulrahman computer graphics project")
win.bgcolor("grey")
win.setup(1200 , 600)

tu = t.Turtle()
tu.speed(0)
tu.hideturtle()
tu.penup()



def rectangle( x , horizontal , vertical , color):

    x.speed(0)
    x.hideturtle()
    x.pendown()
    x.pensize(1)
    x.color(color)
    x.begin_fill()
    for i in range(1, 3):
        x.forward(horizontal)
        x.right(90)
        x.forward(vertical)
        x.right(90)
    x.end_fill()
    x.penup()


def legs(x,  X , Y):
    x.goto(X-100, Y-150)
    rectangle(x ,50, 20, 'black')
    x.goto(X-30, Y-150)
    rectangle(x ,50, 20, 'black')
    x.goto(X-25, Y-50)
    rectangle(x ,15, 100, 'black')
    x.goto(X-55, Y-50)
    rectangle(x ,-15, 100, 'black')

def body(x , X , Y):
    x.goto(X-90, Y+100)
    rectangle(x ,100, 150, '#F3E7E5')


def rhand(x , X , Y):
    x.goto(X-120, Y+70)
    rectangle(x ,30, 15, 'black')
    x.goto(X-120, Y+70)
    rectangle(x ,15, 90, 'black')
    x.goto(X-112.5 , Y-40)
    x.color("#ffdbac")
    x.begin_fill()
    x.circle(10)
    x.end_fill()


def neck(x , X , Y):
    x.goto(X-50, Y+120)
    rectangle(x , 15, 20, '#ffdbac')


def head(x , X , Y):
    x.goto(X-85, Y+170)
    rectangle(x , 80, 50, '#ffdbac')

def eye(x  , X , Y):
    x.goto(X-55, Y+155)
    rectangle(x , 5, 5, 'black')
    x.goto(X-40, Y+155)
    rectangle(x , 5, 5, 'black')

def mouse( x , X , Y):
    x.goto(X-60, Y+140)
    rectangle(x ,30, 10, 'white')

def eyecl():
    eye(te , ta1 , 100 , 0)
    time.sleep(1)
    te.clear()
    ta1.clear()
    time.sleep(0.1)
    eye(te , ta1 , 100 , 0)

def zrz():
    ty = t.Turtle()
    ty.speed(0)
    ty.hideturtle()
    ty.up()
    ty.goto(-345 , 100)
    tu.down()
    ty.color("white")
    ty.begin_fill()
    ty.fd(80)
    ty.setheading(-120)
    ty.fd(50)
    ty.setheading(120)
    ty.fd(50)
    ty.end_fill()
    
    ty1 = t.Turtle()
    ty1.speed(0)
    ty1.hideturtle()
    ty1.up()
    ty1.goto(-292 , 88)
    ty1.down()
    ty1.color("yellow")
    ty1.begin_fill()
    ty1.circle(3)
    ty1.end_fill()
    ty1.up()
    ty1.goto(-292 , 73)
    ty1.down()
    ty1.begin_fill()
    ty1.circle(3)
    ty1.end_fill()

def hair(x):
    x.begin_fill()
    x.penup()
    x.goto(-340,170)
    x.pendown()
    x.color("red")
    x.left(60)
    x.circle(10 , -150)
    x.left(90)
    x.circle(10 , -150)
    x.left(90)
    x.circle(10 , -150)
    x.left(150)
    x.circle(10 , -150)
    x.left(100)
    x.circle(15 , -120)
    x.left(120)
    x.circle(15 , -120)
    x.left(100)
    x.circle(15 , -120)
    x.left(100)
    x.circle(15 , -120)
    x.left(90)
    x.circle(15 , -120)
    x.left(60)
    x.circle(13, -110)
    x.left(55)
    x.circle(15, -110)
    x.goto(-340,170)
    x.end_fill()

def logo( x , y):
    tu.hideturtle()
    tu.speed(6)
    tu.penup()
    tu.goto(x+0,y-190)
    tu.pendown()
    tu.color("#4997d0")
    tu.circle(100)

    tu.penup()
    tu.goto(x+0,y-170)
    tu.pendown()
    tu.circle(80)

    tu.begin_fill()
    tu.color("blue")
    tu.penup()
    tu.goto(x+0, y-150)
    tu.pendown()
    tu.circle(60)
    tu.end_fill()

    tu.penup()
    tu.goto(x-45, y-115)
    tu.pendown()

    tu.color('#FFFFFF')
    tu.write('FCAI', font = ('courier',30,'bold'))
    tu.hideturtle()

def lhandt(x , X , Y):
    x.goto(X+10, Y+70)
    rectangle(x ,60, 15, 'black')

def lhand(x , m , k , X , Y):
    x.goto(X+55, Y+110)
    x.setheading(m)
    rectangle(x ,15 , 40+k , 'black')
    x.goto(X+62.5 , Y+110)
    x.color("#ffdbac")
    x.begin_fill()
    x.circle(10)
    x.end_fill()
    x.setheading(0)

def tv():
    x = Turtle()
    y = Turtle()
    y.penup()
    y.goto(-125,125)
    y.pendown()
    y.width(10)
    y.color("black")
    y.fd(360)
    y.right(90)
    y.fd(160)
    y.right(90)
    y.fd(360)
    y.right(90)
    y.fd(160)
    y.right(90)
    y.hideturtle()

    x.hideturtle()
    x.speed(0)
    x.penup()
    x.goto(-120,120)
    x.pendown()
    x.begin_fill()
    x.color("#FFFFFF")
    x.fd(350)
    x.right(90)
    x.fd(150)
    x.right(90)
    x.fd(350)
    x.right(90)
    x.fd(150)
    x.right(90)
    x.end_fill()

    x.penup()
    x.goto(45,-30)
    x.pendown()
    x.begin_fill()
    x.color("black")
    x.fd(15)
    x.right(90)
    x.fd(50)
    x.right(90)
    x.fd(15)
    x.right(90)
    x.fd(50)
    x.right(90)
    x.end_fill()

    x.penup()
    x.goto(5,-80)
    x.pendown()
    x.begin_fill()
    x.color("black")
    x.fd(100)
    x.right(90)
    x.fd(20)
    x.right(90)
    x.fd(100)
    x.right(90)
    x.fd(20)
    x.right(90)
    x.end_fill()
    x.hideturtle()

def bye():
    ta1.clear()
    lhand(ta1 , -40  , 20 , -210 , 0)
    time.sleep(0.5)
    ta1.clear()
    lhand(ta1 , 0 , 0 , -250 , 0)
    time.sleep(0.4)
    ta1.clear()
    lhand(ta1 , -40  , 20 , -210 , 0)
    time.sleep(0.5)
    ta1.clear()
    lhand(ta1 , 0 , 0 , -250 , 0)
    time.sleep(0.4)
    ta1.clear()
    lhand(ta1 , -40  , 20 , -210 , 0)
    time.sleep(0.5)
    ta1.clear()
    lhand(ta1 , 0 , 0 , -250 , 0)
    time.sleep(0.4)
    ta1.clear()
    lhand(ta1 , -40  , 20 , -210 , 0)
    time.sleep(0.5)


def speak(a , b , c , d , e , f , g):
    trr = t.Turtle()
    trr.hideturtle()
    trr.speed(1)
    trr.up()
    trr.goto(-100 , 90)
    trr.down()
    tm.clear()
    mouse(tm  , -250 , 0)
    trr.write(a , font = ('courier',13,'bold'))
    time.sleep(2)
    trr.up()
    trr.goto(-100 , 70)
    trr.down()
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    trr.write(b , font = ('courier',13,'bold'))
    time.sleep(2)
    trr.up()
    trr.goto(-100 , 50)
    trr.down()
    trr.write(c, font = ('courier',13,'bold'))
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    time.sleep(2)
    trr.up()
    trr.goto(-100 , 30)
    trr.down()
    te.clear()
    eye(te , -240 , 0)
    trr.write(d , font = ('courier',13,'bold'))
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    time.sleep(1)
    trr.up()
    trr.goto(-100 , 10)
    trr.down()
    trr.write(e , font = ('courier',13,'bold'))
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    time.sleep(1)
    trr.up()
    trr.goto(-100 , -10)
    trr.down()
    te.clear()
    eye(te , -240 , 0)
    trr.write(f , font = ('courier',13,'bold'))
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    time.sleep(1)
    trr.up()
    trr.goto(-100 , -30)
    trr.down()
    trr.write(g , font = ('courier',13,'bold'))
    tm.clear()
    time.sleep(0.5)
    mouse(tm  , -250 , 0)
    trr.clear()

th = t.Turtle()
th.speed(0)
th.hideturtle()
th.penup()

thi = t.Turtle()
thi.speed(0)
thi.hideturtle()
thi.penup()


te = t.Turtle()
te.speed(0)
te.hideturtle()
te.penup()


ta = t.Turtle()
ta.speed(0)
ta.hideturtle()
ta.penup()
ta1 = t.Turtle()
ta1.speed(0)
ta1.hideturtle()
ta1.penup()

tb = t.Turtle()
tb.speed()
tb.hideturtle()
tb.penup()

tn = t.Turtle()
tn.speed(0)
tn.hideturtle()
tn.penup()

tm = t.Turtle()
tm.speed(0)
tm.hideturtle()
tm.penup()

tl = t.Turtle()
tl.speed(0)
tl.hideturtle()
tl.penup()

legs(tl ,-250 ,0)
body(tb , -250 , 0)
lhand(ta1 , 0 , 0 , -250 , 0)
lhandt(ta , -250 , 0)
rhand(ta , -250 , 0)
zrz()
neck(tn , -250 , 0)
hair(thi)
head(th , -250 , 0)
eye(te , -250 , 0)
mouse(tm  , -250 , 0)
logo(380 , 220)
bye()

tv()


speak("Hi,DR:Heba,Eng:hanem" , "I wish you both" ,
        "a good day" , "this code done by" , "Fares Ouref"
        , "Roshdy","" )

speak("A word from the college dean:" , "Within the framework of" ,
        "the political leadership’s" , " which all forces will" , "rely on in providing"
        , "digital smart services" ," to citizens," )


speak("artificial intelligence is " , "the second,after smart" ," devices" , "directed towards adopting" , "all smart services," , "directed towards adopting all" , "smart tools and technologies" ,)


speak("including working to " , "improve government performance" ,
        "at all levels so that " , "it shall be" , "an integral part "
        , "the work of the " ,"govenment in the country" )

speak("College Vision" , "leadership in education," ,
        "scientific research and" , "community service," ,
        "and raising the "
        , "the scientific" ,"practical and search level",
        )

speak("Information systems and" , "technology and AI to" ,
        "achieve a distinguished" , "position among colleges" ,
        "of computer and"," information "
        , "locally and internationally" )

speak("Finally, I would like to thank" , "you for reading." ,
        "Bye❤️","","","","")

############################################################

from turtle import Turtle, Screen

def speak(*sentences):
    for sentence in sentences:
        x.write(sentence, align="center", font=("Arial", 10, "normal"))
        x.penup()
        x.goto(center_x, x.ycor() + 20)  # Adjust the spacing between sentences
        x.pendown()

# Create a Screen
screen_width = 1200
screen_height = 600
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.setworldcoordinates(0, screen_height, screen_width, 0)  # Adjust coordinates to start from the top

# Create a Turtle
x = Turtle()
x.hideturtle()
x.penup()
center_x = screen_width / 2
center_y = screen_height
x.goto(200, 100)  # Start from the top of the screen
x.pendown()

# Provide the sentences
speak(
    "A word from the college dean:",
    "Within the framework of the liberal leadership’s pursuit of change,",
    "which all forces will rely on in providing digital smart services to citizens,",
    "artificial intelligence is the second, after smart services, directed towards",
    "adopting all smart tools and technologies, including working to improve",
    "government performance at all levels so that it shall be an integral part of",
    "the work of the government in the country. The impact of artificial intelligence",
    "includes all aspects of our daily lives. And there is no doubt...",
    "",
    "College vision:",
    "Leadership in education, scientific research and community service, and",
    "raising the scientific, practical and research level in the fields of computer",
    "science, information systems and technology and artificial intelligence to",
    "achieve a distinguished position among colleges of computers and information",
    "locally and internationally."
)

# Hide the turtle and display the screen
x.hideturtle()
screen.mainloop()


#########################################################################





te.clear()
eye(te , -250 , 0)
bye()

win.mainloop()

