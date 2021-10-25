#生成器
print("Hello world")
g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max) :
    n,a,b = 0,0,1
    while n < max :
        print(b)
        #a, b = b, a+b
        t = [b, a+b]
        a = t[0]
        b = t[1]
        n = n + 1
    return "done"

fib(10)