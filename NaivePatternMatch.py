

def patternMatch(s,p):

	M = len(s)
	N = len(p)

	#move index i by 1 along main string
	for i in range(M-N+1):

		j = 0


		while(j < N):

			#if there is a mismatch, then stop comparing at current index, move i along by 1
			if (s[i+j] != p[j]):
				break

			#otherwise, move j along to continue pattern matching 
			j+= 1

		#if j == N, then we reached the end of the pattern and it is a match at current index i
		if (j == N):

			print("pattern found at index ", i)



if __name__ == '__main__':

	s = "AABAACAADAABAAABAA"
	p = "AABA"

	patternMatch(s,p)

	

