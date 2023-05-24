for i in range(1,21,2):
    print("Play song number",i)

num = int(input("enter a number: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

num = 5
fac = 1
for i in range(1, num+1):
    fac *= i
print(fac)

for i in range(1,100):
    if i % 5 == 0 and i % 8 == 0:
        print(i)

for i in range(1,41):
    if i % 4 == 0:
        print("Bingo")
    else:
        print(i)

n = 0
num = 7
while n <=10:
    print(n*num)
    n +=1

repeat = "y"
while repeat == "y":
    num1 = int(input("enter 1st number: "))
    num2 = int(input("enter 2nd number: "))
    print(num1+num2)
    repeat = input("do you want to repeat again?(y/n): ")
    if repeat == "n":
        break   
