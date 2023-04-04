class Vehicle():
    def __init__(self, color, wheels, doors):
        self.__color = color
        self.__wheels = wheels
        self.__doors = doors

    def __str__(self):
        return " Color: " + self.__color + "\n Wheels: " + str(self.__wheels) + "\n Doors: " + str(self.__doors)


class Car(Vehicle):
    def __init__(self, color, wheels, doors, speed, displacement):
        self.__speed = speed
        self.__displacement = displacement
        super().__init__(color,wheels,doors)

    def __str__(self):
        return "----------Car info------------\n" + super(Car, self).__str__() + " Speed: " + str(self.__speed) +\
               "\n desplacement: " + str(self.__displacement)

car = Car("White",4,4,280,2000)
print(car.__str__())