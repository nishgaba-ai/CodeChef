#!/usr/bin/env/python
import sys
import math
from sys import stdin, stdout
import itertools


def main():
	T = int(stdin.readline().split()[0])

	for i in range(T):
		N = [int(x) for x in stdin.readline().split()[0]]
		if (6 in N):
			for i in range(5,10):
				if(i in N and i!=6):
					
					stdout.write(unichr(int(str(6)+str(i))))
				elif (i==6):
					if(N.count(6)>1):
						stdout.write(unichr(66))
		if(7 in N):
			for i in range(0,10):
				if(i in N and i!=7):
					stdout.write(unichr(int(str(7)+str(i))))
		
				elif (i==7):
					if(N.count(7)>1):
						stdout.write(unichr(77))
		
		if(8 in N):
			for i in range(0,10):
				if(i in N and i!= 8):
					stdout.write(unichr(int(str(8)+str(i))))
				elif (i==8):
					if(N.count(8)>1):
						stdout.write(unichr(88))
					
		
		if(9 in N and 0 in N):
			stdout.write(unichr(str(90)))  
		stdout.write("\n")
		
		
if __name__=="__main__":
	main()
