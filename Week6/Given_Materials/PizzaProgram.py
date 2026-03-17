# Pizza Program

# Constants
MIN_PIZZAS = 1
MAX_PIZZAS = 6

PIZZA_PRICES = {
    "small": 3.25,
    "medium": 5.50,
    "large": 7.15
}

TOPPING_PRICES = {
    0: 0,
    1: 0.75,
    2: 1.35,
    3: 2.00
}

DELIVERY_CHARGE = 2.50
DISCOUNT_RATE = 0.10


# Function to calculate topping price
def get_topping_price(num_toppings):
    if num_toppings >= 4:
        return 2.50
    return TOPPING_PRICES.get(num_toppings, 0)


# Customer Details
print("=== Pizza Order System ===")

name = input("Enter customer name: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

# Quantity validation
while True:
    try:
        quantity = int(input("Enter number of pizzas (1-6): "))
        if MIN_PIZZAS <= quantity <= MAX_PIZZAS:
            break
        else:
            print("Quantity must be between 1 and 6.")
    except:
        print("Invalid input. Enter a number.")

order_details = []
subtotal = 0

# Pizza order loop
for i in range(quantity):
    print(f"\nPizza {i+1}")

    while True:
        size = input("Enter size (small/medium/large): ").lower()
        if size in PIZZA_PRICES:
            break
        else:
            print("Invalid size. Choose small, medium, or large.")

    price = PIZZA_PRICES[size]

    while True:
        try:
            toppings = int(input("Number of extra toppings: "))
            if toppings >= 0:
                break
            else:
                print("Enter 0 or more toppings.")
        except:
            print("Invalid number.")

    topping_cost = get_topping_price(toppings)

    pizza_total = price + topping_cost
    subtotal += pizza_total

    order_details.append({
        "size": size,
        "base_price": price,
        "toppings": toppings,
        "topping_cost": topping_cost,
        "total": pizza_total
    })

# Delivery option
delivery = input("\nDelivery required? (yes/no): ").lower()
delivery_cost = DELIVERY_CHARGE if delivery == "yes" else 0

# Discount
discount = 0
if subtotal > 20:
    discount = subtotal * DISCOUNT_RATE

total = subtotal - discount + delivery_cost

# Itemised Bill
print("\n=== ITEMISED BILL ===")
print(f"Customer: {name}")
print(f"Address: {address}")
print(f"Phone: {phone}")

print("\nOrder Details:")
for i, pizza in enumerate(order_details, start=1):
    print(f"Pizza {i}: {pizza['size'].capitalize()}")
    print(f"  Base Price: £{pizza['base_price']:.2f}")
    print(f"  Extra Toppings: {pizza['toppings']} (£{pizza['topping_cost']:.2f})")
    print(f"  Pizza Total: £{pizza['total']:.2f}")

print(f"\nSubtotal: £{subtotal:.2f}")
print(f"Discount: -£{discount:.2f}")
print(f"Delivery Charge: £{delivery_cost:.2f}")

print(f"\nTOTAL TO PAY: £{total:.2f}")
print("Thank you for your order!")