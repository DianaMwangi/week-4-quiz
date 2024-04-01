class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gender:", self.gender)

person_class=person("Jane",30,"Female")

person_class.introduce()