class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0.0

    def get_details(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter book author: ")
        self.cost = float(input("Enter book cost: "))

    def print_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost: ${self.cost:,.2f}")

def main():

    book = Book()

    
    book.get_details()

    
    print("\nBook Details:")
    book.print_details()

if __name__ == "__main__":
    main()
