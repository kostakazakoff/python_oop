# Vehicle
Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization. They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.


# Groups
Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str). Implement the needed magic methods so that:
- Each person could be represented by their names, separated by a single space.
- When you concatenate two people, you should return a new instance of a person who will take the first name from the first person and the surname from the second person.

Create another class called Group. Upon initialization, it should receive a name (str) and people (list of Person instances). Implement the needed magic methods so that:
- When you access the length of a group instance, you should receive the total number of people in the group.
- When you concatenate two groups, you should return a new instance of a group which will have a name -string in the format "{first_name} {second_name}" and all the people in the two groups will participate in the new one too.
- Each group should be represented in the format "Group {name} with members {members' names separated by comma and space}"
- You could iterate over a group, and each person (element of the group) should be represented in the format "Person {index}: {person's name}"