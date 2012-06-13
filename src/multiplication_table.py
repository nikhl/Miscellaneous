# Take as input a number and print all the multiplications from 1 upto that number
def print_multiplication_table(n):
	i = 1
	while i<=n:
		j = 1
		while j<=n:
			print '%d * %d = %d' % (i,j,(i*j))
			j = j+1
		i = i+1


# test cases
print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9
