class Student(object):
    count = 1

    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.__age = age
        self.count += 1

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get__age(self):
        return self.__age

    def set__age(self, age):
        if 12 < age < 16:
            self.__age = age
        else:
            raise ValueError('wrong age')


bart = Student('Bart Simpson', 59, 16)
print(bart.count)
lisa = Student('Lisa Simpson', 87, 15)
print(lisa.count)
bart.print_score()
lisa.print_score()
print(lisa.name, lisa.get_grade())
print(lisa.get__age())
lisa.set__age(14)
print(lisa.get__age())
# bart.set__age(16)
print(Student.count)
