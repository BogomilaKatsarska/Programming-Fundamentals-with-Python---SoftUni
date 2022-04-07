number_of_cars = int(input())
cars = {}

for _ in range (number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > cars[car]["fuel"]:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                removed_car = cars.pop(car)
                print(f"Time to sell the {car}!")

    elif command[0] == "Refuel":
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            fuel = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command[0] == "Revert":
        kilometers = int(command[2])
        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")