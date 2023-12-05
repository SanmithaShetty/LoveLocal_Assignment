
def chars_to_add(string):
	n = len(string)
	l = 0#start 
	r = n - 1#end of string being considered
	str1=""
	res = 0#keeps track of characters to be added
	while l < r: # While left lesser than right
		if string[l] == string[r]: # If the characters at the extremes are equal
			l += 1 # move the start right one char
			r -= 1 # Move the end left one char
		else:
			res += 1 # increase by one number of chars to be added
			str1=string[r]+str1
			l = 0 # Reset the start
			r = n - res - 1 # Reset the number
			
	return str1+string # Return the count of characters to be added

#test
string = "abcd"
print(chars_to_add(string))

