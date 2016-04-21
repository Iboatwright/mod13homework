# car_class.py
# Exercise Selected: Chapter 14 program 2
# Name of program: Car Class
# Description of program:  This program demonstrates OOP programming by
#   using a class to create and object then drive it around the block.


def main():
    # Local variables
    end_program = False

    # Display the intro to the user.
    fluffy_intro()

    while end_program not in ['yes', 'y']:
        # Local variables
        speed_changes = 5
        year_model = int(get_user_input(
                         "year of the car's model in YYYY format."))
        make = get_user_input("make of the car.")

        # car_car is an object of Car class.
        car_car = Car(year_model, make)

        # Loop through the accelerate function and print the current speed.
        print("Here we go.  Hang on tight!")
        for i in range(speed_changes):
            car_car.accelerate()
            print("Current speed is: {}".format(car_car.get_speed()))

        # Loop through the brake function and print the current speed.
        for i in range(speed_changes):
            car_car.brake()
            print("Breaking! Speed is: {}".format(car_car.get_speed()))

        # This is a test drive, not a car rental.  Only one ride per turn.
        #   The while loop ends here and the reference variables pass out of
        #   scope, effectively destroying them.  If the user goes again new
        #   variables will be created.
        print("Thanks for test driving the {} {}.".format(year_model, make))
        end_program = go_again()
    print("Please exit to your left. Have a nice day!")


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Car Class program.\n'
          'This program demostrates the use of a Class by creating a car '
          'object\nand test driving it.')
    return None


# Returns unvalidated user input.
def get_user_input(message):
    return input("Please enter the {} >> ".format(message))


# Program loop control variable with validation.
def go_again():
    end_program = input('Are you finished test driving cars? yes or (n)o >> ')
    while end_program.lower() not in ['yes','y','no','n','']:
        end_program = input('Error: Invalid entry.  Type yes or no.')
    return end_program.lower()


# Car class is used to create car objects and drive them around.
class Car:
    # The init constructor accepts the car’s year model and make as arguments.
    def __init__(self, year_model, make):
        # The year_model field is an Integer that holds the car’s year model.
        self.year_model = year_model

        # The make field references a String that holds the make of the car.
        self.make = make

        # The speed field is an Integer that holds the car’s current speed.
        self.speed = 0

    # accelerate adds 5 or some input integer to the speed field.
    def accelerate(self, a=5):
        self.speed += a

    # break subtracts 5 or some input integer to the speed field to a minimum
    #   of 0.
    def brake(self, b=5):
        self.speed -= b if self.speed >= b else 0

    # Accessors to return class field values.
    def year_model(self):
        return self.year_model

    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed


# Execute the program.
main()