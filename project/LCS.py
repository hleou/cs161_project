import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

def get_path_mod(AA,B,indx,p_lo,p_hi):
	m = len(AA) / 2
	n = len(B)
	i,j = m+indx,n

	path = np.zeros((2,n+1))
	path[0][j] = i
	path[1][j] = i

	while i>indx and j>0:
		if AA[i-1] == B[j-1] and (i-1) >= p_hi[0][j-1] and (i-1) <= p_lo[1][j-1]: # move diagonal
			i -= 1
			j -= 1
			path[0][j] = i
			path[1][j] = i

		elif arr[i-1][j] > arr[i][j-1] and (i-1) >= p_hi[0][j] and (i-1) <= p_lo[1][j]: # move up, better option
			i -= 1
			path[0][j] = i

		else: # move left, better option
			j -= 1
			path[0][j] = i
			path[1][j] = i
			
	if i > indx: # moved all the way left
		path[0][0] = indx

	if j > 0: # moved all the way up
		path[0][path[0]==0] = indx
		path[1][path[1]==0] = indx

	return path

def get_path_reg(A,B):
	m = len(A)
	n = len(B)
	i,j = m,n

	path = np.zeros((2,n+1))
	path[0][j] = i
	path[1][j] = i

	while i>0 and j>0:
		if A[i-1] == B[j-1]: # move diagonal
			i -= 1
			j -= 1
			path[0][j] = i
			path[1][j] = i

		elif arr[i-1][j] > arr[i][j-1]: # move up
			i -= 1
			path[0][j] = i

		else: # move left
			j -= 1
			path[0][j] = i
			path[1][j] = i

	return path

def LCS_mod(A,B,AA,indx,p_lo,p_hi,p):
	m = len(A)
	n = len(B)

	for i in range(indx,indx+m+1):
		arr[i] = 0

	leftColCounter = 1

	for i in range(indx+1,indx+m+1): # refill the area from (mXn) region w/ left, top corner (m+indx,0)
		for j in range(leftColCounter,n+1):

			if p_lo[1][j] == i:
				leftColCounter += 1

			if AA[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i][j-1],arr[i-1][j])

			if i < p_hi[1][j]:
				break

	p[indx] = get_path_mod(AA,B,indx,p_lo,p_hi)

	return arr[m+indx][n] # return tuple (lcs, path, lcs length)



def LCS_reg(A,B,path): #path is whether or not you want the retraced path
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
	if path:
		path = get_path_reg(A,B)
		return (path,arr[m][n]) # return tuple (lcs, path, lcs length)
	else: 
		return arr[m][n] # return lcs length


def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		A,B = l.split()
		print LCS_reg(A,B,False)
	return

if __name__ == '__main__':
	main()
