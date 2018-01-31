import turtle
import time 
import random
import math
from bell import Ball

turtle.tracer(0)
turtle.hideturtle()


RUNNING = True
SLEEP = 0.01
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0, 0, 0, 0, 30, "red")


NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30	
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]

for i in range (NUMBER_OF_BALLS):
	x = (random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS ))
	y = (random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,  SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = (random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX))
	dy = (random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY))

	while dx == 0 or dy == 0:
		dx = (random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX))
		dy = (random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY))
	#come back and write this
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(),random.random())
	ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)



def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	d = math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2) + math.pow((ball_a.ycor()-ball_b.ycor()),2))
	if d + 10 <= ball_a.radius+ ball_b.radius:
		return True
	else:
		return False



def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				x = (random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS ))
				y = (random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,  SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = (random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX))
				dy = (random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY))
				while dx == 0 or dy == 0:
					dx = (random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX))
					dy = (random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY))

				radius = (random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS))
				color = (random.random(), random.random(),random.random())
				
				if ball_a.radius>ball_b.radius: #ball_b is smaller
					ball_b.goto(x,y)
					ball_b.dx =dx
					ball_b.dy = dy
					ball_b.radius = radius
					ball_b.color=color
					ball_b.shapesize(radius/10)

					ball_a.radius =+ 1
					ball_a.shapesize(ball_a.radius/10)

				else:
					ball_a.goto(x,y)
					ball_a.dx = dx
					ball_a.dy = dy
					ball_a.radius = radius
					ball_a.color=color
					ball_a.shapesize(radius/10)
					
					ball_b.radius = ball_b.radius+1
					ball_b.shapesize(ball_b.radius/10)


def check_myball_collision():
	for ball in BALLS:
		if collide(ball,MY_BALL):
			if MY_BALL.radius<ball.radius:
				return False
			else:
				x = (random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS ))
				y = (random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,  SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				ball.goto(x,y)
				ball.dx = (random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX))
				ball.dy = (random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY))

			


				#same thing here
				ball.radius = (random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS))
				ball.color = (random.random(), random.random(),random.random())
				ball.shapesize(ball.radius/10)
				MY_BALL.radius = MY_BALL.radius+1
				MY_BALL.shapesize(MY_BALL.radius/10)

	return True


def movearound(event):
	MY_BALL.goto( event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()


while RUNNING:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HIEGHT = turtle.getcanvas().winfo_hieght()/2
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()