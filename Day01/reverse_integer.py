#################################################################
# Programme: Reverse the integer given  #
# Author Name: Amit Arya                #
# Date: Fri Sep 16 22:52:02 IST 2022    #
#################################################################

n = int(input())
# Approach 1: Logical
reversed=0
while n!=0:
    reversed = reversed*10 + n%10
    n = (n//10)

print(reversed)
