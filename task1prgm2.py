n = 20
numbers = 1
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(int(numbers), end=" ")
		numbers += 1
	numbers = 1
	print()
