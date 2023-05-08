# Write a Python function called max_num()
# to find the maximum of three numbers.

def max_num(a, b, c):
    return max([a,b,c])

print(max_num(1, 2, 3))
print(max_num(5, 12, 86))
print(max_num(1, 15, 30))

# Write a Python function called mult_list()
# to multiply all the numbers in a list.

def mult_list(lst):
    #if list is empty, return 0
    if len(lst) == 0:
        return 0
    #product starts with first element of list
    prod=lst[0]

    #go through list elements and multiply them together
    if lens(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([12]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::-1]

print(rev_string(""))
print(rev_string("boats"))
print(rev_string("boston whaler"))

# Write a Python function called num_within() 
# to check whether a number falls in a given range.

def num_within(a,b,c):
    return a in range(b,c+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# Write a Python function called pascal() 
# that prints out the first n rows of Pascal's triangle.

def pascal()