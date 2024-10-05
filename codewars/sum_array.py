#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
#Examples
#Input: [1, 5.2, 4, 0, -1]
#Output: 9.2

#Input: []
#Output: 0

# iterate through the array a, and sum everything
def sum_array1(a):
    return sum(x for x in a)

#but it can be much simpler!!
def sum_array2(a):
    return sum(a)

