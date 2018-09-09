def quick_sort(input_list):
	"""Sort a list using quick sort algorithm

	@param list input_list: list of numbers, which is unsorted
	@return: sorted list
	@return_type: list
	"""

	split_list(input_list, 0, len(input_list) - 1)


def split_list(input_list, first_pos, last_pos):
	"""
	"""

	if first_pos < last_pos:
		split_point = partition_list(input_list, first_pos, last_pos)
		split_list(input_list, first_pos, split_point - 1)
		split_list(input_list, split_point + 1, last_pos)


def partition_list(input_list, first_pos, last_pos):
	"""
	"""

	pivot_value = input_list[first_pos]
	left_mark = first_pos + 1
	right_mark = last_pos
	is_done = False

	while not is_done:
		while left_mark <= right_mark and input_list[left_mark] <= pivot_value:
			left_mark = left_mark + 1
		while input_list[right_mark] >= pivot_value and right_mark >= left_mark:
			right_mark = right_mark - 1

		if right_mark < left_mark:
			is_done = True
		else:
			swap_value(input_list, left_mark, right_mark)

	swap_value(input_list, first_pos, right_mark)
	return right_mark


def swap_value(input_list, first_pos, second_pos):
	"""
	"""

	temp_value = input_list[first_pos]
	input_list[first_pos] = input_list[second_pos]
	input_list[second_pos] = temp_value


if __name__ == '__main__':
	input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(input_list)
	print(input_list)
