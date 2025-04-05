class RECTANGLE:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def find_center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return center_x, center_y

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

def main():
 
    rectangle1 = RECTANGLE(10, 20, 0, 0)
    rectangle2 = RECTANGLE(5, 15, 3, 4)

    
    print("Rectangle 1:")
    print(f"Center: {rectangle1.find_center()}")
    print(f"Area: {rectangle1.calculate_area()}")
    print(f"Perimeter: {rectangle1.calculate_perimeter()}")

    print("\nRectangle 2:")
    print(f"Center: {rectangle2.find_center()}")
    print(f"Area: {rectangle2.calculate_area()}")
    print(f"Perimeter: {rectangle2.calculate_perimeter()}")

if __name__ == "__main__":
    main()
