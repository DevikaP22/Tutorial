class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def dataprint(self):
        return f"Name: {self.name}\nRoll Number: {self.roll_number}"

def main():
    # Create two instances of the Student class
    student1 = Student("John Doe", 101)
    student2 = Student("Jane Smith", 102)

    # Call the dataprint method for each instance
    print("Student 1:")
    print(student1.dataprint())
    print("\nStudent 2:")
    print(student2.dataprint())

if __name__ == "__main__":
    main()
