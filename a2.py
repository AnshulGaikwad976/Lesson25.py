def oddoccuring(arr):
    res=0

    for element in arr:

        res=res ^ element

    return res

arr =[]    

n = int(input("Enter the array size : "))

while(n):

    num = int(input("Enter the number :"))
    arr.append(num)
    n-=1

print("\n\nOdd occuring number is : ", oddoccuring(arr) )    
