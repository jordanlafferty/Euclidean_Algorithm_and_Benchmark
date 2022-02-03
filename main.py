import timeit

@profile
def GCD_loop(n,m):
    if m ==0:
        return 0
    l= n%m
    while l>0:
        n =m
        m=l
        l = n%m
    return m

@profile
def GCD_recursion(n, m):
    if m ==0:
        return n
    else:
        l= n%m
        n =m
        m=l
        return GCD_recursion(n,m)


def test_loop():
    GCD_loop(12121, 121344)

def test_recursion():
    GCD_recursion(12121, 121344)


test_loop()
test_recursion()
#print(timeit.Timer(test_loop).timeit(number =100))
#print(timeit.Timer(test_recursion).timeit(number =100))