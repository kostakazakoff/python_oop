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


# Account
Create a single class called Account. Upon initialization, it should receive an owner (str) and a starting amount (int, optional, 0 by default). It should also have an attribute called _transactions (empty list). Create the following methods:
- handle_transaction(transaction_amount)
    - If the balance becomes less than zero, raise ValueError with the message "sorry cannot go in debt!" and break the transaction. 
    - Otherwise, complete it, save it and return a message "New balance: {account_balance}"
- add_transaction(amount) 
    - if the amount is not an integer, raise ValueError with the message "please use int for amount". 
    - Otherwise, check what the balance will be with the new transaction
        - If the balance becomes less than zero, raise ValueError with the message "sorry cannot go in debt!" and break the transaction. 
        - Otherwise, complete it and return a message "New balance: {account_balance}"
- balance() - a property that returns the sum between the amount and all the transactions
Implement the correct magic methods so the code in the example below works properly:
- When you print an account instance, the output should be in the format "Account of {owner} with starting amount: {amount}".
- When you print a representational string of an account instance, the output should be in the format "Account({owner}, {amount})".
- When you access the length of an account instance, you should receive the total number of transactions made.
- You should iterate over an account instance and receive each transaction as a result.
- You should be able to reverse the order of transactions by reversing an account instance.
- You should be able to compare (>, <, >=, <=, ==, !=) two account instances by their balance amount.
- When you concatenate two accounts, you should return a new account with a name - string in the format "{first_owner}&{second_owner}" and starting amount - the sum between their two. Both their transactions should be added to the new account.