from databaseconnection import DatabaseConnection

d1 = DatabaseConnection()
d2 = DatabaseConnection()
d3 = DatabaseConnection()

for conn in d1, d2, d3:
    print(id(conn))
print()

class Dog:
    pass

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

for dog in dog1, dog2, dog3:
    print(id(dog))
