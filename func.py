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




Age=dict()


def switch(i):
    switcher={
                    1: InsertData,
                    2: UpdateData,
                    3: DeleteData,
                    4: ShowData
             }
    return switcher.get(i,'no option found')

    
def App(): 
    while True:
        print("1.Enter the data:")
        print("2.Update the data")
        print("3.Delete the data")
        print("4.Show the data")
        print("Enter 0 to quit")
        opt=int(input("Please choose option from above:"))
        if (opt > 0 and opt <5):
            ans=switch(opt)
            ans()
            
        elif (opt==0):
            break


def InsertData():
    name=input("Enter Name:")
    age=int(input("Enter age:"))
    Age.update({name:age})
    print("new data added\n")
    
def UpdateData():
    name=input("Enter Name:")
    age=int(input("Enter age:"))
    if name in Age.keys():
        Age.update({name:age})
        print("new data updated\n")
    else:
        print("no item in the dictionary\n")
    
def DeleteData():
    print("Enter the key you want to delete:")
    delete=input()
    if delete in Age.keys():
        del Age[delete]
    else:
        print("no item found")
        
def ShowData():
    for i,j in Age.items():
        print(i,'=',j)