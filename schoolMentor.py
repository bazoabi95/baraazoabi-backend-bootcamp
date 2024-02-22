#uppercase
print("abc".upper())
#lowercase
print("ABC".lower())
#print a word that starting from specific letter???
wordsArr=['apple','banana','cat','dream','elephant','food','google','hat','ignore','jeep','keep','lemon','moment','night','orange','people','quality','rest','stable','understand','volume','wood','xerotic','yellow','zebra']
letter=input("Enter a letter: ")
for word in wordsArr:
    if(letter==word[0]):
        print(word)
    
#print N*N multiplication table
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if(j==n-1):
            print(f'{(i+1)*(j+1)}\n') 
        else:
            print((i+1)*(j+1),end="  ") 
       
#○ print square number of a given number
import math
num=int(input("Enter a number: "))
print(math.pow(num,2))

#check if a given number is prime
pnumber=int(input("Enter a number to check if it a prime number: "))
isPrime=True
for i in range(2,pnumber):
    if(pnumber%i==0):
        isPrime=False
if(isPrime==True):
    print(f'the number {pnumber} is a prime number')
else:
    print(f'The number {pnumber} is not a prime number')

#create a function that, according to the input from the user, run the specific task.
    #input what task we want to do: 
tasks=int(input("Enter the task you want to do, choose by numbers:\n 1.convert to uppercase\n 2.convert to lowercase\n 3.print a word starting with specific letter.\n 4.print multiplication table n*n\n 5.print square number\n 6.check prime number \n"))

match tasks:
    case 1:
        text=input("Enter a text to convert to uppercase: ")
        print(text.upper())
    case 2:
        text=input("Enter a text to convert to lowercase: ")
        print(text.lower())
    case 3: 
        wordsArr=['apple','banana','cat','dream','elephant','food','google','hat','ignore','jeep','keep','lemon','moment','night','orange','people','quality','rest','stable','understand','volume','wood','xerotic','yellow','zebra']
        letter=input("Enter a letter: ")
        for word in wordsArr:
            if(letter==word[0]):
                print(word)
    case 4: 
        n=int(input("Enter a number: "))
        for i in range(n):
            for j in range(n):
                if(j==n-1):
                    print(f'{(i+1)*(j+1)}\n') 
                else:
                    print((i+1)*(j+1),end="  ") 
    case 5:
        num=int(input("Enter a number: "))
        print(math.pow(num,2))
    case 6:
        pnumber=int(input("Enter a number to check if it a prime number: "))
        isPrime=True
        for i in range(2,pnumber):
            if(pnumber%i==0):
                isPrime=False
            if(isPrime==True):
                print(f'the number {pnumber} is a prime number')
            else:
                print(f'The number {pnumber} is not a prime number')