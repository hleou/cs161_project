import sys
from LCS import LCS_reg

def cut(string,k):
	return string[k:]+string[0:k]

def CLCS(A,B):
	m = len(A)
	n = len(B)
	max_len = -float('inf')
	max_lcs = ''
	for k in range(m):
		lcs,path,len_ = LCS_reg(cut(A,k),B,True)
		if len_ > max_len:
			max_len = len_
			max_lcs = lcs
	return (max_lcs, max_len)

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python CLCSSlow.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print CLCS(A,B)
	return

if __name__ == '__main__':
	main()