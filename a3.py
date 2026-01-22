def printtwoodd(arr,size):
    xorf2=arr[0]

    x=0
    y=0

    setbit=0
    for i in range(1,size ):
        xorf2 = xorf2 ^ arr[i]

    setbit = xorf2 & ~(xorf2 - 1)

    for i in range(size):
        if(arr[i] &setbit):
            x=x^arr[i]
        else:
            y=y^ arr[i]

    print("the two ODD elements are :", x,"&",y)

arr=[]

arrsize = int(input("Enter sizeof he array : "))
for i in range(0,arrsize):
    z=int(input("ENter element : "))
    arr.append(z)

printtwoodd(arr, arrsize)    

