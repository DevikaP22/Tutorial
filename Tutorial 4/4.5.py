
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        return f"Name: {self.name}\nAge: {self.age}\nSalary: ${self.salary:,.2f}"

def main():

    person1 = Person("John Doe", 30, 50000)
    person2 = Person("Jane Smith", 25, 60000)

    
    print("Person 1:")
    print(person1.display())
    print("\nPerson 2:")
    print(person2.display())

if __name__ == "__main__":
    main()
