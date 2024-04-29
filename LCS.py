# Longest Common Subsequence Problem
"""
The problem involves finding the longest subsequence common to all sequences in a set of sequences
(often just two). A subsequence is defined as a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

The most common method to solve the LCS problem is through dynamic programming because the problem exhibits both 
optimal substructure and overlapping subproblems. The idea is to build a 2D table 
L where L[i][j] represents the length of the LCS of the sequences X[1..i] and Y[1..j]
"""

# sequence1= ['abc', 'defff', 'ijjkdef']
seq1= ['aababbabca', 'bbababaacaac']

def lcs(x,y):
    # get the length of the strings
    m, n= len(x), len(y)

    # create a 2d array to store lengths of longest common subsequence.
    L= [[0] * (n+1) for i in range(m+1)]

    # build the L[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j ==0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] +1
            else:
                L[i][j]= max(L[i-1][j], L[i][j-1])

            


