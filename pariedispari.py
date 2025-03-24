n:int=int(input("Enter 10 numbers: "))
i=0
count=0
while i<=10:
    n1:int=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
i+=1
count+=1
print("Total even numbers: ",count)
print("Total odd numbers: ",10-count)

