import turtle
import random
from time import sleep

### USER SETTINGS ###
baseSpeed = 3 # Base speed for the drawing intervals
LOD = 1 # Levels of details for the circle. They will take longer to draw and it's barely noticable
fillMode = False # Weither to fill the circles
clearOnBounce = True # Weither to clear the canvas on bounce
rgb = True # Weither the circles are RGB
rgbInterval = 2 # How much the color changes per circle.
gradient = [(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255)] # List of gradients to cycle through when RGB is on
#####################


turtle.hideturtle() # Hide the turtle
turtle.speed(0) # Make the turtle move as fast as it can
turtle.tracer(0, 0) # Disables screen refreshing and screen updates
turtle.title("Circles!")
turtle.penup()

screen = turtle.getscreen()
screen.setup(1.0, 1.0) # Open the window in 100% size
screen.screensize(screen.window_width()/2,screen.window_height()/2)
screen.colormode(255) # RGB
Mx,My = screen.screensize()
print("Canvas size:",Mx,My)

screen.bgcolor("black")
turtle.pencolor("white")

def drawCircle(x,y,radius):
	turtle.goto(x,y)

	if fillMode:
		turtle.begin_fill()
	else:
		turtle.pendown()
	for j in range(360*LOD): # Draw the circle
		turtle.forward(radius/LOD)
		turtle.left(1/LOD)
	if fillMode:
		turtle.end_fill()
	else:
		turtle.penup()

def drawCanvasBox(): # Draws a box around the canvas
	oldpos = turtle.pos()
	turtle.penup()
	turtle.setx(Mx)
	turtle.sety(-My)
	turtle.pendown()
	turtle.sety(My)
	turtle.setx(-Mx)
	turtle.sety(-My)
	turtle.setx(Mx)
	turtle.penup()
	turtle.goto(oldpos)

drawCanvasBox()
r,g,b=1,1,1
curgradient = 0
while True:
	if clearOnBounce:
		turtle.clear()
		drawCanvasBox()

	if turtle.xcor() > Mx: # If turtle above max X
		turtle.setx(Mx-10)
	elif turtle.xcor() < -Mx: # If turtle under minimum X
		turtle.setx(-Mx+10)

	if turtle.ycor() > My:
		turtle.sety(My-10)
	elif turtle.ycor() < -My:
		turtle.sety(-My+10)


	Yspeed = random.random()*10
	Xspeed = random.random()*10

	print("Direction chosen: ",end="")

	#Determine if we go +x or -x
	if random.random() < .5:
		print("+X, ",end="")
		Xdirection = baseSpeed+Xspeed
	else:
		print("-X, ",end="")
		Xdirection = -(baseSpeed+Xspeed)

	#Determine if we go +y or -y
	if random.random() < .5:
		print("+Y",end="")
		Ydirection = baseSpeed+Yspeed
	else:
		print("-Y",end="")
		Ydirection = -(baseSpeed+Yspeed)
	
	print(" Function: ",end="")
	#Determine if we use the min or max function when picking the radius, leading to different visual effects for the same path
	if random.random() < .5:
		print("max",end="\r")
		maxmin = max
	else:
		print("min",end="\r")
		maxmin = min

	#While the turtle is inbound:
	# X coords under max X
	# Y coords under max Y
	# Y coords above min Y
	# X coords above min X
	while turtle.xcor() <= Mx and turtle.ycor() <= My and turtle.ycor() >= -My and turtle.xcor() >= -Mx:
		if r < gradient[curgradient][0]:
			r+=rgbInterval
		elif r > gradient[curgradient][0]:
			r-=rgbInterval

		if g < gradient[curgradient][1]:
			g+=rgbInterval
		elif g > gradient[curgradient][1]:
			g-=rgbInterval

		if b < gradient[curgradient][2]:
			b+=rgbInterval
		elif b > gradient[curgradient][2]:
			b-=rgbInterval
		if r>255:
			r = 255
		elif r<0:
			r = 0

		if g>255:
			g = 255
		elif g<0:
			g = 0

		if b>255:
			b = 255
		elif b<0:
			b = 0

		if r == gradient[curgradient][0] and g == gradient[curgradient][1] and b == gradient[curgradient][2]:
			curgradient+=1
			if len(gradient) == curgradient:
				curgradient = 0

		if rgb:
			turtle.pencolor((r,g,b))
			turtle.fillcolor((r,g,b))

		Xmotion = Xdirection+turtle.xcor()
		Ymotion = Ydirection+turtle.ycor()

		try: # Get some semi random circle sizes n shit using math idk
			radius = maxmin(Ymotion/Xmotion,Xmotion/Ymotion)
		except ZeroDivisionError as e: # division per zero lol
			radius = 0

		drawCircle(Xmotion,Ymotion,radius)
		turtle.update()
		sleep(0.05)