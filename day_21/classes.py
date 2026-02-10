class Person:
    def __init__ (self, name="Adam", age="20", city="Warszawa"):
    # self allows to attach parameter to the class
        self.name =name
        self.age = age
        self.city = city
        self.skills = []
    def person_info(self):
        return f'Mam an imię {self.name}, i mam {self.age} lat.'
    def add_skill(self, skill):
        self.skills.append(skill)

class Student(Person):
    def __init__ (self, name="Adam", age="20", city="Warszawa", year=1):
        self.year = year
        super().__init__(name, age, city)
    def person_info(self):
        if self.year == 1:
            year = "junior"
        elif self.year == 2:
            year = "sophomore"
        else:
            year = "senior"
        return f'Mam an imię {self.name}, i mam {self.age} lat i jestem {year}.'


s1 = Student("Ania")
print(s1.person_info())

p1= Person('Pola', '21', 'Łódź')
print(p1.person_info())

p2 = Person()
print(p2.person_info())

p1.add_skill("Taniec")

print(p1.skills)



