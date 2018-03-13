import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

#def get_path_mod(AA,B,indx,p_lo,p_hi):
def get_path_mod(AA,B,indx,p_lo,p_hi,b_lo,b_hi):
	m = len(AA) / 2
	n = len(B)
	i,j = m+indx,n

	path = np.zeros((2,n+1))
	path[0][j] = i
	path[1][j] = i
	bound = np.zeros((2,2*m+1))
	bound[0][i] = j
	bound[1][i] = j

	while i>indx and j>0:
		if AA[i-1] == B[j-1] and (i-1 <= p_hi[1][j-1] and i-1 >= p_lo[0][j-1]): # move diagonal
			i -= 1
			j -= 1
			path[0][j] = i
			path[1][j] = i
			bound[0][i] = j
			bound[1][i] = j
		elif arr[i-1][j] > arr[i][j-1] and (i-1 <= p_hi[1][j] and i-1 >= p_lo[0][j]): # move up, better option
			i -= 1
			path[0][j] = i
			bound[0][i] = j
			bound[1][i] = j
		else: # move left, better option
			j -= 1
			path[0][j] = i
			path[1][j] = i
			bound[0][i] = j
			
	if i > indx: # moved all the way left, so move up until you are at (index+1,1)
		path[0][0] = indx

	if j > 0: # moved all the way up, so move left until you are at (index+1,1)
		path[0][path[0]==0] = indx
		path[1][path[1]==0] = indx
		bound[1][indx] =  j

	return path,bound

def get_path_reg(A,B):
	m = len(A)
	n = len(B)
	i,j = m,n

	path = np.zeros((2,n+1))
	path[0][j] = i
	path[1][j] = i
	bound = np.zeros((2,m+1))
	bound[0][i] = j
	bound[1][i] = j

	while i>0 and j>0:
		if A[i-1] == B[j-1]: # move diagonal
			i -= 1
			j -= 1
			path[0][j] = i
			path[1][j] = i
			bound[0][i] = j
			bound[1][i] = j
		elif arr[i-1][j] > arr[i][j-1]: # move up
			i -= 1
			path[0][j] = i
			bound[0][i] = j
			bound[1][i] = j
		else: # move left
			j -= 1
			path[0][j] = i
			path[1][j] = i
			bound[0][i] = j

	bounds1 = np.zeros((2,m+1))
	bounds2 = np.zeros((2,m+1))

	if j > 0: # moved all the way up, so move left until you are at (index+1,1)
		bound[1][0] =  j

	return path,bound

#def LCS_mod(A,B,AA,indx,p_lo,p_hi,p):
def LCS_mod(A,B,AA,indx,p_lo,p_hi,p,b_lo,b_hi,b):
	m = len(A)
	n = len(B)

	#for i in range(indx,indx+m+1):
		#for j in range(1:n+1):
			#arr[i][j] = 0
	for j in range(1,n+1):
		arr[indx][j] = 0

	for i in range(indx+1,indx+m+1): # refill the area from (mXn) region w/ left, top corner (m+indx,0)
		for j in range(1,n+1):

			if AA[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i][j-1],arr[i-1][j])
	if p:
		#p[indx] = get_path_mod(AA,B,indx,p_lo,p_hi)
		p[indx],b[indx] = get_path_mod(AA,B,indx,p_lo,p_hi,b_lo,b_hi)
		return arr[m+indx][n] # return tuple (lcs, path, lcs length)
	else: 
		return arr[m+indx][n] # return lcs length


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
		#path,bound = get_path_reg(A,B)
		path,bound = get_path_reg(A,B)
		return (path,bound,arr[m][n]) # return tuple (lcs, path, lcs length)
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
