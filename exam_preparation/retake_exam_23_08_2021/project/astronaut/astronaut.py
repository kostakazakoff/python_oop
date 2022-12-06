from abc import ABC, abstractmethod


class Astronaut(ABC):
    BREATHE_VALUE = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.BREATHE_VALUE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        backpack_items = ', '.join(self.backpack) if self.backpack else 'none'
        return '\n'.join([f'Name: {self.name}', f'Oxygen: {self.oxygen}', f'Backpack items: {backpack_items}'])
