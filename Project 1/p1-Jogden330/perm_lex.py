# takes in a string of zero or more  uniquelower-case letters in alphabetical order and returns a list of all the permutations of that string
# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):


    if not str_in:
        return []                                                                               #if the input string is empty return it as a empty list
    elif len(str_in) == 1:
        return [str_in]                                                                         #if the input string is 1 character long return that charicter as a list
    else:
        appended_perm_list = []                                                                 #initalizes the appable list
        for char in str_in:                                                                     #loops through each charicter in the input string
            new_str = str_in.replace(char, '')                                                  #removes select charicter from input string to make a simpler one
            perm_list = perm_gen_lex(new_str)                                                   #recursivly creates all permutations of the simpler string and stores them in a list
            appended_perm_list = appended_perm_list + [char + string for string in perm_list]   #appends the premuteded string to an appebded list and adds the removed caricter to front each perutatuon

        return appended_perm_list


# a StrList is one of
# - None, or
# - Node(string, StrList)

class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

