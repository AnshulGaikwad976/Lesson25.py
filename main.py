def checkisame(number1,number2):

    if((number1 ^ number2) !=0):
        print("numbers are not equal")

    else:
        print("both numbers are equal")

number1=int(input("Enter the first number to compare :"))
number2 = int(input("Enter the second number to compare:"))     

checkisame(number1,number2)