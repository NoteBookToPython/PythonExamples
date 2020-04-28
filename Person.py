class Person:
    def __init__ ( self, name, age ):
        self.person_name = name
        self.__person_age = age #declaring a variable private in python

    def birthday ( self ):
        self.person_age += 1

    def getName ( self ):
        return self.person_name


bob=Person('Bob',32)
print(bob.getName())

bob.birthday()
print(bob.person_age)