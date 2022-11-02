class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 0
    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power