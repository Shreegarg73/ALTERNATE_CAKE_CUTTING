#Project for cutting a cake
def cake(N): #defining a function in which cake is to be divide
    """ condition to cut cake in equal pieces from center till it's borderline"""
    if 360 % N == 0:
        a = 'Yes'
    else:
        a = 'No'

    if N > 360:
        b = 'No'
    else:
        b = 'Yes'

    if N > 26:
        c = 'No'
    else:
        c = 'Yes'

    return f'{a} {b} {c}'

N = int(input()) #input in which cake is to be cut for dividation

print(cake(N)) #calling the defined function