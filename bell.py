from turtle import Turtle

class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, x, y, dx, dy, rdius, color):
		Turtle.__init__(self)
		
		self.penup()
		self.goto(x,y)

		self.shape("circle")
		self.color(color)
		self.shapesize(rdius/10)


		self.dx = dx
		self.dy = dy
		self.radius = rdius


	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		current_y = self.ycor()

		new_x = current_x + self.dx
		new_y = current_y + self.dy

		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		up_side_ball = new_y + self.radius
		doun_side_ball = new_y - self.radius


		self.goto(new_x, new_y)

		if(right_side_ball >= screen_width):
			self.dx = -self.dx
			self.clear()

		if(left_side_ball <= -screen_width):
			self.dx = -self.dx
			self.clear()

		if(up_side_ball >= screen_height):
			self.dy = -self.dy
			self.clear()

		if(doun_side_ball <= -screen_height):
			self.dy = -self.dy
			self.clear()













		
		