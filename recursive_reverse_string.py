def reverse_string(input_string):
	if len(input_string) <= 1:
		return input_string
	else:
		return reverse_string(input_string[1:]) + input_string[0]


if __name__ == '__main__':
	print(reverse_string('hello'))
	print(reverse_string(''))
	print(reverse_string('b'))
