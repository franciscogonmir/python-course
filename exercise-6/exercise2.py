class Student:
    __name = ""
    __grade = -1

    def askName(self):
        self.__name = input("Enter your name: ")

    def askGrade(self):
        self.__grade =  float(input("Enter your grade: "))

    def __str__(self):
        return "-------Student data--------\n" + " Name: " + self.__name \
               + "\n Grade: " + str(self.__grade) \
               + "\n The result is Exam " + self.result()

    def result(self):
        if self.__grade >= 5:
            return "approved"
        else:
            return "failure"


student = Student()
student.askName()
student.askGrade()
print(student.__str__())