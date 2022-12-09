num = int(input("Enter number: "))
thesum = 0
#give the range from (1,11)
for count in range(1,11):
    print(num," * ",count,"=",num*count)
    thesum +=count
print(thesum)
