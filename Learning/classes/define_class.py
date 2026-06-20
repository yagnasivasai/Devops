class person:
    def __init__(self,name,educcation,country):
        self.name=name
        self.educcation=educcation
        self.country=country



    def details(self):
        print("my name is " + self.name)
        print("my education is " + self.educcation)
        print("and my country is " + self.country)

person_details = person("yagnya","MCA","India")
person_details.details()
