def person(name, age, **kw):
    print('name:',name,'age:',age, 'others:',kw)
    return
person('Tommy',17)  
person('Jack',18,Job='engineer',Location='Beijing')
extra={'job':'doctor','location':'shanghai'}
person('Lucy',20,job=extra['job'],location=extra['location'])
person('Jack',21,**extra)