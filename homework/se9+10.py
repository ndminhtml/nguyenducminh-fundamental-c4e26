def get_even_list(l):
    new_list = []
    for i in l:
        if i%2 == 0:
            new_list.append(i)
    return new_list

list_l = get_even_list([1,4,5,-1,10])
print(list_l)

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
