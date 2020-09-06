import turtle

win = turtle.Screen()
win.title("Pong by yabi")
win.bgcolor("black")
win.setup(width=800 , height=600)
win.tracer(0)

# Score 
Score_a = 0
Score_b = 0

# Pen
pen =turtle.Turtle()
pen.speed(0)
pen.penup() # don't want to draw a line when pen move
pen.color("white")
pen.hideturtle()
pen.goto(0,260)

show_score="Player A:" + str(Score_a) +" " + "Player B:" + str(Score_b)
pen.write(show_score,align="center", font=("Courier", 24, "normal"))

# Gameover
GG =turtle.Turtle()
GG.speed(0)
GG.penup() # don't want to draw a line when pen move
GG.color("white")
GG.hideturtle()
GG.goto(0,0)

# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_a_right():
    x=paddle_a.xcor()
    x+=20
    paddle_a.setx(x)
def paddle_a_left():
    x=paddle_a.xcor()
    x-=20
    paddle_a.setx(x)


def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

def paddle_b_right():
    x=paddle_b.xcor()
    x+=20
    paddle_b.setx(x)
def paddle_b_left():
    x=paddle_b.xcor()
    x-=20
    paddle_b.setx(x)
# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    win.update()

    # Love ya!
    if Score_b > 5:
        
        GG.write("Love ya! Ting<3", align="center", font=("Courier", 30, "normal"))
    if Score_a > 5:
        
        GG.write("Ridiculous! ", align="center", font=("Courier", 30, "normal"))

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        Score_a += 1
        pen.clear()
        show_score="Player A:" + str(Score_a) +" " + "Player B:" + str(Score_b)
        pen.write(show_score,align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        Score_b += 1
        pen.clear()
        show_score="Player A:" + str(Score_a) +" " + "Player B:" + str(Score_b)
        pen.write(show_score,align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
        ball.dx *= -1
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ):
        ball.dx *= -1