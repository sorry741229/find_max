def find_max(a_list):
	x = a_list
	y = 0
	for a in x :
		if a > y:
			y = a
		else:
			continue
	return y


print(find_max([1, 2, 3]))
print(find_max([1, -1, -5]))
print(find_max([]))