from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    # '''Evaluates a postfix expression
    #
    # Input argument:  a string containing a postfix expression where tokens
    # are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    # Returns the result of the expression evaluation.
    # Raises an PostfixFormatException if the input is not well-formed
    # DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack(30)                                   #imitalises the stack
    input_str = input_str.split()                       #turns a string into a list of strings
    if len(input_str) == 0:                             #if the imput is empty return error
        raise PostfixFormatException("Empty input")
    else:
        for token in input_str:                         #iterat through each position in the array
            if token == "+":                            #if the tocken is an operator proform the operation matching there simbals on the last two entrys on the stack
                pluse(stack)
            elif token == "-":
                minus(stack)
            elif token == "*":
                multiply(stack)
            elif token == "/":
                divide(stack)
            elif token == "**":
                power(stack)
            elif token == ">>":
                shiftleft(stack)
            elif token == "<<":
                shiftright(stack)
            else:                                       #if the token is not a number save it as an into or a float, if it is an invaled token raise an error
                try:
                        token = int(token)
                        stack.push(token)
                except ValueError:
                        try:
                             token = float(token)
                             stack.push(token)
                        except:
                             raise PostfixFormatException("Invalid token")




        finalValue = stack.pop()                       #return the final value, if the are is leftover data on the stack reaise an error
        if stack.is_empty():
            return finalValue
        else:
            raise PostfixFormatException("Too many operands")


    #Converts an infix expression to an equivalent postfix expression
    #
    # Input argument:  a string containing an infix expression where tokens are
    # space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    # Returns a String containing a postfix expression '''
def infix_to_postfix(input_str):
    RPNexpression = ""                                                      #initalise the string veriable
    stack = Stack(30)                                                       #imitalises the stack
    input_str = input_str.split()                                           #turns a string into a list of strings
    for token in input_str:                                                 # if the token is a ( the push it to the stack
        if token == "(":
            stack.push(token)

        elif token == ")":                                                 # if the token is a ) the pop data of the stack and stor it to a string untel a ( is found. remove the ( from stack
            while not stack.is_empty():
                if stack.peek() == "(":
                    stack.pop()
                    break
                else:
                    RPNexpression = RPNexpression + stack.pop() + " "

        elif token == "+" or token == "-":                                  # if the token is a + or - then pop operaters off the stack tell ( or is empty the push operator tp the stack
            while not stack.is_empty():
                if stack.peek() == "(":
                    break
                else:
                    RPNexpression = RPNexpression + stack.pop() + " "
            stack.push(token)

        elif token == "*" or token == "/":                                   # if the token is a * or / then pop operaters off the stack tell ( or is empty or iconteing a lower prority opewrator the push operator tp the stack
            while not stack.is_empty():
                if stack.peek() == "-" or stack.peek() == "+" or stack.peek() == "(":
                    break
                else:
                    RPNexpression = RPNexpression + stack.pop() + " "
            stack.push(token)

        elif token == "**" or token == ">>" or token == "<<":                # if the token is a ** or >> or << then pop operaters off the stack tell ( or is empty or iconteing a lower prority opewrator the push operator tp the stack
            while not stack.is_empty():

                if stack.peek() == "-" or stack.peek() == "+" or stack.peek() == "*" or stack.peek() == "/" or stack.peek() == "**" or stack.peek() == "(":
                    break
                else:
                    RPNexpression = RPNexpression + stack.pop() + " "
            stack.push(token)


        else:
            RPNexpression = RPNexpression + token + " "                        # if the token is number append it to the string

    while not stack.is_empty():                                                # pop remaing entrys off the stack and append them the string
            RPNexpression = RPNexpression + stack.pop() + " "
    return RPNexpression[:-1]                                                  # return string - one " "

    #Converts a prefix expression to an equivalent postfix expression
    #
    # Input argument:  a string containing a prefix expression where tokens are
    # space separated.  Tokens are either operators + - * / ** >> << or numbers
    # Returns a String containing a postfix expression (tokens are space separated)'''
def prefix_to_postfix(input_str):
    operator = ["+", "-", "*", "/", "**", ">>", "<<"]                            # creat a list of operator to check

    stack = Stack(30)                                                            #imitalises the stack
    input_str = reversed(input_str.split())                                      #turns a string into a list of strings and revers it order

    for token in input_str:                                                      #iterat through each position in the array
        if token in operator:                                                    #if the token is an operator then take the last to entrys in the stack and append them together with the token
            operand1 = (stack.pop())
            operand2 = (stack.pop())
            postfix_srt = operand1 + " " + operand2 + " " + token
            stack.push(postfix_srt)
        else:
            stack.push(token)                                                    #if the token is a number puch it to the stack

    return stack.pop()                                                           #return the last entry on the stack


# Signature: stack -> none
# Purpose: performs a sum of calculation on the last to operand on the stack
def pluse(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    stack.push(operand1 + operand2)
# Signature: stack -> none
# Purpose: performs a difference of calculation on the last to operand on the stack then push that number to the stack
def minus(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    stack.push(operand1 - operand2)
# Signature: stack -> none
# Purpose: performs a product of calculation on the last to operand on the stack  then push that number to the stack
def multiply(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    stack.push(operand1 * operand2)
# Signature: stack -> none
# Purpose: performs a quotient calculation on the last to operand on the stack  then push that number to the stack
def divide(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    if operand2 == 0:
        raise ValueError
    else:
        stack.push(operand1 / operand2)
# Signature: stack -> none
# Purpose: performs a power of calculation on the last to operand on the stack  then push that number to the stack
def power(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    stack.push(operand1 ** operand2)
# Signature: stack -> none
# Purpose: performs a sift left logic calculation on the last to operand on the stack  then push that number to the stack
def shiftleft(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    try:
        stack.push(operand1 >> operand2)
    except:
        raise PostfixFormatException("Illegal bit shift operand")
# Signature: stack -> none
# Purpose: performs a sift right logic calculation on the last to operand on the stack  then push that number to the stack
def shiftright(stack):
    try:
        operand2 = (stack.pop())
        operand1 = (stack.pop())
    except:
        raise PostfixFormatException("Insufficient operands")
    try:
        stack.push(operand1 << operand2)
    except:
        raise PostfixFormatException("Illegal bit shift operand")



