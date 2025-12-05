n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
try:
    with open("example.txt","r") as file:
        file.readline()
    try:
         z=n1/n2
         print(z)
    except ZeroDivisionError:
        print("Error is in the nested try block")
except ZeroDivisionError:
    print("Division by zero")
except FileNotFoundError:
    print("Example File not found")
except :
    print("Error in your program")
finally:
    print("Program is finished")