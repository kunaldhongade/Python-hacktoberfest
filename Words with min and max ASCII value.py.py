# Python implementation of the above approach

# Function to find the average
# of ASCII value of a word
def averageValue(s):

	# Stores the sum of ASCII
	# value of all characters
	sumChar = 0

# Traverse the string
	for i in range(len(s)):

		# Increment sumChar by ord(s[i])
		sumChar += ord(s[i])

	# Return the average
	return sumChar // len(s)

# Function to find words with maximum
# and minimum average of ascii values
def printMinMax(string):

	# Stores the words of the
	# string S separated by spaces
	lis = list(string.split(" "))

	# Stores the index of word in
	# lis[] with maximum average
	maxId = 0

	# Stores the index of word in
	# lis[] with minimum average
	minId = 0

	# Stores the maximum average
	# of ASCII value of characters
	maxi = -1

	# Stores the minimum average
	# of ASCII value of characters
	mini = 1e9

	# Traverse the list lis
	for i in range(len(lis)):

		# Stores the average of
		# word at index i
		curr = averageValue(lis[i])

		# If curr is greater than maxi
		if(curr > maxi):

			# Update maxi and maxId
			maxi = curr
			maxId = i

		# If curr is lesser than mini
		if(curr < mini):

			# Update mini and minId
			mini = curr
			minId = i

	# Print string at minId in lis
	print("Minimum average ascii word = ", lis[minId])

	# Print string at maxId in lis
	print("Maximum average ascii word = ", lis[maxId])


# Driver Code

S = input("Enter the string:")
printMinMax(S)
