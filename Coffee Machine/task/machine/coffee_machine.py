class CoffeeMachine:
    n_coffee_machines = 0

    def __new__(cls):
        if cls.n_coffee_machines == 0:
            return object.__new__(cls)
        else:
            return None

    def __init__(self):
        self.water_available = 400
        self.milk_available = 540
        self.coffee_beans_available = 120
        self.disposable_cups_available = 9
        self.money = 550
        self.state = "choosing_an_action"

    def show_message(self):
        print("The coffee machine has:")
        print(f"{self.water_available} ml of water")
        print(f"{self.milk_available} ml of milk")
        print(f"{self.coffee_beans_available} g of coffee beans")
        print(f"{self.disposable_cups_available} disposable cups")
        print(f"${self.money} of money")

    def coffee_maker(self, water, milk, coffee_beans, price):
        if water > self.water_available:
            print("Sorry, not enough water!")
        elif milk > self.milk_available:
            print("Sorry, not enough milk!")
        elif coffee_beans > self.coffee_beans_available:
            print("Sorry, not enough coffee beans")
        else:
            print("I have enough resources, making you a coffee!")

            self.water_available -= water
            self.milk_available -= milk
            self.coffee_beans_available -= coffee_beans
            self.disposable_cups_available -= 1
            self.money += price

    def action(self, opt):
        if self.state == "choosing_an_action":
            if opt == "buy":
                self.state = "choosing_a_type_of_coffee"
            elif opt == "fill":
                self.fill_machine()
            elif opt == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif opt == "remaining":
                self.show_message()
            elif opt == "exit":
                exit()

        if self.state == "choosing_a_type_of_coffee":
            self.buy()
            self.state = "choosing_an_action"

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "1":
            self.coffee_maker(250, 0, 16, 4)
        elif coffee_type == "2":
            self.coffee_maker(350, 75, 20, 7)
        elif coffee_type == "3":
            self.coffee_maker(200, 100, 12, 6)
        elif coffee_type == "back":
            return

    def fill_machine(self):
        water = int(input("Write how many ml of water you want to add:"))
        milk = int(input("Write how many ml of milk you want to add: "))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:"))
        disposable_cups = int(input("Write how many disposable cups you want to add:"))

        self.water_available += water
        self.milk_available += milk
        self.coffee_beans_available += coffee_beans
        self.disposable_cups_available += disposable_cups


coffee_machine = CoffeeMachine()
while True:
    option = input("\nWrite action (buy, fill, take, remaining, exit):")
    coffee_machine.action(option)
