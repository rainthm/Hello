#Create list test
L = list(range(1,11))
print(L)

LL = list(x * x for x in(range(1,11)))
print(LL)

LLL = list(x for x in(range(1,11)) if x % 2 == 1)
print(LLL)

print(list(m+''+n for m in 'ABC' for n in ['Hello','Hi']))