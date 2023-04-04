class Vehicle():
    def __init__(self, color, wheels, doors):
        self.__color = color
        self.__wheels = wheels
        self.__doors = doors

    def __str__(self):
        return "Color:{} \n Wheels: {} \n Doors:  {}".format(self.__color,self.__wheels,self.__doors)


class Car(Vehicle):
    def __init__(self, color, wheels, doors, speed, displacement):
        self.__speed = speed
        self.__displacement = displacement
        super().__init__(color,wheels,doors)

    def __str__(self):
        return "----------Car info------------\n {} \n Speed: {} \n desplacement: {}".format(super(Car, self).__str__()
                                                                                           ,self.__speed
                                                                                           ,self.__displacement)

car = Car("White",4,4,280,2000)
print(car.__str__())