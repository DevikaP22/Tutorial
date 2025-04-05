class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0.0

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        return f"Company: {self.company}\nModel: {self.model}\nPrice: ${self.price:,.2f}"

def main():
    
    mobile = Mobile()

    
    mobile.set_details("Apple", "iPhone 14", 999.99)

    
    print(mobile.display_details())

if __name__ == "__main__":
    main()
