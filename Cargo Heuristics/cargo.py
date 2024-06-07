import random
import math


def load_trucks(cargo, truck_capacity):
    cargo.sort(reverse=True)

    trucks = [[], []]

    for crate in cargo:
        if sum(trucks[0]) + crate <= truck_capacity:
            trucks[0].append(crate)
        elif sum(trucks[1]) + crate <= truck_capacity:
            trucks[1].append(crate)
        else:
            print("Crate is too heavy to fit in any truck")
    return trucks


total_weight = int(input("Enter the total weight of the cargo: "))
truck_capacity = math.ceil(total_weight / 2)

cargo = []

while sum(cargo) < total_weight:
    crate = random.randint(1, min(truck_capacity, total_weight - sum(cargo)))
    cargo.append(crate)

trucks = load_trucks(cargo, truck_capacity)

print(cargo, sum(cargo))
print("Truck 1:", trucks[0], "Total weight:", sum(trucks[0]))
print("Truck 2:", trucks[1], "Total weight:", sum(trucks[1]))
