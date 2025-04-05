class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
        self.total = 0

    def readData(self):
        self.rollno = int(input("Enter roll number: "))
        self.mark1 = float(input("Enter mark 1: "))
        self.mark2 = float(input("Enter mark 2: "))

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll Number: {self.rollno}")
        print(f"Mark 1: {self.mark1}")
        print(f"Mark 2: {self.mark2}")
        print(f"Total: {self.total}")

def main():
    # Create an object of the Student class
    student = Student()

    # Invoke the readData method
    student.readData()

    # Invoke the computeTotal method
    student.computeTotal()

    # Invoke the printDetails method
    student.printDetails()

if __name__ == "__main__":
    main()
