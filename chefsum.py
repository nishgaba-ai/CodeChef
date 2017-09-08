#!/usr/bin/env/python
import sys
import math
from sys import stdin, stdout

def main():

	T = int(stdin.readline().split()[0])
	for i in range(T):
		arr = [0]
		N = int(stdin.readline().split()[0])
		hold = stdin.readline().split()
		for j in range(N):
			arr.append(int(hold[j])+arr[j])		
		min = 1
		check = arr[1] + arr [-1]
		for j in range(2,N+1):
		
			if (arr[j]+(arr[-1]-arr[j-1])) < check :
				check = arr[j]+(arr[-1]-arr[j-1])
       				min = j

		stdout.write(str(min)+"\n")
		arr=[]
if __name__=="__main__":
	main()		
