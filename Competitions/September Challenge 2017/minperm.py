#!/usr/bin/env/python
import sys
import math
from sys import stdin, stdout

def main():
	T = int(stdin.readline().split()[0])

	for i in range(T):
		N = int(stdin.readline().split()[0])
		if(N%2 == 0):
			for j in range(N/2):
				stdout.write(str(2*j+2) + " "+str(2*j+1)+" ")
		else:
			if N == 3:
				stdout.write("2 3 1")
			else:
				for j in range((N-3)/2):
					stdout.write(str(2*j+2) + " "+str(2*j+1)+" ")
				stdout.write(str(2*j+4)+" "+str(2*j+5)+" "+str(2*j+3))
			
		print("\n")
if __name__=="__main__":
	main()
