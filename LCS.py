# Longest Common Subsequence Problem
"""
The problem involves finding the longest subsequence common to all sequences in a set of sequences
(often just two). A subsequence is defined as a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

The most common method to solve the LCS problem is through dynamic programming because the problem exhibits both 
optimal substructure and overlapping subproblems. The idea is to build a 2D table 
L where L[i][j] represents the length of the LCS of the sequences X[1..i] and Y[1..j]
"""

# a simple solution would be to generate a substring of given strings and check for the match of those
# substring. Those substring that matches and has of max length , that will be the LCS.

def generate_substring(ipstring):
    subst= []

    for i in range(len(ipstring)):
        subStr= ""

        for j in range(i, len(ipstring)):
            subStr+=(ipstring[j])
            subst.append(subStr)
            
    return subst

substring1= generate_substring("zxabcdezy")
substring2= generate_substring("yzabcdezx")

matched_strings= []
for i in substring1:
    for j in substring2:
        if i==j:
            matched_strings.append(i)

max_len= -1
max_lenth_element= ''
for element in matched_strings:
    if len(element)> max_len:
        max_len= len(element)
        max_len_element= element
# print(substring1)
# print(substring2)
print(matched_strings)
print(max_len_element)
print(max_len)
