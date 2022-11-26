from unittest import TestCase, main
from CarManager.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car('Volvo', 'V50', 10, 60)


if __name__ == '__main__':
    main()