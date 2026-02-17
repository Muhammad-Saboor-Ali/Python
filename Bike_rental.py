class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"\nAvailable bikes: {self.stock}")

    def rent_hourly(self, num_bikes):
        if num_bikes <= 0:
            print("Number of bikes should be positive!")
            return None
        elif num_bikes > self.stock:
            print("Sorry! Not enough bikes available.")
            return None
        else:
            self.stock -= num_bikes
            print(f"You rented {num_bikes} bike(s) on hourly basis.")
            return num_bikes, "hourly"

    def rent_daily(self, num_bikes):
        if num_bikes <= 0:
            print("Number of bikes should be positive!")
            return None
        elif num_bikes > self.stock:
            print("Sorry! Not enough bikes available.")
            return None
        else:
            self.stock -= num_bikes
            print(f"You rented {num_bikes} bike(s) on daily basis.")
            return num_bikes, "daily"

    def return_bike(self, request):
        if request is None:
            print("No bikes were rented.")
            return

        num_bikes, rental_type, time = request
        bill = 0

        if rental_type == "hourly":
            bill = time * 5 * num_bikes   # $5 per hour
        elif rental_type == "daily":
            bill = time * 20 * num_bikes  # $20 per day

        self.stock += num_bikes
        print(f"\nReturned {num_bikes} bike(s).")
        print(f"Total bill: ${bill}")


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_type = None
        self.time = 0

    def request_bike(self):
        try:
            bikes = int(input("How many bikes would you like to rent? "))
            return bikes
        except ValueError:
            print("Invalid input. Enter a number.")
            return -1

    def return_bike(self):
        if self.bikes == 0:
            return None
        try:
            time = int(input("Enter rental duration (hours/days): "))
        except ValueError:
            print("Invalid input.")
            return None
        return self.bikes, self.rental_type, time


# ----------- Main Program -----------

shop = BikeRental(20)   # 20 bikes in stock
customer = Customer()

while True:
    print("\n Bike Rental System ")
    print("1. Display available bikes")
    print("2. Rent bike on hourly basis (Rs.150 per hour)")
    print("3. Rent bike on daily basis (Rs.2500 per day)")
    print("4. Return bike")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        shop.display_stock()

    elif choice == "2":
        bikes = customer.request_bike()
        request = shop.rent_hourly(bikes)
        if request:
            customer.bikes, customer.rental_type = request

    elif choice == "3":
        bikes = customer.request_bike()
        request = shop.rent_daily(bikes)
        if request:
            customer.bikes, customer.rental_type = request

    elif choice == "4":
        request = customer.return_bike()
        shop.return_bike(request)
        customer.bikes = 0

    elif choice == "5":
        print("Thank you for using Bike Rental System 🚲")
        break

    else:
        print("Invalid choice! Please try again.")

