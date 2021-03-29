"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print (item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    odd_index_nums = []
    for index, num in enumerate(items):
        if index % 2 != 0:
            odd_index_nums.append(num)
    return odd_index_nums


def print_as_numbered_list(items):
    for index, num in enumerate(items):
        print(f'{index+1}. {num}')


def get_range(start, stop):    
    nums = []
    for i in range(start, stop):
        nums.append(i)
        i +=1
    return nums


def censor_vowels(word):
    letters = []
    vowels=['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowels:
            letters.append('*')
        else:
            letters.append(char)
    return "".join(letters)
            


def snake_to_camel(string):
    camel_case = []
    words = string.split('_')
    for word in words:
        camel_case.append(word.title())
    return ''.join(camel_case)
    

def longest_word_length(words):
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest = word
    return len(longest)



def truncate(string):

    result=[]
    for char in string:
        if len(result)==0 or char != result[(len(result)-1)]:
            result.append(char)
    return ''.join(result)
        
    


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            if parens > 0:
                return False

    return parens == 0


def compress(string):
    curr_char = ''
    compressed = []
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char     
            char_count = 0

        char_count += 1
        
    compressed.append(curr_char)
    
    if char_count > 1:
        compressed.append(str(char_count))
    return ''.join(compressed)


