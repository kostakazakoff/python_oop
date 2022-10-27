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


# Flower
Create a class called Flower. Upon initialization, the class should receive a name (string) and a water_requirements (number). The flower should also have an instance attribute called is_happy (False by default).
Add two additional methods to the class:
- water(quantity) - it will water the flower. Each time check if the quantity is greater than or equal to the required. If it is - the flower becomes happy (set is_happy to True).
- status() - it should return "{name} is happy" if the flower is happy, otherwise it should return "{name} is not happy".


# Steam User
Create a class called SteamUser. Upon initialization, it should receive a username (string) and games (list). It should also have an attribute called played_hours (0 by default). Add three methods to the class:
- play(game, hours)
    - f the game is in the game list, increase the played_hours by the given hours and return "{username} is playing {game}"
    - Otherwise, return "{game} is not in library"
- buy_game(game)
    - If the game is not in the game list, add it and return "{username} bought {game}"
    - Otherwise, return "{game} is already in your library"
- status() - returns the following:

    "{username} has {games_count} games. Total play time: {played_hours}"
