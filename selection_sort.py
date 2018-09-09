def selection_sort(input_list):
	number_of_process = len(input_list) - 1
	while number_of_process > 0:
		position_max = 0
		for i in range(1, number_of_process + 1):
			if input_list[i] > input_list[position_max]:
				position_max = i

		input_list[position_max], \
			input_list[number_of_process] = input_list[number_of_process], \
				input_list[position_max]
		number_of_process = number_of_process - 1
		
	return input_list


if __name__ == '__main__':
	input_list = [54,26,93,17,77,31,44,55,20]
	print(selection_sort(input_list))
