# def addition(num1, num2):
   
#     total = num1 + num2
#     print(total)
    
#     num1 = input("please give the first number to be summed: ")
#     num2 = input("please give the second number to be summed: ")

# def meanValue(list):
  
#     mysum = sum(list)/(len(list))
#     # mean = mysum/(len(list))
#     print(mysum)
      
      
# # meanValue([4, 2, 5, 1, 2, 1, 6])
# # meanValue([1, 2, 3, 4, 5])
# meanValue([-99, 105])
# meanValue([25, 50, 100, 95])

#Exercise 29 
# def calculate(*args, operation = "sum", is_float = False):
#     if operation == "sum":
#         result = sum(args)
#     elif operation == "product":
#         result = 1
#         for num in args:
#             result *= num
#     else:
#         return "Invalid operation"
    
#     if is_float:
#         return float(result)
#     return int(result)

# print(calculate(1, 2, 3.1))
# print(calculate(1, 2, 3.1, operation = 
# "product", is_float = True))
# print(calculate(1, 2, 3.1, operation = 
# "division"))

#Temperature Conversion Function

def convert_temperature(value, **kwargs):
    # Extract units from kwargs, with defaults
    unit_in = kwargs.get("unit_in", "Celsius")
    unit_out = kwargs.get("unit_out", "Celsius")
    
    # Convert the input temperature to Celsius first
    if unit_in == "Celsius":
        temp_in_celsius = value
    elif unit_in == "Fahrenheit":
        temp_in_celsius = (value - 32) * 5/9
    elif unit_in == "Kelvin":
        temp_in_celsius = value - 273.15
    else:
        return "Invalid input unit"
    
    # Convert the Celsius temperature to the desired output unit
    if unit_out == "Celsius":
        return temp_in_celsius
    elif unit_out == "Fahrenheit":
        return (temp_in_celsius * 9/5) + 32
    elif unit_out == "Kelvin":
        return temp_in_celsius + 273.15
    else:
        return "Invalid output unit"
    
    # Default units (Celsius to Celsius)
print(convert_temperature(100))  # Output: 100.0

# Celsius to Fahrenheit
print(convert_temperature(100, unit_out="Fahrenheit"))  # Output: 212.0

# Fahrenheit to Celsius
print(convert_temperature(32, unit_in="Fahrenheit", unit_out="Celsius"))  # Output: 0.0

# Kelvin to Celsius
print(convert_temperature(273.15, unit_in="Kelvin", unit_out="Celsius"))  # Output: 0.0

# Celsius to Kelvin
print(convert_temperature(0, unit_out="Kelvin"))  # Output: 273.15
