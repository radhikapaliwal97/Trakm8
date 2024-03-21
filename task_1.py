"""Task 1
Consider a sequence of integers A1, A2, ... for which An = A(n-1) + A(n-2) for all n
&gt; 2. You are given the first two elements of the sequence A1 and A2, and the index
n.
Write a function to output the n-th element of the sequence. The function will take
a single argument consisting of a single string which contains integers A1, A2 and n
separated by single spaces.
Example: Input &#39;1 2 5&#39;
Output 8"""

def sequence_element(input_string):
    # spliting values of a1 (first term), a2 (second term), and n (desired position) from the input string
    a1, a2, n = map(int, input_string.split())
    seq = [a1, a2]

    # Looping to generate the sequence up to the nth position
    for _ in range(2, n):
        # Appending the next term to the sequence by adding the last two terms
        seq.append(seq[-1] + seq[-2])
    
    # Returning the nth element of the sequence
    return seq[-1]

print(sequence_element('1 2 5'))