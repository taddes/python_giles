def linear_srch(item, array=[]):
    for value in array:
        if item == value:
            return value
        else:
            continue

print(linear_srch(7, [2,3,5,7,8]))

def alt_linear(item, my_list=[]):
    i = 0
    found = False

    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i = i + 1
        
    return found

print(alt_linear(7, [2,3,5,7,8]))