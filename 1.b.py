
def F(d : dict):
    print("Sorted by keys:")
    for k in sorted(d.keys()):
        x,y=d[k]
        print('-',k,'-,-',x,'-,-',y,'-')
    print("Sorted by x values:")
    for k in sorted(d.keys(), key= lambda k:d[k][0],reverse=True):
        x,y=d[k]
        print('-',k,'-,-',x,'-,-',y,'-')
    print("Sorted by y values:")
    for k in sorted(d.keys(), key=lambda k:d[k][1]):
        x,y=d[k]
        print('-',k,'-,-',x,'-,-',y,'-')
    print()
    pass

# Tests
F({1 : (1, 2), 2 : (-1, 4), 5 : (-4, 3), 4 : (2, 3)})
F({-8 : (4, 2), 6 : (-3, 4), 7 : (2, 1), 5 : (9, -10)})