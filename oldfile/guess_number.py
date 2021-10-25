import random
print("Hello,welcome to my Guess number game!")
target = random.randint(0,100)
print(target)
nofguess = int(input('Please enter a num that I am thinking(0~100):'))

def guess(n):
    if n == target :
        return 0
    elif n > target :
        print('Too high,Guess again:',end="")
        
    elif n < target :
        print('Too low,Guess again:',end="")
        
ToContinue = True
Choose_of_yes_or_not = 'yes'

while ToContinue :
    while guess(nofguess) !=0 :
        nofguess=int(input())
   
   
    print("That's it! Would you like to play again? (yes/no)",end="")
    Choose_of_yes_or_not = input()
    ToContinue = (Choose_of_yes_or_not == 'yes') or (Choose_of_yes_or_not == 'y') or (Choose_of_yes_or_not == 'Y') 
    if ToContinue :
        target = random.randint(0,100)
        print('Please enter a num that I am thinking:',end="")
        nofguess=int(input())
    else :
        ToContinue = False




    
