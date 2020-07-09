# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

def getDivisors(userNumber):
    divisorsList = range(2, userNumber)
    check = 0
    for item in divisorsList:
        if ((userNumber % item) == 0):
            check += 1

    if(check == 0 and userNumber != 1):
        print("This number is Prime")
    else:
        print("This number is not Prime")


def main():
    userNumber = int(input("Digite um numero: "))

    getDivisors(userNumber)


main()
