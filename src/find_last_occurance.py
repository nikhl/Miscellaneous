def find_last_occurance(s,t):
	if s.find(t) == -1:
		return -1
	else:
		index = -1
		while s.find(t,index+1) != -1:
			index = s.find(t,index+1)
	return index

# various test cases
print find_last_occurance('aaaa', 'a')
#>>> 3

print find_last_occurance('aaaaa', 'aa')
#>>> 3

print find_last_occurance('aaaa', 'b')
#>>> -1

print find_last_occurance("111111111", "1")
#>>> 8

print find_last_occurance("222222222", "")
#>>> 9

print find_last_occurance("", "3")
#>>> -1

print find_last_occurance("", "")
#>>> 0