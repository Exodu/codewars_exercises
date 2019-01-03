# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]


def move_zeros(array):
    no_zeros = [i for i in array if isinstance(i, bool) or i != 0]

    return no_zeros + [0] * (len(array) - len(no_zeros))
