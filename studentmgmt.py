class Student :
    school = 'xyz college'
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def _display_info(self):
        print(f"\nName : {self.name}\nAge : {self.age}\nSchool : {self.school}")


student1 = Student("John", 20)
student1.introduce();
student1._display_info()
student2 = Student("Mike", 21)
student2.introduce();