# John Miller
# CS 315
# Homework 8

import random

# selection sort
def selection(array, count):
	j = 0

	while(j != len(array)):
		for i in range(j, len(array)):
			if(array[i] < array[j]):
				array[j], array[i] = array[i], array[j]
			count.append(1)
		j = j + 1
	return array

# insertion sort
def insertion(array, count):
	
	for i in range(1, len(array)):
		k = i - 1
		x = array[i]

		while (k >= 0) and (x < array[k]):
			array[k + 1] = array[k]
			k = k - 1
		count.append(1)

		array[k + 1] = x

	return array

# quick sort with random pivot 
def quick1(array, count):
	pivot = random.choice(array)
	less = []
	equal = []
	greater = []

	if (len(array) <= 50):
		return insertion(array, count)

	else:
		for i in range(0, len(array)):
			if array[i] < pivot:
				less.append(array[i])
			elif array[i] == pivot:
				equal.append(array[i])
			elif array[i] > pivot:
				greater.append(array[i])
			count.append(1)

	return quick1(less, count) + equal + quick1(greater, count)

# quick sort with pivot as first number of list
def quick2(array, count):
	pivot = array[0]
	less = []
	equal = []
	greater = []

	if (len(array) <= 50):
		return insertion(array, count)

	else:
		for i in range(0, len(array)):
			if array[i] < pivot:
				less.append(array[i])
			elif array[i] == pivot:
				equal.append(array[i])
			elif array[i] > pivot:
				greater.append(array[i])
			count.append(1)

	return quick1(less, count) + equal + quick1(greater, count)

# merge sort
def mergesort(array, count):

	result = []
	if len(array) < 2:
		return array

	middle = int(len(array)/2)
	y = mergesort(array[:middle], count)
	z = mergesort(array[middle:], count)

	i = 0
	j = 0

	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1
		count.append(1)

	result += y[i:]
	result += z[j:]

	return result

def main():
	
	sort = []
	sort_input = ''
	count = []

	print("Press 1 for selection sort.")
	print("Press 2 for insertion sort.")
	print("Press 3 for quicksort with random pivot.")
	print("Press 4 for quicksort with first index as pivot.")
	print("Press 5 for mergesort.")

	selection_input = input("Your selection: ")
	print("")
	
	try:
		while True:
			sort_input = int(input("Please input positive numbers (Enter to quit): "))
			sort.append(sort_input)
	except SyntaxError:
		pass

	if (selection_input == 1):
		print(selection(sort, count))
		print "Count = ", len(count)

	if (selection_input == 2):
		print(insertion(sort, count))
		print "Count = ", len(count)

	if (selection_input == 3):
		print(quick1(sort, count))
		print "Count = ", len(count)

	if (selection_input == 4):
		print(quick2(sort, count))
		print "Count = ", len(count)

	if (selection_input == 5):
		print(mergesort(sort, count))
		print "Count = ", len(count)
main()
