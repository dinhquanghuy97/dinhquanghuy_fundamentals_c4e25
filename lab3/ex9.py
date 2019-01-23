def get_even_list(l):
    new_l = []
    for i in l:
        if i % 2 == 0:
            new_l.append(i)
    return(new_l)
l = get_even_list([1,2,3,4,5,6,7,8,9,10])
print(l)
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
