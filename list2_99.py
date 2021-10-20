#print("Hello world")
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
n = 0 
while n < len(L) / 2:
    print(L[n],end=", ")
    n = n + 1

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print('-----------------------')
print(L[0:3])

print('-----------------------')
L2 = L[:3]

tag=['https://www.cnblogs.com/yangyuqig/p/10101663.html']
print(tag)
print(tag[0])
print(tag[0][:24])

tt2 = list(tag[0])


for i in range(len(tt2)) :
    if tt2[i] == '/' :
       tt2[i] = '\\'
       i = i + 1
       pass
tt = "".join(tt2)
print(tt)
print(tt.upper())
print(tt.title())
