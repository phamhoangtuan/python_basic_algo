def binary_search(input_list, search_item):
	if len(input_list) == 0:
		return False
	else:
		mid_point = len(input_list) / 2
		if input_list[mid_point] == search_item:
			return True
		else:
			if input_list[mid_point] < search_item:
				return binary_search(input_list[mid_point + 1:], search_item)
			else:
				return binary_search(input_list[:mid_point], search_item)


if __name__ == '__main__':
	input_list = [2, 5, 8, 14, 18, 23, 29, 32]
	print binary_search(input_list, 5)
	print binary_search(input_list, 24)
