# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively

def first_string(strlist):
    if strlist is None:                             # Base case is there is nothing in strlist return none
        return None
    restlist = first_string(strlist.rest)            # recursivly move down the list until and compar then returing the samllist
    if restlist is None:                             # if the next value in the list of node is non the return the vallue befor it
        return strlist.value
    if strlist.value < restlist:                     # compair the current smalist value to the curent list value, if it is smaller make it the new smallist vale uthermist retun the current value
        return strlist.value
    else:
        return restlist



# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively

def split_list(strlist):
    vowel = 'aeiouAEIOU'                                                                #a list of all the vawels to check through
    consonant = 'bcdfghjklmnpqrstvwxzyBCDFGHJKLMNPQRSTVWXZY'                            #a list of all the consenents to check through
    if strlist is None:                                                                 # Base case is there is nothing in strlist retuen a tuple with three nones
        return (None, None, None)
    if strlist.value is None:                                                           # Base case if the fist value ofn the list is none
        return (None, None, None)
    tupel_list = split_list(strlist.rest)                                               # recursivly move down the list until and return a tuple of lists
    if strlist.value[0] in vowel:                                                       # check if the curent list value starts with a vowle is so add it to the first entry on the tupal
        return (Node(strlist.value, tupel_list[0]), tupel_list[1], tupel_list[2])
    if strlist.value[0] in consonant:                                                    # check if the curent list value starts with a consanent is so add it the second entry on the tupal
        return (tupel_list[0], Node(strlist.value, tupel_list[1]), tupel_list[2])
    return (tupel_list[0], tupel_list[1], Node(strlist.value, tupel_list[2]))            # if not a vale of a concanent add it the therid entry on the tupal

