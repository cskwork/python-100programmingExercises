"""
1 point first 2
2 compare
3 highest value bubble to right

"""

#EDIT X
def bubble_sort(list):
	unsorted_until_index = len(list)-1;
	sorted = False
	
	while not sorted:
		sorted = True
		for i in range(unsorted_until_index):
			print('i',i)
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i]
		unsorted_until_index = unsorted_until_index - 1

list = [5,4,3]
bubble_sort(list)
print(list)