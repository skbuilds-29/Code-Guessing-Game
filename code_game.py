import random
digits = 0
secret_code=""
for digits in range(0,4):
    secret_code+=(str)(random.randint(0,9))
    digits+=1
n = 0
count  = 0
print("The secret code is 4 digits long!")
while n!=4:
    i = 0
    n = 0
    guess = input("Enter your guess! (type quit to quit)  ").lower()
    while  len(guess)!=4 or(not guess.isdigit() and guess!="quit"):
        print("Invalid guess! Please enter a 4-digit NUMBER ")
        guess = input("Enter your guess! (type quit to quit) ").lower()
    if guess == "quit":
        break
    for i in range(0,4):
        if (guess[i]==secret_code[i]):
             n+=1
    count+=1
    print("You have " + str(n) + " numbers right!")
if guess == "quit":
    print("The secret code was " + str(secret_code))
else:
    print("You win! That took you " + str(count) + " guesses!")
