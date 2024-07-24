#Assignments for today
#Create a Simple Chatbot
#Write a program that takes & stores the following data from the person using the program via input():
# the first name and the year of birth
#Afterwards the program should output a personal greeting and calculate how old the respective person will be in the year 2050.
name = input("What is your name? ")
print(f"Hello {name}")

age = int(input("What year were you born? "))
age = 2050 - age

print (f"Here is a fun fact for you {name}. In 2050 you will be {age} years old!")