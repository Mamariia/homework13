def test (a, b = 'string', c = True):
    print (a, b, c)

test(1)

def factorial (n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))