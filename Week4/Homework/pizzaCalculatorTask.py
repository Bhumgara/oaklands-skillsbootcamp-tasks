def getCustomerDetails():
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phone = input("Please enter your phone number: ")
    return name, address, phone

def getPizzaOrder():
    quantity = int(input("\nHow many pizzas would you like to order? "))
    pizzas = []

    while quantity < 1:
        print("You must order at least one pizza.")
        quantity = int(input("\nHow many pizzas would you like to order? "))

    while quantity > 6:
        print("You must order no more than six pizzas.")
        quantity = int(input("\nHow many pizzas would you like to order? "))

    for i in range(quantity):
        size = input(f"\nEnter the size of pizza {i+1} (small, medium, large): ")
        price = 0.00

        while price == 0.00:
            if size.lower() == 'small' or size.lower() == 's':
                price = 3.25
                size = 'small'
            elif size.lower() == 'medium' or size.lower() == 'm':
                price = 5.50
                size = 'medium'
            elif size.lower() == 'large' or size.lower() == 'l':
                price = 7.15
                size = 'large'
            else:
                size = input("Invalid size entered. Please try again.\n\nEnter the size of the pizza (small, medium, large): ")
                price = 0.00

        toppings = int(input(f"\nDo you want extra toppings on pizza {i+1}, if so, how many?: "))

        if toppings == 1:
            price += 0.75
        elif toppings == 2:
            price += 1.35
        elif toppings == 3:
            price += 2.00
        elif toppings >= 4:
            price += 2.50
        else:
            price += 0

        pizzas.append({"size": size, "toppings": toppings, "price": price})
    return pizzas

def getDeliveryOption():
    delivery = input("\nDo you want delivery? (yes/no): ")
    return delivery.lower() == 'yes' or delivery.lower() == 'y'

def calculateTotal(pizzas, delivery):
    total = sum(pizza["price"] for pizza in pizzas)
    if total > 20:
        total *= 0.9  # Apply 10% discount
    if delivery:
        total += 2.50
    return total

def printBill(name, address, phone, pizzas, delivery, total):
    print("\n--- Bill ---")
    print(f"Customer Name: {name.capitalize()}")
    print(f"Address: {address.capitalize()}")
    print(f"Phone: {phone}\n")

    for i, pizza in enumerate(pizzas, 1):
        toppings_str = f"Extra Toppings: {pizza['toppings']}" if pizza['toppings'] > 0 else "No Extra Toppings"
        print(f"Pizza {i}: {pizza['size'].capitalize()} ({toppings_str}) - £{pizza['price']:.2f}")

    if total > 20:
        print("\nDiscount Applied: 10% off for orders over £20")
    if delivery:
        print("Delivery Charge: £2.50")
    else:
        print("No Delivery Charge")

    print(f"\nTotal Cost: £{total:.2f}")

def main():
    name, address, phone = getCustomerDetails()
    pizzas = getPizzaOrder()
    delivery = getDeliveryOption()
    total = calculateTotal(pizzas, delivery)
    printBill(name, address, phone, pizzas, delivery, total)

main()