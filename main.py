print('Hello World')
class Student:
    def __init__(self,name,age,grade):
        """Initializing a student object"""
        self.name = name
        self.age = age
        self.grade = grade

    def Display_info(self):
        print(f"Name :{self.name}")
        print(f"Name :{self.age}")
        print(f"Name :{self.grade}")

    def is_underage(self):
        if self.age < 18:
            return True
        else:
            return False


student1 = Student("John",20,"A")
student2 = Student("Jane",17,"B")

print(student1.Display_info())
print(student2.is_underage())