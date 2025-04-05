class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        return f"The price of the {self.model} ({self.year}) is ${self.price:,.2f}"

def main():

    car1 = Car("Toyota Camry", 2022, 25000)
    car2 = Car("Honda Civic", 2020, 20000)


    print(car1.cost())
    print(car2.cost())

if __name__ == "__main__":
    main()
