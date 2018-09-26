# lps: longest_palindromic_subsequence
# Reference: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
def find_lps(input_string):
	print input_string
	length = len(input_string)
	result_array = [[0 for i in range(length)] for i in range(length)]
	for i in range(length):
		result_array[i][i] = 1
	for len_substring in range(2, length + 1):
		print('len_substring: %s', len_substring)
		for i in range(length - len_substring + 1):
			print('i: %s', i)
			j = i + len_substring - 1
			print('j: %s', j)
			print('input i: %s', input_string[i])
			print('input j: %s', input_string[j])
			if input_string[i] == input_string[j] and len_substring == 2:
				result_array[i][j] = 2
			elif input_string[i] == input_string[j]:
				result_array[i][j] = result_array[i + 1][j - 1] + 2
			else:
				result_array[i][j] = max(result_array[i][j - 1], result_array[i + 1][j])
			print('result_array ij: %s', result_array[i][j])
	print result_array
	return result_array[0][length - 1]


if __name__ == '__main__':
	print find_lps('BBABCBCAB')
