from turtle import *
import random

class Ball(Turtle):
	"""docstring for ball"""
	def __init__(self, rdius,color,speed):
		Turtle. __init__(self)
		self.shape("circle")
		self.shapesize(rdius/10)
		self.rdius = rdius
		self.color(color)
		self.speed(speed)


ball1 = Ball(10, "blue", 10)
ball2 = Ball(11, "pink", 5)

def chack_collision(ball1,ball2):
	

	math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2) + math.pow((ball1.ycor()-ball2.ycor()),2))
mainloop()
