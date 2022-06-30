# Divide and Conquer algorithms that processes integer sequences

All three programs have the same input and output format. The input consist of two white-space separated sequence S1 and S2 of positive integers (each sequence is given on one line). The length of S1 is n1 and the length of S2 is n2; note these are not necessarily the same. The output will be a n2 lines, each consisting of a single integer. For the following three problems we index elements in each sequence start at 0 and end at n1 −1 or n2 −1.


## Problem 0:
This simple warm-up problem will check if the algorithm can read the input correctly (from stdin). For each integer x in S2, output/print (to stdout) the value n1 + x.

### Sample Input:
```
1 3 0 2 3 4
3 2 3 4
```

### Sample Output:
```
9
8
9
10
```

## Problem 1:
We assume the first input sequence S1 is sorted. Determine the highest index each item x in S2 within S1. If x does not appear, then output −1 for that case. It uses a traditional O(log n1) binary-search function, called n2 times.

### Sample Input:
```
1 3 10 21 23 23 24
3 12 23 24
```
### Sample Output:
```
1
-1
5
6
```

## Problem 2:
This is the same as Problem 1, except the input S1 is a sorted and rotated array. That is, S1 = s0,s1,s2,...,si,...,sn1−1, where for some 0 < i < n, si is the smallest element, and modulo n, sj ≤sj+1 forallj̸=i−1.

### Sample Input:
```
23 24 1 3 10 21 23
3 12 23 24
```
### Sample Output:
```
3
-1
6
1
```
