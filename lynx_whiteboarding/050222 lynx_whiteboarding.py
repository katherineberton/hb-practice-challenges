#ZERO OUT MATRIX -------------------------------------------------------- KAT

#link: https://fellowship.hackbrightacademy.com/materials/challenges/zero-matrix/index.html

#take every row and column that contains a 0 and zero out the entire row and column

#Write a function given an nxm matrix that changes all entire rwos and columns to 0 if there is a 0 in that row or column at all
#the implementation of this matrix is a list of lists
#do it in place

# n = 3, m = 4

# A B C D
# E F 0 H
# I J K L

# A B 0 D
# 0 0 0 0
# I J 0 L

#[ ['A', 'B', 'C', 'D'], ['E', 'F', 0, 'H'], ['I', 'J', 'K', 'L'] ]

#this list is going to be a list of n elements, each element being a list of m elements
#to traverse the rows, we can loop over the entire list (range 0 to n-1)
#to traverse the columns, we loop over the indices of each element in the list (indices 0 to m-1)

# dictionary containing kvp for # of rows and # of columns in the list
# variable for the original state of the list (so that i can make changes to the original, and not turn the whole board to 0s)

#rows first (for each element in the overarching list, if that element contains 0, reassign each element to 0)
#then columns (for each index in range 0 to m - 1, over all lists, if there is 0 in there, reassign the value of each list at that index to 0)

#function definition (mtx):


#mtx_dimensions = {
    #rows: count of rows (length of the given matrix)
    #columns: count of columns (length of the first element in the given matrix)
#}

#mtx_columns = {
    
#}

#for i in range 0 to number of columns:
    #mtx_columns at that index = []

#in all of the elements in th eoverarching list enumerated:
    #mtx_columns at index.append (element)


#original_mtx = the state of the parameter as it's passed in


#row reassignment
#for each element in mtx:
    #if that element contains 0:
        #for each element in that element:
            #reassign element to 0


#column reassignment
#for keys, values in the dicitonary.items:
    #if values contains 0
        #loop over each row in the original list and reassign the value of the element at that index to 0

# for row in test_list:
#     print(row)

def zero_matrix(matrix):
    """For each 0 in the matrix, changes in place all others in that zero's row and column to 0"""

    #num of rows and columns in the given matrix
    dimensions = {
        'rows': len(matrix),
        'columns': len(matrix[0])
    }

    #setup for list of columns in the matrix (it's already given in the format of a list of rows)
    mtx_columns = {}

    #set up the indices in the list of columns dict
    for i in range(dimensions['columns']):
        mtx_columns[i] = []

    #populate the indices in the list of columns dict
    for row in matrix:
        for i, el in enumerate(row):
            mtx_columns[i].append(el)

    #row reassignment
    for row in matrix:
        if 0 in row:
            for i, _ in enumerate(row):
                row[i] = 0

    #column reassignment
    for k, v in mtx_columns.items():
        if 0 in v:
            for row in matrix:
                row[k] = 0

    return matrix


#ANAGRAM OF PALINDROME -------------------------------------------------------- YOLINE

#link: https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html

#take in string, if it is an anagram of palindrome return True. palindrom == same back and forth, ana = same letters as somethign else. 

# bcbca --> bcacb 
# {
    # 'b' : 2, 
    # 'c': 2
    # 'a': 1
# } TRUE
    
# bccbca 
# {
    # 'b' : 2, 
    # 'c': 3
    # 'a': 1
# } FALSE more than 1 char @ > value%2 !=0 instance, false?

# arceace
# {
    # 'a': 2, 
    # 'r': 1, 
    # 'c': 2, 
    # 'e': 2
# } TRUE

 # "aab"
# {
    # 'a': 2, 
    # 'b': 1, 
# } TRUE 

# "ab"
# {
    # 'a': 1, 
    # 'b': 1, 
# } FALSE more than 1 char @ 1 instance, false?
    
#  space is a char, and capitals distinct
#
# dictionary of char counts,
#set up some test dictionaries of char counts of all these examples
#figure out what they all have in common

# PSEUDO
#set up a dictionary char count
    #iterate through string
    #create dictionary by adding in there

#w/ established char count, need to see if there are values over 1, that's is odd (not even!)

#odd_char_count == 0
    #iterate through dict values, if value is %2 !=0, then +1 to odd_char_count
    # THE SECOND is goes to two, return false

#else return True

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("arceace") -> racecar
    True

    >>> is_anagram_of_palindrome("aab") -> aba
    True

    >>> is_anagram_of_palindrome("ab") -> no way to rearrange this
    False
    
    """
    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    odd_char_count = 0

    for value in char_count.values(): 
        if value % 2 != 0: 
            odd_char_count += 1
            
        if odd_char_count == 2: 
            return False

    return True
