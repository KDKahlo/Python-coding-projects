# number = 0

# print(number ** 2)
# number += 1

# print(number ** 2)
# number += 1



#Exercise 16 - while loop w/ if statement
# number = 5
#  #this loop will allow you to exit the loop by entering "quit"
# while input(">> ") != "quit":
#  #this 'if statement' gives a second way to exit the loop is to press enter to iterate through the loop til 10 is reached
#     if number >= 10:
#         break
#     print(f"number = {number}")
#     number += 1
    
#for-loop

#it is possible to use the for loop by defining the text variable and using an auxiliary variable character
# text = "Python"
# for character in text:
#     print(character)

#we can also use just the auxiliary variable to loop through 
# for character in ["start",2,5,3,1,6,8,10, "finished"]:
#     print(character)

# for numbers in "123456789":
#     int(numbers) ** 2
#     print(numbers)
#     numbers ** 2

# for numbers in "123456789":
#    print( int(numbers) ** 2)

# for numbers in range(1, 100+1):
#     print(numbers)

#declared the number variable    
# number = 1
# #the while statement ask number to loop until it is great than or equal to 100
# while number <= 100:
# #it will print the current number of the loop
#     print(number)
# #after printing it will increment number by 1 and the loop will begin again
#     number += 1
    
   
#Exercise 19 -Score

# number = int(input("Give me a number>>"))
# #  #this loop will allow you to exit the loop by entering "quit"
# while number != "quit":
# #  #this 'if statement' gives a second way to exit the loop is to press enter to iterate through the loop til 10 is reached
#         if int(number) <=0:
#             print("Invalid number")
#             break
#         elif int(number) in range(0, 40+1):
#             print("you failed the exam")
#             break
#         elif int(number) in range(41,80+1):
#             print("You passed, but you did not do amazing")
#             break
#         elif int(number) in range(81,100):
#             print("Congratulations! you did well")
#             break
#         elif int(number) == 100:
#             print("You have a perfect score!")
#             break
            
        
        
#Login 1 Exercise 21.1

# user = input("please enter user name: ")
# password = input("please enter your password: ")
# if user == "admin" and  password == "1234":
#          print("True")        
# else:
#     print("False")
    
    
#Letter Filter
inputString = input("Enter a Text: ")
output=""
for character in inputString:
   if(character in ['a','e','i','o','u'] or character in ['A','E','I','O','U'] ):
      continue
   else:
      output += character
print(output)
  
            
            
        
            
    

   


    

        
       
