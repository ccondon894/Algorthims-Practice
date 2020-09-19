

#create array to find longest prefix that is also a suffix at each index in pattern
def make_array(pattern):

	m = len(pattern)

	# make pointers to compare 
	i=0
	j=1

	
	#longest prefix at index 0 is always 0
	lps = [None]*m
	lps[0] = 0


	while j < m:

		#if match, then advance i, store value of i at index j, and advance j
		if pattern[i] == pattern[j]:
			i+= 1
			lps[j] = i
			j+= 1

		# if i is still at index 0, then assign 0 at lps[j] and advance j
		elif i == 0:

			lps[j] = 0
			j += 1

		#retract i, notice that j is not retracted! 
		#loop will continue at indexes j and i-1.
		#If mismatched again, then continue until i = 0 again
		else:

			i = lps[i-1]

	print(lps)
	return lps

def patternMatch(p,s):

	lps = make_array(p)

	#pointer for pattern
	i = 0
	#pointer for string
	j = 0
	# m = length of string, n = length of pattern
	m = len(s)
	n = len(p)

	while i < n and j < m:

		#if last char in pattern matches, then pattern found
		if p[i] == s[j] and i == n - 1:

			print("pattern found at index: ", j-n+1 )

			i = 0
			j += 1

		#if match, advance i and j
		elif p[i] == s[j]:
			
			j += 1
			i += 1

		else:

			if i != 0:

				i = lps[i-1]

			else: 

				j += 1


s = "AABAACAADAABAAABAA"
p = "AABA"

patternMatch(p,s)