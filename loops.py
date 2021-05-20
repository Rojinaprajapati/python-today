for i in range(10):
    print(i)


string="hello world"
for i in range(0,len(string),2):
    print(string[i])


j=11
while(j<=10):
    print(j)
    j=j+1


set1={1,2,3,4,5,6}
set2={2,3,4,5,6,7,8}
print (set1)
print (set2)


set1=set1.union(set2)
set1

def function():
    return [1,2,3,4]
print(function())

#lambda arguments:expression
#x=lambda a:a+10
#print(x(5))


y=lambda a,b:a*b
print(y(5,10))


""" With no Argument , and no Return """
def my_function():
    print("I am from My function ")

my_function()

""" With Argument and no Return """
def function(message):
    print("Hello "+message)
function("Nitesh")

""" With no Argument , but with Return Type """
def function1():
    return "Nitesh "
a=function1()
print(a)
print(function1())
""" With Argument and Return Type """
def function_sum(a):
    return a+10
print("Sum called by function_sum is : ",function_sum(5))