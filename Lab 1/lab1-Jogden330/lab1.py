# CPE 202 Lab 1

# Data definitions:

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Signature: Maybe_List -> Maybe_integer
# Purpose: Find the index of the largest number
def max_list_iter(int_list):
    if int_list is None:
        raise ValueError
    if not int_list:
        return None

    maxNum = int_list[0]
    for i in range(1, len(int_list)):
        if int_list[i] > maxNum:
            maxNum = int_list[i]
    return maxNum


#
#  '''Finds the max of a list of numbers and returns the value (not the index)
# If int_list is empty, returns None. If list is None, raises ValueError'''


# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list 
def reverse_list(int_list):
    if int_list is None:
        raise ValueError
    if not int_list:
        return []
    rev_list = [None] * len(int_list)
    for i in range(len(int_list)):
        rev_list[i] = int_list[-i - 1]
    return rev_list

    #  '''Returns the reverse of the input list, but does not mutate the input list
    # If list is None, raises ValueError'''


# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
    if int_list is None:
        raise ValueError



    for i in range(len(int_list) // 2):

        (int_list[i], int_list[-i - 1]) = (int_list[-i - 1], int_list[i])

    return None


    #  '''Reverses a list, modifying the input list
    # If list is None, raises ValueError'''
    #  pass


# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list using recursion
def reverse_rec(int_list):  # must use recursion3
    if int_list is None:
        raise ValueError
    elif not int_list:
        return []

    elif len(int_list) == 1:
        return int_list
    else:
        return [int_list[-1]] + reverse_rec(int_list[:-1])




#  '''Returns the reverse of the input list, but does not mutate the input list.
# May NOT mutate the original list. If list is None, raises ValueError'''
#  pass
