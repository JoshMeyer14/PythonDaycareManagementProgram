"""I am going to add first and last name and full name vairbale and adjust my object and merrry day class
i ma goiing to use title method to make it more proffesional and do a hiddin emplyoee panel that does addign tuition
makes this better and then ill be done"""


#Print a Welcome message!
print("Welcome to Merry Day!")

enrollments = {}

class MerryDay:
    """Merry Day class."""

    def __init__(self, name, age, balance, enrolled):
        self.name = name
        self.age = age
        self.balance = balance
        self.enrolled = enrolled

    def enroll(self):
        """Enroll at Merry Day."""
        self.enrolled = True
        print(f"{self.name} is now enrolled.")

    def unenroll(self):
        """Unenroll at Merry Day."""
        self.enrolled = False
        print(f"{self.name} is now unenrolled.")

    def add_week(self):
        """Add week to Merry Day for weekly payment."""
        if self.enrolled:
            self.balance = self.balance + 250
        else:
            print("You are not enrolled.")

    def make_payment(self):
        """Decrease the balance by one day."""
        payment = float(input("Please enter your payment amount: "))
        if payment > self.balance:
            print("Payment is greater than your balance.")
        else:
            self.balance = self.balance - payment
            print(f"Your balance is now {self.balance}.")

    def show_balance(self):
        """Show your balance."""
        print(f"Your balance is ${self.balance}.")

    def print_person(self):
        """Print a message to user to person reading."""
        person_name = {
            "name": self.name,
            "age": self.age,
        }
        print(person_name)

    @staticmethod
    def show_beliefs():
        """Print a message to user to person reading."""
        with open("Doctrine.txt", "r") as file:
            print(file.read())

    @staticmethod
    def save_enrollments():
        with open("Enrollments.txt", "w", encoding="utf-8") as file:
            for child in enrollments.values():
                file.write(
                    f"Name: {child.name}, "
                    f"Age: {child.age}, "
                    f"Balance: ${child.balance}, "
                    f"Enrolled: {child.enrolled}\n"
                )

    @staticmethod
    def charge_everyone():
        """Charge everyone."""
        weeks = int(input("How many weeks do you want to charge: "))

        for child in enrollments.values():
            for i in range(weeks):
                child.add_week()

        print("You are now charged everyone.")

    @staticmethod
    def show_all_enrollments():
        """Show all enrollments."""
        for child in enrollments.values():
            print(
                f"{child.name} | "
                f"Age: {child.age} | "
                f"Balance: ${child.balance} | "
            )

#Have a loop that asks the user their desired request
while True:
    print("Choose an option: (Please enter"
          " the letter designated for each option)")
    print("-------------------------------------")
    option = input("(a) Enroll \n(b) Unenroll \n(d) Make Payment \n(e) What We Believe \n"
                   "(f) Show Balance \n(x) Exit \nEnter your option: ")
    print("-------------------------------------")
    if option.lower() == "a":
        nameOfChild = input("Enter your name: ")
        ageOfChild = int(input("Enter your age: "))

        person = MerryDay(nameOfChild, ageOfChild, 0, False)
        person.enroll()
        enrollments[person.name] = person
        MerryDay.save_enrollments()

    elif option.lower() == "b":
        nameOfChild = input("Enter your name: ")
        if nameOfChild in enrollments:
            enrollments[nameOfChild].unenroll()
            del enrollments[nameOfChild]
            MerryDay.save_enrollments()
            print(f"{nameOfChild} has been unenrolled.")

        else:
            print("You are not enrolled.")

    elif option.lower() == "z":
        password = input("Enter the password: ")
        if password == "MerryDay2026":
            print("Access granted.")

            while True:
                print("\nEmployee Menu")
                print("------------------------")
                choice = input("(a) Charge Everyone \n(b) View All Enrollments \n(c) Return to Main Menu")
                print("------------------------")

                if choice == "a":
                    MerryDay.charge_everyone()
                elif choice == "b":
                    MerryDay.show_all_enrollments()
                elif choice == "c":
                    break
                else:
                    print("Invalid choice!")

        else:
            print("Access denied! Incorrect password!")

    elif option.lower() == "d":
        nameOfChild = input("Enter your name: ")
        if nameOfChild in enrollments:
            enrollments[nameOfChild].make_payment()
            MerryDay.save_enrollments()
        else:
            print("You are not enrolled.")

    elif option.lower() == "e":
        MerryDay.show_beliefs()

    elif option.lower() == "f":
        nameOfChild = input("Enter your name: ")

        if nameOfChild in enrollments:
            enrollments[nameOfChild].show_balance()
        else:
            print("You are not enrolled.")

    elif option.lower() == "x":
        print("Thank you for using Merry Day!")
        break

    else:
        print("Try again! Invalid option.")




