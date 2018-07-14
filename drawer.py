import turtle
import math
import argparse
import reca_sequence as rec_sec

"""Module for drawing the Recamán's sequence"""

DEFAULT_SPEED		= 'fastest'
DEFAULT_PEN_COLOR	= 'black'
DEFAULT_BG_COLOR	= 'white'
DEFAULT_CIRCLE_RES	= None
DEFAULT_SHAPE		= 'classic'
DEFAULT_HIDDEN		= False
DEFAULT_SIZE		= 1
DEFAULT_PEN_SIZE	= 1

class Circle_Drawer:
	def __init__(self, 
		sequence, 
		speed		=DEFAULT_SPEED, 
		pencolor	=DEFAULT_PEN_COLOR, 
		bgcolor	=DEFAULT_BG_COLOR, 
		circleres	=DEFAULT_CIRCLE_RES, 
		shape		=DEFAULT_SHAPE, 
		hidden		=DEFAULT_HIDDEN, 
		size		=DEFAULT_SIZE, 
		pensize	=DEFAULT_PEN_SIZE
		):
		
		self.sequence		= sequence
		self._speed			= speed
		self._pen_color		= pencolor
		self._bg_color		= bgcolor
		self._circle_res	= circleres
		self._shape			= shape
		self._hidden		= hidden
		self._size			= size
		self._pen_size		= pensize
		
	def from_args(sequence, args):
		return Circle_Drawer(
			sequence, 
			args.speed,
			args.pencolor,
			args.bgcolor,
			args.circleres,
			args.shape,
			args.hidden,
			args.size,
			args.pensize)
		
	def _draw(self):
		
		sequence	= self.sequence
		bg_color	= self._bg_color
		hidden		= self._hidden
		speed		= self._speed
		pen_color	= self._pen_color
		shape		= self._shape
		steps		= self._circle_res
		size		= self._size
		pen_size	= self._pen_size
		
		switch = 1
		
		win_width = \
			max(
			[abs(sequence[i-1] - sequence[i]) 
			for i in range(1, len(sequence))]) * 2 * size + math.floor(pen_size / 2)
			
		win_height = max(sequence) * 2 * size + math.floor(pen_size / 2)
		
		turtle.setup()
		turtle.screensize(win_width, win_height, bg_color)
		
		t = turtle.Turtle()
		if hidden:
			t.hideturtle()
		t.speed(speed)
		t.pencolor(pen_color)
		t.shape(shape)
		t.pensize(pen_size)
		
		t.pu()
		t.setpos(0, -int(win_height/2))
		t.pd()
		
		old_num = sequence[0]
		for i in range(1, len(sequence)):
			num = sequence[i]
			radius = (num - old_num) * switch * size
			t.circle(radius, 180, steps=steps)
			
			old_num = num
			switch *= -1
		
		turtle.done()
	
	def draw(self):
		try:
			self._draw()
				
		except turtle.Terminator:
			pass
	
def add_parser_args(parser):
	parser.add_argument(
		'-sp', '--speed', 
		choices=['slowest', 'slow', 'normal', 'fast', 'fastest'], 
		help='The speed of the drawer')
	parser.add_argument(
		'-pe', '--pencolor',
		choices=['black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange'],
		help='The color of the pen')
	parser.add_argument(
		'-bg', '--bgcolor',
		choices=['black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange'],
		help='The color of the background')
	parser.add_argument(
		'-cr', '--circleres',
		type=int,
		help='The resolution of the circle (dynamic if non-specified)')
	parser.add_argument(
		'-sh', '--shape',
		choices=['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'], 
		help='The shape of the turtle')
	parser.add_argument(
		'-hi', '--hidden', 
		action='store_true', 
		help='Should the turtle be hidden?')
	parser.add_argument(
		'-si', '--size',
		type=int,
		help='The size of the drawing')
	parser.add_argument(
		'-ps', '--pensize',
		type=int,
		help='The thickness of the pen')
		
	parser.set_defaults(
		speed		=DEFAULT_SPEED,
		pencolor	=DEFAULT_PEN_COLOR,
		bgcolor		=DEFAULT_BG_COLOR,
		circleres	=DEFAULT_CIRCLE_RES,
		shape		=DEFAULT_SHAPE,
		hidden		=DEFAULT_HIDDEN,
		size		=DEFAULT_SIZE,
		pensize		=DEFAULT_PEN_SIZE)
	
def main():
	
	parser = argparse.ArgumentParser(description='Parser for input for drawer and sequence.')
	
	add_parser_args(parser)
	rec_sec.add_parser_args(parser)
	
	args = parser.parse_args()
	
	sequence = args.get_sequence(args)
	cd = Circle_Drawer.from_args(sequence, args)
	cd.draw()
		
if __name__ == '__main__':
	main()