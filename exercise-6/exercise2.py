class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def __str__(self):
        return "-------Student data--------\n Name: {} \n Grade: {}\n The result is Exam {}".format(self.__name,
                                                                                                    self.__grade
                                                                                                    , self.result())

    def result(self):
        if self.__grade >= 5:
            return "approved"
        else:
            return "failure"


student1 = Student("Fran", 4.9)
student2 = Student("Rome", 5.1)
print(student1.__str__())
print(student2.__str__())
