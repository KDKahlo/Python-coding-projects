# number = 0

# print(number ** 2)
# number += 1

# print(number ** 2)
# number += 1



#Exercise 16 - while loop w/ if statement
number = 5
 #this loop will allow you to exit the loop by entering "quit"
while input(">> ") != "quit":
 #this 'if statement' gives a second way to exit the loop is to press enter to iterate through the loop til 10 is reached
    if number >= 10:
        break
    print(f"number = {number}")
    number += 1
    