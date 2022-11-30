num = int(input("Enter number: "))
thesum = 0
for count in range(1,11):
    print(num," * ",count,"=",num*count)
    thesum +=count
print(thesum)