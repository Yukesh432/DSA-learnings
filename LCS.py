# Longest Common Subsequence Problem
"""
The problem involves finding the longest subsequence common to all sequences in a set of sequences
(often just two). A subsequence is defined as a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

The most common method to solve the LCS problem is through dynamic programming because the problem exhibits both 
optimal substructure and overlapping subproblems. The idea is to build a 2D table 
L where L[i][j] represents the length of the LCS of the sequences X[1..i] and Y[1..j]
"""