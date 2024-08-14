# def addition(num1, num2):
   
#     total = num1 + num2
#     print(total)
    
#     num1 = input("please give the first number to be summed: ")
#     num2 = input("please give the second number to be summed: ")

def meanValue(list):
  
    mysum = sum(list)/(len(list))
    # mean = mysum/(len(list))
    print(mysum)
      
      
# meanValue([4, 2, 5, 1, 2, 1, 6])
# meanValue([1, 2, 3, 4, 5])
meanValue([-99, 105])
meanValue([25, 50, 100, 95])