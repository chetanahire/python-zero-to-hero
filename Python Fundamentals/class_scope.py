class Student:
    name = 'suraj'

    def print_name(self):
        # print(name) # we can access name vairable directly
        print(self.name)
        print(Student.name)

s = Student()
s.print_name()