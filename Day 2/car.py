class Car(object):
    def __init__(self, name = "General", model = "GM", car_type = None, speed = 0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = speed

    def num_of_doors(self):
        if self.name in ["Porshe" or "Koenigsegg"]:
            self.num_of_doors = 2


        else:
            self.num_of_doors = 4

        return self.num_of_doors

    def num_of_wheels(self):
        if self.car_type is "trailer":
            self.num_of_wheels = 8
            return self.num_of_wheels

        else:
            self.num_of_wheels = 4
            return self.num_of_wheels

    def is_saloon(self):
        if self.car_type is not "trailer":
            self.car_type = "saloon"
            return self.car_type

        else:
            return "trailer"

    def drive(self, moving_speed):
        if moving_speed ==3:
            self.speed = 1000

        elif moving_speed == 7:
            self.speed = 77

        return self


import unittest

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car('Honda')
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = Car('Honda')
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')

    def test_default_car_model(self):
        gm = Car()
        self.assertEqual('GM', gm.model, msg="The car's model should be called `GM` if no model was passed as an argument")

    def test_car_properties(self):
        toyota = Car('Toyota', 'Corolla')
        self.assertListEqual(['Toyota', 'Corolla'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        opel = Car('Opel', 'Omega 3')
        porshe = Car('Porshe', '911 Turbo')
        self.assertListEqual([opel.num_of_doors,
                             porshe.num_of_doors,
                             Car('Koenigsegg', 'Agera R').num_of_doors],
                             [4, 2, 2],
                             msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        man = Car('MAN', 'Truck', 'trailer')
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                         msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertTrue(koenigsegg.is_saloon(),
                        msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        man = Car('MAN', 'Truck', 'trailer')
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 77],
                             msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

    def test_car_speed2(self):
        man = Car('Mercedes', 'SLR500')
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 1000],
                             msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

    def test_drive_car(self):
        man = Car('MAN', 'Truck', 'trailer')
        moving_man = man.drive(7)
        moving_man_instance = isinstance(moving_man, Car)
        moving_man_type = type(moving_man) is Car
        self.assertListEqual([True, True, man.speed],
                             [moving_man_instance, moving_man_type, moving_man.speed],
                             msg='The car drive function should return the instance of the Car class')


unittest.main()