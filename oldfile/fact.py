print("Hello world")
def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(5))
print(fact(4))
print(fact(10))