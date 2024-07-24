class AxrailVendingMachine:
    def __init__(self):
        # Assumption: Drinks are to be hardcoded, customer cannot add or remove drinks
        # Will use a hash map here, to map the drinks to the price.
        # Prices shall be integers (In your code, you can have a few drinks as your items with any price (no coin))
        self.drinks = {
            "Coke": 3,
            "100 Plus": 3,
            "Gatorade": 4,
            "Whiskey": 299,
            "Absolute Vodka": 250,
            "Bombay Sapphire Dry Gin": 60
        }

        self.currency = "RM"

        self.acceptedNotes = [100, 50, 20, 10, 5, 1]  # Assumption 2: as per standard Malaysian RM Notes

    def display_available_drinks(self):
        print("======================================================================")
        print("Welcome to the Axrail Vending :Machine!\nHere are a list of beverages available: ")
        print("(Disclaimer: The sale of alcoholic beverages in Malaysia is PROHIBITED for Muslims and to those under "
              "the age of 21)")
        print("======================================================================")
        for drink, price in self.drinks.items():
            print(f"{drink}: {self.currency}{price}")

    def choose_drinks(self):
        while True:
            drink_choice = input("Please select a drink: ")
            if drink_choice in self.drinks:
                return drink_choice
            else:
                print("Sorry! This drink does not exist in our machine. Please try again.")

    def make_payment(self, cost, drink_choice):
        while True:
            try:
                amount_inserted = int(input(f"Total amount due is {self.currency}{cost}. Please insert cash in RM: "))
                if amount_inserted < cost:
                    print("Sorry, the amount entered is insufficient. "
                          " Please try again or 'Cancel' to cancel purchase.")
                elif amount_inserted == cost:
                    print(f"Exact amount inserted, no change returned. Thank you and enjoy your {drink_choice}!")
                    return amount_inserted
                else:
                    return amount_inserted
            except ValueError:
                print("Sorry, your input is invalid. The transaction has been canceled.")
                return False

    # function to calculate the change
    def calc_change(self, change):
        result = []
        for note in self.acceptedNotes:
            count, change = divmod(change, note)
            result.append((note, count))
        return result

    def buy_drink(self):
        self.display_available_drinks()
        drink_choice = self.choose_drinks()
        cost = self.drinks[drink_choice]

        amount_inserted = self.make_payment(cost, drink_choice)

        try:
            if not amount_inserted:
                print("Please try again.")
            elif amount_inserted == cost:
                pass
            else:
                change = amount_inserted - cost
                change_notes = self.calc_change(change)

                print(f"Thank you and enjoy your {drink_choice}!")
                print("Don't forget to take your change: ")
                for note, count in change_notes:
                    if count > 0:
                        print(f"{self.currency}{note} x {count} -->", self.currency, str(note * count))
        except TypeError:
            return "An invalid input has resulted in an error."
