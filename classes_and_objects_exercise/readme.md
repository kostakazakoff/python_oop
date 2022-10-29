# Vet

Create a class called Vet. Upon initialization, it should receive a name (string). It should also have an instance attribute called animals (empty list by default).

There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; and space (5 by default). You should create 3 additional instance methods:
- register_animal(animal_name)
    - If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
    - Otherwise, returns "Not enough space"
- unregister_animal(animal_name)
    - If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
    - Otherwise, returns "{animal} not in the clinic"
- info()

Returns info about the vet, the number of animals in his list and the free space in the clinic:

"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


# Time
Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers).
The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59.
You should also create 3 additional instance methods:
- set_time(hours, minutes, seconds) - updates the time with the new values
- get_time() - returns "{hh}:{mm}:{ss}"
- next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)


# Account
Create a class called Account. Upon initialization, it should receive an id (number), a name (string), and a balance (integer; optional; 0 by default). The class should also have 3 additional instance methods:
- credit(amount) - adds the amount to the balance and returns the new balance
- debit(amount)
    - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance.
    - Otherwise, return "Amount exceeded balance"
- info() - returns "User {name} with account {id} has {balance} balance"


# Pizza Delivery
Create a class called PizzaDelivery. Upon initialization, it should receive a name (string), a price (float), and ingredients (dictionary). The class should also have an instance attribute ordered set to False by default. You should also create 3 additional instance methods:
- add_extra(ingredient: str, quantity: int, price_per_quantity: float):
    - If we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update the pizza price by adding the ingredient price for the given quantity
    - If we do not have this ingredient in our pizza, we should add it and update the pizza price
- remove_ingredient(ingredient: str, quantity: int, price_per_quantity: float):
    - If we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
    - If we have the ingredient, but we try to remove more than we have available, we should return the following message "Please check again the desired quantity of {ingredient}!"
    - Otherwise, remove the given quantity of the ingredient and update the pizza price by removing the ingredient price for the given quantity
- make_order()
    - Set the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared with {ingredient: quantity} and the price will be {price}lv.". The ingredients should be separated by a comma and a space ", "
    - Keep in mind that once the pizza is ordered, no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"