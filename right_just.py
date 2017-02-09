def right_justify(s):
	s_length = len(s)
	location = 70-s_length
	padding = (" "*location)
	print(padding+s)
	
right_justify('monty')

def print_grid():
	line_sub_a = ('+ '+'- '*5)
	line_sub_b = ('/ '+' '*10)
	line_seg_a = (line_sub_a*2+' +')
	line_seg_b = (line_sub_b*2+' /')
	
	print(line_seg_a)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_a)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_b)
	print(line_seg_a)
	
	
print_grid()