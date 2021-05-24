def Message_print(*args):
    print(args)
Message_print(1,2,3,4,5,6)


def Message_print(*a,**b):
    print(a)
    print(b.keys())
    print(b.values())
Message_print(1,2,3,4,5,6,name="Rama")

d={1:'one',2:'two',3:'Threee'}
d.keys()

d.values()

d[0]='zero'
print(d)

d.update({1:'one',5:'five'})
print(d)


del d[1]
d

d[1]='one'
print(d)


#map reduce filter
li=[1,2,3,4,5,6]
li[3:]
 

ans=[]
for i in li:
    if(i%2==0):
        ans.append(0)
    else:
        ans.append(1)
print(ans)


#map function
def function(i):
    if(i%2==0):
        return 0
    else:
        return 1
answer=map(function,li)
list(ans)

ans1=map(lambda x: 0 if x%2==0 else 1,li)
list(ans1)


a=lambda: 2+3
a()

b=lambda x,y:print(x,y)
b(5,6)


b=lambda x: 1 if x%2==0 else 0
b(2)

a=1
b=2
a > b and True or False


li=[1,2,3,4,6,5]
ans=filter(lambda x: 1 if x%2==0 else 0,li)
print(list(ans))


ans=filter(lambda x: 1 if x%2==0 else 0,li)
print(list(ans))


from functools import reduce
ans=reduce(lambda a,b: a+b, li)
print(ans)
