#
#  * 60. self in Python

class Car:
    wheels = 4
    
    def start_car(self):
        print('car started')
        
    def example_one(self):
        print(self.wheels)
        


fusca = Car()
fusca.start_car()
print(fusca.wheels)
x = type(fusca.wheels)
print(x)
print(fusca.example_one)
fusca.example_one()