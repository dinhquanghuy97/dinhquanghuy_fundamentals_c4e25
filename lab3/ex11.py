def is_inside(x,y):
    if x[0] > y[0] and x[1] > y[1]:
        return True
    else:
        return False
check_1 = is_inside([200, 120], [140, 60, 100, 200])
check_2 = is_inside([100, 120], [140, 60, 	])
print(check_1,check_2)
    