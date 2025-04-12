# Q1
lst = [1,2,3, [1,2,3,[3,4],2]]

def flatten(lst):
    result = []
    for element in lst:
        if type(element) == type(1):
            result.append(element)
        else:
            result += flatten(element)

    return result

result = flatten(lst)
print(result)

# OUTPUT:
# [1, 2, 3, 1, 2, 3, 3, 4, 2]


# Q2
lst = [ [ [ '(0,1,2)' , '(3,4,5)'] , ['(5,6,7)' , '(9,4,2)'] ] ]

def convert(lst):
    if type(lst) == type('a'):
        return [int(num) for num in lst.strip("()").split(",")]
    
    elif type(lst) == type([]):
        return [convert(item) for item in lst]
    
    return lst
    
result = convert(lst)
print(result)

# OUTPUT
# [[[[0, 1, 2], [3, 4, 5]], [[5, 6, 7], [9, 4, 2]]]]