class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        """Displays the car details in a clean format."""
        print("\n" + "=" * 30)
        print("     VEHICLE DETAILS")
        print("=" * 30)
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
        print("=" * 30)


def main():
    print("Welcome to the Car Information Entry System!\n")

    vehicle_type = "car"

    year = input("Enter the year: ").strip()
    make = input("Enter the make: ").strip().capitalize()
    model = input("Enter the model: ").strip().capitalize()

    doors = input("Enter the number of doors (2 or 4): ").strip()
    while doors not in ["2", "4"]:
        doors = input("Invalid input. Please enter 2 or 4 for doors: ").strip()

    roof = input("Enter the type of roof (solid or sun roof): ").strip().lower()
    while roof not in ["solid", "sun roof"]:
        roof = input("Invalid input. Please enter 'solid' or 'sun roof': ").strip().lower()

    car = Automobile(
        vehicle_type=vehicle_type,
        year=year,
        make=make,
        model=model,
        doors=doors,
        roof=roof
    )

    car.display_info()

if __name__ == "__main__":
    main()