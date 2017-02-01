#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
temp_arr=[];
for i in range(n):
    temp_arr.append(arr[n-1])
    n=n-1
print ' '.join([str(x) for x in temp_arr])
