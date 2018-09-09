def bubble_sort(input_list):
	is_sorted_list = False
	number_of_process = len(input_list) - 1
	while number_of_process > 0 and not is_sorted_list:
		is_sorted_list = True
		for i in range(number_of_process):
			if input_list[i] > input_list[i + 1]:
				is_sorted_list = False
				input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
		number_of_process = number_of_process - 1
	return input_list


if __name__ == '__main__':
	input_list = [5, 80, 30, 50, 36, 10, 20]
	print(bubble_sort(input_list))
	input_list = [5, 10, 15, 35, 46, 60]
	print(bubble_sort(input_list))
