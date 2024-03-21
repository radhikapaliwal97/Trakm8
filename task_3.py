"""Task 3
Given an array of integers, write a function that tests each integer for their
divisibility into 3 and 11 using the below methods.
To see if a number is divisible by 3:
 Add up the digits of its decimal notation
 Check if the sum is divisible by 3
To see if a number is divisible by 11:
 Split its decimal notation into pairs of digits (starting from the right
end)
 Sum the resulting numbers and check if divisible by 11
The function must return a new array containing the results:
- If the integer is divisible by 3, the result is &#39;fizz&#39;
- If the integer is divisible by 11, the result is &#39;buzz&#39;
- If the integer is divisible by both 3 and 11, the result is &#39;fizzbuzz&#39;
- If the integer isn&#39;t divisible by 3 or 11, the result is &#39;baz&#39;

Example: Input [2, 3, 10, 11, 12, 22, 297]

Output ['baz', 'fizz', 'baz', 'buzz', 'fizz', 'buzz', 'fizzbuzz']"""

def fizz_buzz_baz(numbers):
    result = [] # Creating an empty list
    for number in numbers:
        # Calculating the sum of the individual digits of the current number
        digits_sum = sum(int(digit) for digit in str(number))
        # Calculating the sum of pairs of digits in the current number
        pairs_sum = sum([int(str(number)[i-2:i]) if i > 2 else int(str(number)[:i]) for i in range(len(str(number)), 0, -2)])

        # Check if the sum of digits is divisible by 3 and the sum of pairs is divisible by 11 
        if digits_sum % 3 == 0 and pairs_sum % 11 == 0:
            result.append('fizzbuzz')
         # Check if the sum of digits is divisible by 3
        elif digits_sum % 3 == 0:
            result.append('fizz')
        # Check if the sum of pairs of digits is divisible by 11
        elif pairs_sum % 11 == 0:
            result.append('buzz')
        else:
            #If none of the above conditions are matching, add 'baz' to the list
            result.append('baz')
    return result

print(fizz_buzz_baz([2, 3, 10, 11, 12, 22, 297]))