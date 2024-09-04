def count_all_stars(galaxies):
    total_stars = 0
    for stars in galaxies:
        total_stars += stars  # fix me!
    return total_stars
galaxies = [1000000, 2300000, 500000]  # Example list of galaxies with star counts
print("there are ",count_all_stars(galaxies), "stars in the galaxy")  # This should print the sum of all stars


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance #Private attribute
        
    # Public method to access private attribute
    def get_balance(self):
        return self.__balance