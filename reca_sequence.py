"""Small module for generating the Recamán's sequence.
For more info, see https://oeis.org/A005132"""

DEFAULT_NUM_START = 0
DEFAULT_JUMP_START = 1
DEFAULT_JUMP_DELTA = 1

def add_parser_args(parser):
	parser.add_argument(
		'seqlen',
		type=int,
		help='The length of the sequence')
	
	parser.add_argument(
		'-ns', '--numstart',
		nargs='?',
		type=int,
		help='The starting number of the sequence')
		
	parser.add_argument(
		'-js', '--jumpstart',
		nargs='?',
		type=int,
		help='The starting jump value of the sequence')
		
	parser.add_argument(
		'-jd', '--jumpdelta',
		nargs='?',
		type=int,
		help='The increment of jump')
		
	parser.set_defaults(
		get_sequence=get_sequence_from_args,
		numstart	=DEFAULT_NUM_START,
		jumpstart	=DEFAULT_JUMP_START,
		jumpdelta	=DEFAULT_JUMP_DELTA)

def get_sequence_from_args(args):
	return get_sequence(args.seqlen, args.numstart, args.jumpstart, args.jumpdelta)
	
def get_sequence(seqlen, startnum=0, startjump=1, jumpdelta=1):
	"""Function for generating and returning the sequence"""
	num = startnum
	jump = startjump
	seq_set = set()
	seq_list = []
	
	for i in range(seqlen):
	
		seq_set = seq_set | {num}
		seq_list.append(num)
		
		num = do_jump(num, jump, seq_set)
		jump += jumpdelta
	
	return seq_list
	
def do_jump(num, jump, seq_set):
	"""Determines if a negative jump is possible, otherwise jumps positively"""
	num = num - jump
	if num < 0 or num in seq_set:
		num += jump * 2
		
	return num
	
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
	
	seq = get_sequence(n)
	print(seq)
	
if __name__ == '__main__':
	main()