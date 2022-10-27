# Shop
Create a class called Shop. Upon initialization, it should receive a name (string) and items (list). Create a method called get_items_count() which should return the number of items in the store.

# Hero
Create a class called Hero. Upon initialization, it should receive a name (string) and health (number). Create two additional methods:
- defend(damage) - reduce the given damage from the hero's health:
    - if the health become 0 or less, set it to 0 and return "{name} was defeated"
- heal(amount) - increase the health of the hero with the given amount


# Employee
Create class Employee. Upon initialization, it should receive id (number), first_name (string), last_name (string) and salary (number).
Create 3 additional instance methods:
- get_full_name() - returns "{first_name} {last_name}"
- get_annual_salary() - returns the total salary for 12 months
- raise_salary(amount) - increases the salary by the given amount and returns the new salary


# Cup
Create a class called Cup. Upon initialization, it should receive size (integer) and quantity (an integer representing how much liquid is in it).
The class should have two methods:
- fill(quantity) that will increase the amount of liquid in the cup with the given quantity (if there is space in the cup, otherwise ignore).
- status() that will return the amount of free space left in the cup.
