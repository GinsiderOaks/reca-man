import turtle
import reca_sequence as re_se

"""Module for drawing the Recamán's sequence"""

class Circle_Drawer:
	def __init__(self, sequence, speed='normal', pen_color='black', bg_color='white', circle_res=None, shape='classic', hidden=False):
		
		self.sequence = sequence
		self._speed = speed
		self._pen_color = pen_color
		self._bg_color = bg_color
		self._circle_res = circle_res
		self._shape = shape
		self._hidden = hidden
		
	def _draw(self):
		
		sequence = self.sequence
		bg_color = self._bg_color
		hidden = self._hidden
		speed = self._speed
		pen_color = self._pen_color
		shape = self._shape
		steps = self._circle_res
		switch = 1
		
		win_width = max([abs(sequence[i-1] - sequence[i]) for i in range(1, len(sequence))]) * 2
		win_height = max(sequence) * 2
		
		turtle.setup()
		turtle.screensize(win_width, win_height, bg_color)
		
		t = turtle.Turtle()
		if hidden:
			t.hideturtle()
		t.speed(speed)
		t.pencolor(pen_color)
		t.shape(shape)
		
		t.pu()
		t.setpos(0, -int(win_height/2))
		t.pd()
		
		old_num = sequence[0]
		for i in range(1, len(sequence)):
			num = sequence[i]
			radius = (num - old_num) * switch
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
	cd = Circle_Drawer(sequence, speed='fastest')
	cd.draw()
		
if __name__ == '__main__':
	main()