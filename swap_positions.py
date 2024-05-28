# Python3 program to swap elements
# at given positions

def swapTwo(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

#driver function
list = [15,26,31,22]
pos1, pos2 = 1,3 # will swap index 1 and 3
print(swapTwo(list, pos1, pos2))
# output [15, 22, 31, 26]

print(swapTwo(list, pos1-1, pos2-1))
# output [31, 26, 15, 22]