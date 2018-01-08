# ask for the person's name
your_name = input("Please enter your name here: ")
# ask for the person's age
your_age = int(input("Please enter your age here: "))

# check if the person's age is between 18 to 30
if your_age >= 18 and your_age < 31:
    print("Welcome to the holiday, {}!".format(your_name))
else:
    print("I'm sorry, {}, this holiday is not for you.".format(your_name))
