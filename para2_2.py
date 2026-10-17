class Student:
    def __init__(self, name, height=160):
        self.name = name
        self.height = height

    def say_height(self):
            print(f'My height is {self.height}')

    def say_name(self):
            print(f'My name is {self.name}')


student1 = Student('John', height=180)
student1.say_name()
student1.say_height()
