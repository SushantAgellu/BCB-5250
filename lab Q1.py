number = (range(1,16))
for num in number :
    print(num)
    
for num in number :
    if num%3 ==0:
        print(num)


temperature = [32, 45, 50, 60, 72, 85, 90,100]
for temp in temperature :
    celsius = (temp - 32)*(5/9)
    print(celsius)




fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(list(enumerate(fruits)))
n = len(fruits)
print(n)
for index,item in enumerate(fruits):
    x=((n-1) - index)
    print(x,fruits[x])

variable = int(input("your integer"))
if variable%3==0 and variable%5 ==0:
   print("FizzBuzz")
elif variable%5==0:
    print("buzz")
elif variable%3==0 :
    print("Fizz")
else:print(variable)


