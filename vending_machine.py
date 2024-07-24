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

    def start(self):
        self.display_available_drinks()

    def display_available_drinks(self):
        print("======================================================================")
        print("Welcome to the Axrail Vending :Machine!\nHere are a list of beverages available: ")
        print("(Disclaimer: The sale of alcoholic beverages in Malaysia is PROHIBITED for Muslims and to those under "
              "the age of 21)")
        print("======================================================================")
        for drink, price in self.drinks.items():
            print(f"{drink}: {self.currency}{price}")

