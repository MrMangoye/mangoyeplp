def personalized_greetings():
    """
    Asks the user for their name and favourite color,
    then prints a personalized greeting.
    """
    name = input("What is your name? ")
    color = input("What is your favourite color? ")

    print(f"Hello, {name}! Your favourite color, {color}, is awesome!")

# Call the function to execute the program
personalized_greetings()
