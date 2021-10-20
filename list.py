print("Hello world")
classmates = ['Michael','Tomy','Jerry']
print(classmates[0])
print(classmates[-1])
print(classmates[-2])
print(len(classmates))
classmates.append('Frank')
print(classmates)
classmates.pop()
print(classmates)
classmates.insert(0,'Frank')
print(classmates)
mate = classmates.pop(0)
classmates.append(mate)

print('classmates')
print(classmates)

#classmates2 = classmates
#print('classmates 2')
#print(classmates2)
print('classmates 2 again')
classmates2 = ['Lucy', 'Mary']
print(classmates2)
classmates.insert(1,classmates2)
print(classmates)



print('-------------------')
l = len(classmates)
print(l)
print(classmates[1])
print(classmates[l - 1])


classmates3 = ('Michael', 'Bob', 'Tracy')
print(classmates3)
#classmates3[2] = 'ooo'
print(classmates3[2])
print(len(classmates3))