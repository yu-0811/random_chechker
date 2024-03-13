import sys,math
if len(sys.argv) == 2: sys.stdin = open(sys.argv[1])
from collections import defaultdict,deque
from itertools import combinations,permutations,accumulate,product
from bisect import bisect,bisect_left,bisect_right
from heapq import heappop,heappush,heapify
#from sortedcontainers import SortedList,SortedSet
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def ms(): return map(int, input().split())
def li(): return list(map(int,input().split()))
#////////////////////////////////////
print(-11)

