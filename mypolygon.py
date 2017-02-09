import turtle
bob = turtle.Turtle()
print(bob)


def square(t,length):
	for i in range(4):
		t.fd(length)
		t.lt(90)


def polygon(t,length,sides):
	for i in range(sides):
		t.fd(length)
		t.lt(360/sides)	


def circle(t,r):
	sides = 50
	circ = 2*3.14*r 
	length = circ/sides  
	
	for i in range(sides):
		t.fd(length)
		t.lt(360/sides)
		
def arc(t,r,a):
	sides = 50
	circ = 2*3.14*r 
	length = circ/sides  
	
	for i in range(sides):
		t.fd(length)
		t.lt(a/sides)

		
square(bob,50)		
polygon(bob,50,6)
circle(bob,50)
arc(bob,100,270)

turtle.mainloop()
