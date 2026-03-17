# Supercar Experience Cost Calculator

# Price list (3 laps included)
car_prices = {
    1: ("Lamborghini Gallardo", 59),
    2: ("Lamborghini Huracan", 59),
    3: ("Ferrari F40", 49),
    4: ("Porsche Boxster", 39),
    5: ("Audi A5", 39),
    6: ("BMW i8", 39),
    7: ("Lotus Elise", 30)
}

ADDITIONAL_LAP_COST = 15
MAX_CARS = 5

print("=== Supercar Experience Booking System ===")

# Customer details
name = input("Enter customer name: ")
address = input("Enter customer address: ")
phone = input("Enter customer phone number: ")

# Number of cars
while True:
    try:
        num_cars = int(input("How many cars would the customer like to drive? (1-5): "))
        if 1 <= num_cars <= MAX_CARS:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except:
        print("Invalid input. Enter a number.")

chosen_cars = []
total_cost = 0

print("\nAvailable Cars (Price includes 3 laps):")
for key, value in car_prices.items():
    print(f"{key}. {value[0]} - £{value[1]:.2f}")

# Car selection
for i in range(num_cars):
    while True:
        try:
            choice = int(input(f"\nSelect car {i+1} (enter number 1-7): "))
            if choice in car_prices:
                car_name, price = car_prices[choice]
                chosen_cars.append(car_name)
                total_cost += price
                break
            else:
                print("Invalid car number.")
        except:
            print("Please enter a valid number.")

# Additional laps
while True:
    try:
        extra_laps = int(input("\nEnter number of additional laps required (0 if none): "))
        if extra_laps >= 0:
            break
        else:
            print("Enter 0 or a positive number.")
    except:
        print("Invalid input.")

extra_lap_cost = extra_laps * ADDITIONAL_LAP_COST
total_cost += extra_lap_cost

# Itemised Bill
print("\n===== SUPER CAR EXPERIENCE BILL =====")
print(f"Customer Name: {name}")
print(f"Address: {address}")
print(f"Phone: {phone}")

print("\nCars Chosen:")
for car in chosen_cars:
    print(f"- {car}")

print(f"\nTotal Cars Driven: {num_cars}")
print(f"Additional Laps: {extra_laps}")

print("\nCost Breakdown:")
for car in chosen_cars:
    for key, value in car_prices.items():
        if value[0] == car:
            print(f"{car}: £{value[1]:.2f}")

print(f"Additional Laps Cost: £{extra_lap_cost:.2f}")

print("\n-------------------------------------")
print(f"TOTAL COST: £{total_cost:.2f}")
print("-------------------------------------")
print("Thank you for booking a Supercar Experience!")