# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
# This part involves a game with teddy bears. The game starts when I give you some bears. You can then
# repeatedly give back some bears, but you must follow these rules, where n is the number of bears that you
# currently have:
# 1. If n is even, then you may give back n/2 bears.
# 2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
# 3. If n is divisible by 5, then you may give back 42 bears.
# The goal of the game is to end up with EXACTLY 42 bears.
def bears(n):
    print(n)
    if n == 42:                                                #Base case if n == 42 you win the game
        return True
    if n < 42:                                                 #Base Case if n is less the 42 then return falce
        return False
    if n % 2 == 0:                                             #rull 1 if n is evenly davisabel by 2 the send half of n into a recursive functio
        if bears(n // 2):                                      #if the recursive fuction returns ture the also return true otherwis go on th next rull
            return True
    if n % 3 == 0 or n % 4 == 0:                               #rull 2 If n is divisible by 3 or 4, then you may multiply the last two digits and subtrac that from n send that into a recursive function
        next_value = n - (int(str(n)[-1]) * int(str(n)[-2]))   # if the nex value of n would not change dont preform rull 2
        if next_value != n:
            if bears(next_value):                              #if the recursive fuction returns ture the also return true otherwis go on th next rull
                return True
    if n % 5 == 0:                                             #rull 3 If n is divisible by 5, then subtract 41 from n in send that to a recursicve function
        if bears(n - 42):
            return True

    return False                                               #returns falce if prim numbers < the 42
