# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle



# Your code here.

def draw_square(some_turtle):
	for i in range(4):
		some_turtle.fd(100)
		some_turtle.rt(90)

def draw_square_circle(some_turtle,angle):
	times = 360/angle
	for i in range(times):
		draw_square(some_turtle)
		some_turtle.rt(angle)

def draw_diamond(some_turtle):
	for i in range(2):
		some_turtle.fd(100)
		some_turtle.rt(20)
		some_turtle.fd(100)
		some_turtle.rt(160)

def draw_flower(some_turtle,density):
	angle = 360/density;
	for i in range(density):
		draw_diamond(some_turtle)
		some_turtle.rt(angle)
	some_turtle.rt(90)
	some_turtle.fd(500)

def turtle_draw():
	window = turtle.Screen()
	window.bgcolor("red")

	tom = turtle.Turtle()
	tom.shape('turtle')
	tom.color('yellow')
	tom.speed(0)
	density = 72
	# angle = 20
	draw_flower(tom,density)
	# draw_diamond(tom)
	# draw_square(tom)
	# draw_square_circle(tom,angle)
	# for i in range(4):
	# 	tom.forward(100)
	# 	tom.right(90)

	# angie = turtle.Turtle()
	# angie.shape('turtle')
	# angie.color('blue')
	# angie.circle(100)

	# jenny = turtle.Turtle()
	# jenny.shape('turtle')
	# jenny.color('green')
	# for i in range(3):
	# 	jenny.fd(100)
	# 	jenny.lt(120)


	window.exitonclick()


turtle_draw()