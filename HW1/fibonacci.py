print("\nWelcome to the Fibonacci generator!")
n = int(input("Please enter how many fibonacci numbers to generate: "))
n1 = 0
n2 = 1

for i in range(0,n):
    print(n1, end =" ") #keep the output on the same line
    if i%3 == 0: #start a new line every 3rd number
        print(" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print("\nThank you for using the Fibonacci generator!\n")