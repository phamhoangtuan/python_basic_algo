def remove_space(input_string):
	return input_string.replace(' ', '').replace('"', '')


def is_palindrome(input_string):
	if len(input_string) <= 1:
		return True
	elif input_string[0] != input_string[-1]:
		return False
	return is_palindrome(remove_space(input_string[1:-1]))


if __name__ == '__main__':
	print(is_palindrome('x'))
	print(is_palindrome('radar'))
	print(is_palindrome('hello'))
	print(is_palindrome(''))
	print(is_palindrome('hannah'))
	print(is_palindrome('madam i"m adam'))
