import turtle
import math
import argparse
import reca_sequence as re_se

"""Module for drawing the Recamán's sequence"""

class Circle_Drawer:
	def __init__(self, sequence, speed='normal', pen_color='black', bg_color='white', circle_res=None, shape='classic', hidden=False, size=1, pen_size=1):
		
		self.sequence		= sequence
		self._speed			= speed
		self._pen_color		= pen_color
		self._bg_color		= bg_color
		self._circle_res	= circle_res
		self._shape			= shape
		self._hidden		= hidden
		self._size			= size
		self._pen_size		= pen_size
		
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

def check_positive(value):
	if value == None:
		return value
	ivalue = int(value)
	if ivalue <= 0:
		raise argparse.ArgumentTypeError('{0} is an invalid positive int value'.format(value))
	return ivalue
			
def parse_args():

	parser = argparse.ArgumentParser(description='Parser for input for drawer.')
	
	# SEQUENCE RELATED
	parser.add_argument(
		'seqlen',
		type=check_positive,
		help='The length of the sequence')
	
	parser.add_argument(
		'-sn', '--startnum',
		nargs='?',
		type=check_positive,
		help='The starting number of the sequence')
		
	parser.add_argument(
		'-sj', '--startjump',
		nargs='?',
		type=check_positive,
		help='The starting jump value of the sequence')
		
	parser.add_argument(
		'-jd', '--jumpdelta',
		nargs='?',
		type=check_positive,
		help='The increment of jump')
		
	# DRAWING RELATED
	parser.add_argument(
		'-sp', '--speed', 
		nargs='?', 
		default='fastest',
		choices=['slowest', 'slow', 'normal', 'fast', 'fastest'], 
		help='The speed of the drawer')
	parser.add_argument(
		'-pc', '--pencolor',
		nargs='?',
		default='black',
		choices=['black', 'white', 'red', 'green', 'yellow'],
		help='The color of the pen')
	parser.add_argument(
		'-bg', '--bgcolor',
		nargs='?',
		default='white',
		choices=['black', 'white', 'red', 'green', 'yellow'],
		help='The color of the background')
	parser.add_argument(
		'-cr', '--circleres',
		nargs='?',
		type=check_positive,
		default=None,
		help='The resolution of the circle (dynamic if non-specified)')
	parser.add_argument(
		'-sh', '--shape', 
		nargs='?', 
		default='classic',
		choices=['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'], 
		help='The shape of the turtle')
	parser.add_argument(
		'-hi', '--hidden', 
		nargs='?', 
		default=False,
		type=bool, 
		help='Should the turtle be hidden?')
	parser.add_argument(
		'-si', '--size',
		nargs='?',
		type=check_positive,
		default=1,
		help='The size of the drawing')
	parser.add_argument(
		'-ps', '--pensize',
		nargs='?',
		type=check_positive,
		default=1,
		help='The thickness of the pen')
		
	args = parser.parse_args()
	return args
		
def main():
	args = parse_args()
	
	print(args.__dict__)
	
	draw_args_dict = {
		'bg_color':		args.bgcolor, 
		'circle_res':	args.circleres, 
		'pen_color':	args.pencolor, 
		'hidden':		args.hidden, 
		'speed':		args.speed, 
		'shape':		args.shape,
		'size':			args.size,
		'pen_size':		args.pensize}
		
	seq_args = (args.seqlen,)
	seq_args_dict = {
		'start_num':	args.startnum,
		'start_jump':	args.startjump,
		'jump_delta':	args.jumpdelta}
	# Removes none-values from seq_args_dict
	seq_args_dict = {k:v for k,v in seq_args_dict.items() if v is not None}
	
	sequence = re_se.get_sequence(*seq_args, **seq_args_dict)
	cd = Circle_Drawer(sequence, **draw_args_dict)
	cd.draw()
		
if __name__ == '__main__':
	main()