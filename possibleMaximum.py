"""Problem Statement

You are given a set S = {1, 2, 3,…,N}. Find two integers A and B (A<B) from the set S such that the value of A & B is the maximum possible and less than the given integer K. In this case, & represents the operator bitwise AND.

Input Format

The first line of input is T: total number of test cases. Each of the next T lines contains two space separated integers N and K.

Constraints

1≤T≤103
2≤N≤103
2≤K≤N
Output Format

Output the possible maximum value of A & B for each test case on separate line.

Sample Input

3
5 2
8 5
2 2
Sample Output

1
4
0
Explanation

N = 5, K = 2

S = {1, 2, 3, 4, 5}

All the possible values of A and B are:

A = 1, B = 2. So, A & B = 0
A = 1, B = 3. So, A & B = 1
A = 1, B = 4. So, A & B = 0
A = 1, B = 5. So, A & B = 1
A = 2, B = 3. So, A & B = 2
A = 2, B = 4. So, A & B = 0
A = 2, B = 5. So, A & B = 0
A = 3, B = 4. So, A & B = 0
A = 3, B = 5. So, A & B = 1
A = 4, B = 5. So, A & B = 4
So, the possible maximum value of A & B which is less than K = 2 is 1.

"""


import itertools

T = int(raw_input())
test_case = []

for i in range(T):
    test = raw_input().split()
    test_case.append(tuple(test))

def func(tc):
    N = int(tc[0])
    K = int(tc[1])
    s = set(xrange(1,N+1))
    combo = itertools.combinations(s,2)
    maximum = 0
    
    for i in combo:
        bitand = i[0]&i[1]
        if maximum < bitand < K:
            maximum = bitand
            
    return maximum

for test in test_case:
    output = func(test)
    print output
