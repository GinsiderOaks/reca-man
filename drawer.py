import turtle
import reca_sequence as re_se

"""Module for drawing the Recamán's sequence"""

class Circle_Drawer:
	def __init__(self, sequence, size=1, speed='normal', color='black', circle_res=None, shape='classic'):
		t = turtle.Turtle()
		t.speed(speed)
		t.pencolor(color)
		t.shape(shape)
		
		self.t = t
		self.sequence = sequence
		self._size = size
		self._circle_res = circle_res
		
	def _draw(self):
		t = self.t
		screen = t.getscreen()
		
		sequence = self.sequence
		steps = self._circle_res
		switch = 1
		size = self._size
		
		canvwidth = int(max([abs(sequence[i-1] - sequence[i]) for i in range(1, len(sequence))]) * size)
		canvheight = int(max(sequence) * size)
		
		screen.screensize(canvwidth=canvwidth, canvheight=canvheight)
		
		t.pu()
		t.sety(-int(canvheight / 2))
		t.pd()
		
		print(turtle.screensize())
		
		old_num = sequence[0]
		for i in range(1, len(sequence)):
			num = sequence[i]
			radius = (num - old_num) * size * switch
			print(t.pos())
			t.circle(radius, 180, steps=steps)
			
			old_num = num
			switch *= -1
		
		turtle.done()
	
	def draw(self):
		try:
			self._draw()
				
		except turtle.Terminator:
			pass
		
def main():
	while True:
		n = input('How long of a sequence do you want? ')
		try:
			n = int(n)
		except ValueError:
			print('Please type a non-negative number.')
			continue
		if n < 0:
			print('Please type a non-negative number.')
			continue
		break

	sequence = re_se.get_sequence(n)
	cd = Circle_Drawer(sequence, speed='fast')
	cd.draw()
		
if __name__ == '__main__':
	main()