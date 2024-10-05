## Description
#You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0.

#Simplest solution
def positive_sum1(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

# can just do it in one line, using sum function
# which will (default to zero if given nothing and)
# iterate across its input iterable
def positive_sum2(arr):
    return sum(i for i in arr if i > 0)


# This is a version using filter and a lamba function
# - must less intuitive IMO unless you've spent a lot
# of time getting used to lambda's.
def positive_sum3(arr):
    return sum(filter(lambda x: x > 0,arr))
  #the above line means: sum of all things in arr which match a filter criterion
  # the criterion is defined by a function, which is defined there in the middle of the line
  # lambda (the function) takes x as an input, and returns yes/no (actually 1/0)
  # depending on whether its input x is positive

#Back to a simple option - just make a list
#start out empty and add things if they are >0
def positive_sum4(arr):
    L = []
    for i in arr:
        if (i > 0):
            L.append(i)
    return (sum(L))



