CARS = {
    "lamborghini gallardo": 59,
    "lamborghini huracan": 59,
    "ferrari f40": 49,
    "porsche boxster": 39,
    "audi a5": 39,
    "bmw i8": 39,
    "lotus elise": 30
}
ADDITIONAL_LAP_COST = 15
STANDARD_LAPS = 3

def display_welcome():
    print("SUPERCAR EXPERIENCE DAY - BOOKING SYSTEM")
    print("Available Cars:")
    for i, car in enumerate(CARS.keys(), 1):
        print(f"{i}. {car.title()} £{CARS[car]:.2f} (for 3 laps)")


def get_customer_details():
    print(f"CUSTOMER DETAILS", end="\n")
    
    name = input("Enter customer name: ")
    while not name.isalpha():
        print("Error: Name cannot be empty and must only contain alphabetical characters.")
        name = input("Enter customer name: ")
    name = name.strip()
    
    address = input("Enter customer address: ")
    while not address.replace(" ", "").replace(",", "").isalnum():
        print("Error: Address cannot be empty and must only contain alphanumeric characters, spaces, and commas.")
        address = input("Enter customer address: ")
    address = address.strip()
    
    phone = input("Enter customer phone number: ")
    phone = phone.replace(" ", "")
    while not (phone[1:len(phone)].isdigit() and ((phone[0:2] == "+44" and len(phone) <= 13) or (phone[0] == "0" and len(phone) <= 11))):
        print("Error: Phone number must be a valid UK phone number.")
        phone = input("Enter customer phone number: ")
    phone = phone.strip()
    
    return name, address, phone


def get_number_of_cars():
    print(f"\n\nNUMBER OF CARS", end="\n")
    
    while True:
        try:
            num_cars = int(input("How many cars would you like to drive (1-5)? "))
            if 1 <= num_cars <= 5:
                return num_cars
            else:
                print("Error: Please enter a number between 1 and 5.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_car_choices(num_cars):
    print("\n\nSELECT CARS", end="\n")
    
    car_list = list(CARS.keys())
    selected_cars = []
    
    for i in range(num_cars):
        print(f"Car {i + 1}:")
        for j, car in enumerate(car_list, 1):
            print(f"{j}. {car.title():<30} £{CARS[car]:.2f}")
        
        carSelected = True
        while carSelected:
            try:
                choice = int(input(f"\nSelect car {i + 1} (1-{len(car_list)}): "))
                if 1 <= choice <= len(car_list):
                    selected_cars.append(car_list[choice - 1])
                    carSelected = False
                else:
                    print(f"Error: Please enter a number between 1 and {len(car_list)}.")
            except ValueError:
                print("Error: Please enter a valid number.")
    
    return selected_cars


def get_additional_laps():
    print("\n\nADDITIONAL LAPS", end="\n")
    print(f"Each additional lap costs £{ADDITIONAL_LAP_COST:.2f}")
    
    while True:
        try:
            additional_laps = int(input("Enter number of additional laps (0 if none): "))
            if additional_laps >= 0:
                return additional_laps
            else:
                print("Error: Please enter a number greater than or equal to 0.")
        except ValueError:
            print("Error: Please enter a valid number.")


def calculate_costs(selected_cars, additional_laps):
    car_costs = {car: CARS[car] for car in selected_cars}
    subtotal_cars = sum(car_costs.values())

    subtotal_additional_lap = additional_laps * ADDITIONAL_LAP_COST
    
    total_cost = subtotal_cars + subtotal_additional_lap
    
    return car_costs, subtotal_cars, subtotal_additional_lap, total_cost


def display_bill(name, address, phone, selected_cars, additional_laps, 
                car_costs, subtotal_cars, subtotal_additional_lap, total_cost):
    print("\n\nSUPERCAR EXPERIENCE DAY - INVOICE", end="\n\n")
    
    print("CUSTOMER DETAILS:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}", end="\n\n")

    print("ORDER SUMMARY")
    print(f"Total number of cars chosen: {len(selected_cars)}")
    print(f"\nCars selected:")
    for i, car in enumerate(selected_cars, 1):
        print(f"  {i}. {car.title()}")
    
    if additional_laps > 0:
        print(f"\nTotal additional laps: {additional_laps}")
    else:
        print(f"\nTotal additional laps: None")

    print("COST BREAKDOWN")
    print("Cars (3 laps included):")
    for car in selected_cars:
        cost = CARS[car]
        print(f"    {car.title()} £{cost:.2f}")
    print(f"  Subtotal (Cars): £{subtotal_cars:.2f}")
    
    if additional_laps > 0:
        print(f"\nAdditional Laps:")
        print(f"  {additional_laps} laps x £{ADDITIONAL_LAP_COST:.2f} = £{subtotal_additional_lap:.2f}")

    print(f"TOTAL COST: £{total_cost:.2f}")
    print("\nThank you for choosing Supercar Experience Day!")


def main():
    display_welcome()
    
    name, address, phone = get_customer_details()
    
    num_cars = get_number_of_cars()
    selected_cars = get_car_choices(num_cars)
    
    additional_laps = get_additional_laps()
    
    car_costs, subtotal_cars, subtotal_additional_lap, total_cost = calculate_costs(
        selected_cars, additional_laps
    )
    
    display_bill(name, address, phone, selected_cars, additional_laps,
                car_costs, subtotal_cars, subtotal_additional_lap, total_cost)


if __name__ == "__main__":
    main()
