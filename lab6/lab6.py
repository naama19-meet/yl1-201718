from turtle import *
import random
import math 

class Ball(Turtle):
	"""docstring for ball"""
	def __init__(self, rdius,color,speed):
		Turtle. __init__(self)
		self.shape("circle")
		self.shapesize(rdius/10)
		self.rdius = rdius
		self.color(color)
		self.speed(speed)


ball1 = Ball(10, "green", 1)
ball2 = Ball(5, "red", 6)

#def check_collision(ball1,ball2):
#	d = math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2) + math.pow((ball1.ycor()-ball2.ycor()),2))
#	if d <= ball1.rdius+ ball2.rdius:
#		print("collision!!!")
#	else:
#		print("not collision  :(")
#
#check_collision(ball1,ball2)
#mainloop()
 









balls = []
balls.append(ball1)
balls.append(ball2)

#print(balls)


def check_collision(balls):
	d = math.sqrt(math.pow((balls[0].xcor()-balls[1].xcor()),2) + math.pow((balls[0].ycor()-balls[1].ycor()),2))
	if d <= balls[0].rdius+ balls[1].rdius:
		if balls[0].rdius < balls[1].rdius:
			balls[0].goto(50,50)
		else:
			balls[1].goto(50,50)


check_collision(balls)



mainloop()