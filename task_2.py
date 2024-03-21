"""Task 2
You are given an array of strings. Each array element contains one or several words
separated with single spaces.
Write a function to reverse the order of the words in each element of the array.
Additionally where a word contains a sequence of the same character, replace the
sequence with * characters of the same length.
Example: Input ['Hello World', 'Bye World', 'Useless World']
Output ['World He**o', 'World Bye', 'World Usele**']"""

def reverse_and_replace_word(words):
    match_count = 1
    # Add a space at the end to handle the last word
    words = words + " " 
    my_string = words[0]
    for wrd in range(1, len(words)):
        # Check if the current character matches the previous one
        if words[wrd-1] == words[wrd]:
            # Increment the match count if it's a consecutive match
            match_count += 1
        else:
            if match_count > 1:
                # Replace matched character with '*'
                my_string = my_string[:-1]+"*"*match_count  
            # Reset match count for the new character           
            match_count = 1
            # Return the result string without the extra space at the end
            my_string += words[wrd]
    
    return my_string[:-1]
     

def reverse_and_replace(arr):  
    reverse_list = []
    for string in arr:
        rev_list = []
        words = string.split()[::-1]
        for strs in words:         
            # Reverse and replace each word   
            rev_list.append(reverse_and_replace_word(strs))
        # Join the reversed and replaced words and append to the result list
        reverse_list.append(" ".join(rev_list))
    return reverse_list
     

input_array = ['Hello World', 'Bye World', 'Useless World']
output_array = reverse_and_replace(input_array)
print(output_array)
