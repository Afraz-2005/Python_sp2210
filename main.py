##########################Excercise-1####################################
name = input("enter your name: ")
age = int(input("enter you age:" ))
year_to_turn_100 = 2022 - age + 100
print(name + ", you will be 100 years old in the year " + str(year_to_turn_100))
#########################################################################
##########################Excercise-2####################################

number = int(input("enter a number: "))
modL = number % 2
if modL > 0:
    print("odd number.")
else:
    print("even number.")
#########################################################################
##########################Excercise-3####################################

lessFnums = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)
        lessFnums.append(i)
        lessFnums.sort()
       
print(lessFnums)
print()
#########################################################################
##########################Excercise-4####################################
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
#########################################################################
##########################Excercise-5####################################
def common_member(a, b):  
    a_set = set(a)
    b_set = set(b)
     
    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set))
    else:
        return("no common elements")
     
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common_member(a, b))
#########################################################################
##########################Excercise-6####################################
word = input("Please enter a word: ")
word = str(word)
reverse = word[::-1]
print(reverse)

if word == reverse:
    print("palindrome")
else:
    print("not a palindrome")


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)
#########################################################################
##########################Excercise-7####################################

import random

computerList = ['rock', 'paper', 'scissor']
playerChoice = input("enter player choice from rock, paper, scissor: ")
computer_choice = random.choice(computerList)

if playerChoice == "rock" and computer_choice == "paper":
    print("computer picked paper, you lost")
elif playerChoice == "rock" and computer_choice == "scissor":
    print("computer picked scissor, you won")
elif playerChoice == "rock" and computer_choice == "rock":
    print("its a draw")
    
if playerChoice == "paper" and computer_choice == "paper":
    print("its a draw")
elif playerChoice == "paper" and computer_choice == "scissor":
    print("computer picked scissor, you won")
elif playerChoice == "paper" and computer_choice == "rock":
    print("computer picked rock, you won")
    
if playerChoice == "scissor" and computer_choice == "paper":
    print("computer picked paper, you won")
elif playerChoice == "scissor" and computer_choice == "scissor":
    print("Its a draw")
elif playerChoice == "scissor" and computer_choice == "rock":
    print("computer picked rock, you lost")
    
########################################################################
#########################Excercise-8####################################

import random

randomNum = random.randint(1, 9)
guessIt = 0

while guessIt != randomNum and guessIt != "exit":
    guessIt = input("enter a number between 1 to 9 or type 'exit' to quit: ")
    if guessIt == "exit":
        break
    
    guessIt = int(guessIt)
    
    if randomNum == guessIt:
        print("you are correct")

    elif randomNum > guessIt:
        print("Guessed too low")

    elif randomNum < guessIt:
        print("guessed too high")
    
#######################################################################
########################Excercise-9####################################

import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
print(result)

#######################################################################
#######################Excercise-10####################################

num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print ('prime')
		else:
			print ('not prime')
	else:
		print ('not prime')
	
is_prime(num)

######################################################################
######################Excercise-12####################################

a = [5, 10, 15, 20, 25]
def list(list):
    return [list[0], list[len(list)-1]]
print(list(a))

######################################################################
######################Excercise-12####################################

def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()

######################################################################
######################Excercise-13####################################

import random

chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()|\}{]['
userInp = int(input("enter the password length: "))
length = userInp
password = "".join(random.sample(chars,length ))
print('your password: ', password)

#####################################################################
#####################Excercise-13####################################

userInp = str(input("enter a sentence: "))

userInp = userInp.split()
a = userInp
b = " ".join(reversed(a))
print(b)

#####################################################################
#####################Excercise-14####################################

import random

guess = 10
bull = 0
cow = 0

randomNum = str(random.randint(0, 9999))
print(randomNum)

for i in range(guess):
    userInp = str(input("Enter The Number: "))
    if userInp == randomNum:
        cow = cow + 1
    a = map(int, userInp)
    x = list(a)
    b = map(int, randomNum)
    y = list(b)
    if all(item in x for item in y) and x != y:
        bull = bull + 123
    a = str(a)
    b = str(b)
    print(bull, " bull ", cow, " cow")




        
