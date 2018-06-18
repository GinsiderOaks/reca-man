"""Small module for generating the Recamán's sequence.
For more info, see https://oeis.org/A005132"""

def get_sequence(n, start_num=0, start_jump=1, jump_delta=1):
	"""Function for genereting and returning the sequence"""
	num = start_num
	jump = start_jump
	seq_set = set()
	seq_list = []
	
	for i in range(n):
	
		seq_set = seq_set | {num}
		seq_list.append(num)
		
		num = do_jump(num, jump, seq_set)
		jump += jump_delta
	
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