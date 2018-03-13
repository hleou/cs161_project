import sys
import numpy as np
import LCS
from LCS import LCS_reg
from LCS import LCS_mod
import time


def FindShortestPaths(A,B,AA,p,l,u,bestSoFar):
	if u-l <= 1:
		return
	mid = (l+u)/2

	length = LCS_mod(A,B,AA,mid,p[u],p[l],p)
	if length > bestSoFar[0]:
		bestSoFar[0] = length

	FindShortestPaths(A,B,AA,p,l,mid,bestSoFar)
	FindShortestPaths(A,B,AA,p,mid,u,bestSoFar)

def CLCS(A,B):
	m,n = len(A),len(B)

	path,length = LCS_reg(A,B,True)

	p = (m+1)*[np.zeros((2,n+1),dtype=int)]

	p[0] = path
	p[m] = path+m

	bestSoFar = [length]
	AA = A+A

	FindShortestPaths(A,B,AA,p,0,m,bestSoFar)
	return bestSoFar[0]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python CLCSFast.py < input`')
	
	for l in sys.stdin:
	 	A,B = l.split()
	 	start_time = time.time()
	 	print CLCS(A,B)
	 	print("--- %s seconds ---" % (time.time() - start_time))
	return

if __name__ == '__main__':
	main()