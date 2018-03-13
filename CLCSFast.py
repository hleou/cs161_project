import sys
import numpy as np
import LCS
from LCS import LCS_reg
from LCS import LCS_mod
import time


def FindShortestPaths(A,B,AA,p,b,l,u,bestSoFar):
	if u-l <= 1:
		return
	mid = (l+u)/2

	length = LCS_mod(A,B,AA,mid,p[u],p[l],p,b[l],b[u],b)
	if length > bestSoFar[0]:
		bestSoFar[0] = length

	FindShortestPaths(A,B,AA,p,b,l,mid,bestSoFar)
	FindShortestPaths(A,B,AA,p,b,mid,u,bestSoFar)

def FindShortestPaths1(A,B,AA,p):
	m = len(A)
	q = int(np.log2(m))
	for j in range(1,q+1):
		for k in range(1,2**(j-1)+1):
			mid = (2*k-1)*m/(2**j)
			up = (2*k-2)*m/(2**j)
			lo = (2*k)*m/(2**j)
			p[mid], length = LCS_mod(A,B,AA,mid,p[lo],p[up],True)

def CLCS(A,B):
	m,n = len(A),len(B)

	path,bound,length = LCS_reg(A,B,True)

	p = (m+1)*[np.zeros((2,n+1),dtype=int)]
	b = (m+1)*[np.zeros((2,2*m+1),dtype=int)]

	p[0] = path
	p[m] = path+m
	b[0] = bound
	b[m] = bound

	bestSoFar = [length]
	AA = A+A

	FindShortestPaths(A,B,AA,p,b,0,m,bestSoFar)
	#print p
	return bestSoFar[0]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python CLCSFast.py < input`')
	# print CLCS('ABC','CAB')
	
	for l in sys.stdin:
	 	A,B = l.split()
	 	start_time = time.time()
	 	print CLCS(A,B)
	 	print("--- %s seconds ---" % (time.time() - start_time))
	return

if __name__ == '__main__':
	main()