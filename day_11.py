from abc import ABC, abstractmethod
class ParkingSpot(ABC):
    @abstractmethod
    def park_vehicle(self):
        pass
class Sensor:
    def __init__(self, available=True):
        self.__available = available
    def check_availability(self):
        return self.__available
    def update_availability(self, status):
        self.__available = status

class CarParking(ParkingSpot):
    def park_vehicle(self):
        print("Car parked")

class BikeParking(ParkingSpot):
    def park_vehicle(self):
        print("Bike parked")
car_spot = CarParking()
bike_spot = BikeParking()
car_sensor = Sensor()
bike_sensor = Sensor()

print("Car Parking Spot:")
if car_sensor.check_availability():
    car_spot.park_vehicle()
    car_sensor.update_availability(True)
else:
    print("Car parking spot is not available.")

print("\nBike Parking Spot:")
if bike_sensor.check_availability():
    bike_spot.park_vehicle()
    bike_sensor.update_availability(True)
else:
    print("Bike parking spot is not available.")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
task 1: Coffee Shop Bill System
A coffee shop uses a computer to manage bills.
1. When a customer comes, the computer creates a new bill file.
2. It writes the customer details and first order.
3. If the customer orders more items, it adds them to the same bill.
4. When the customer wants to see the bill, the computer reads the file.
5. If the order is cancelled, the bill file is deleted.
'''
print("Task 1: Coffee Shop Bill System\n")
import os

name = input("Enter Customer Name: ")
filename = name + ".txt"

file = open(filename, "w")
file.write("Coffee Shop Bill\n")
file.write("Customer: " + name + "\n")
file.close()
print("Bill Created Successfully")
file = open(filename, "a")
file.write("Latte - 2 cups - 200\n")
file.close()
file = open(filename, "a")
file.write("Sandwitch - 2 - 80\n")
file.close()
print("Item Added Successfully")
print("----------")
file = open(filename, "r")
print(file.read())
file.close()
print("-------------")
os.remove(filename)
print("Order Cancelled")
print("Bill Deleted Successfully")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
task 2: File Handling
1. Write a program to create a text file and write a message into it.
2. Open a file in read mode and display its contents.
3. Write a program to append data to an existing file.
4. Read a file and display each line.
'''
print("Task 2: File Handling\n")

file = "example.txt"
f = open(file, "w")
f.write("Hello, this is a sample file.\nThis file contains just some example text.")
f.close()
f = open(file, "r")
content = f.read()
print("File Contents:\n", content)
f.close()
f = open(file, "a")
f.write("\nThis line is appended to the file.")
f.close()
f = open(file, "r")
print("Updated File Contents:")
for line in f:
    print(line.strip())
f.close()

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 1: Method Overriding  
Create:  
· Shape→area()  
· Rectangle →override area()
'''
print("Task 1: Method Overriding\n")

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
rect = Rectangle(5, 3)
print("Area of Rectangle:", rect.area())

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 2 : Movie Info 
Create a class Movie:  
· Attributes: title, rating  
· Method to check if rating is Hit (≥8) or Average
'''
print("Task 2: Movie Info\n")

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def check_rating(self):
        if self.rating >= 8:
            return "Hit"
        else:
            return "Average"
movie1 = Movie("Inception", 8.8)
movie2 = Movie("Some Average Movie", 6.5)
print(f"Movie: {movie1.title}, Rating: {movie1.rating}, Status: {movie1.check_rating()}")
print(f"Movie: {movie2.title}, Rating: {movie2.rating}, Status: {movie2.check_rating()}")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 3: Book Discount 
Create a class BookStore: 
· Attributes: book_name, price  
· Method discount() that applies 10% discount if price > 500
'''
print("Task 3: Book Discount\n")

class BookStore:
    def __init__(self, book_name, price):
        self.book_name = book_name
        self.price = price

    def discount(self):
        if self.price > 500:
            return self.price * 0.9
        else:
            return self.price
book1 = BookStore("Expensive Book", 600)
book2 = BookStore("Affordable Book", 300)
print(f"Book: {book1.book_name}, Original Price: {book1.price}, Discounted Price: {book1.discount()}")
print(f"Book: {book2.book_name}, Original Price: {book2.price}, Discounted Price: {book2.discount()}")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 4: Password Protection (Encapsulation)  
Create a class UserAccount:  
· Private variable __password  
· Methods to set and validate password length (>6)
'''
print("Task 4: Password Protection\n")

class UserAccount:
    def __init__(self):
        self.__password = None

    def set_password(self, password):
        if len(password) > 6:
            self.__password = password
            print("Password set successfully.")
        else:
            print("Password must be longer than 6 characters.")

    def validate_password(self, password):
        if self.__password is None:
            print("No password set.")
        elif self.__password == password:
            print("Password is valid.")
        else:
            print("Invalid password.")
user = UserAccount()
user.set_password("mysecretpassword")
user.validate_password("wrongpassword")
user.validate_password("mysecretpassword")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 5: Temperature Control (Encapsulation) 
Create a class Thermostat:  
· Private variable __temperature  
· Setter ensures temperature is between 16-30°C 
· Getter returns temperature
'''
print("Task 5: Temperature Control\n")

class Thermostat:
    def __init__(self):
        self.__temperature = None

    def set_temp(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
            print(f"Temperature set to {temp}°C.")
        else:
            print("Temperature must be between 16 and 30°C.")

    def get_temp(self):
        return self.__temperature
    
thermostat = Thermostat()
thermostat.set_temp(25)
print(f"Current Temperature: {thermostat.get_temp()}°C")
thermostat.set_temp(10)

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 6: Electronics Store (Inheritance)  
Create: 
· ElectronicItem → brand 
· WashingMachine → capacity  
Display both values.
'''
print("Task 6: Electronics Store\n")

class ElectronicItem:
    def __init__(self, brand):
        self.brand = brand

class WashingMachine(ElectronicItem):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity
wm = WashingMachine("LG", "7kg")
print(f"Washing Machine Brand: {wm.brand}, Capacity: {wm.capacity}")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 7: Media Player 
Create: 
· AudioPlayer →play_audio() 
· VideoPlayer →play_video()  
· SmartPlayer inherits both
'''
print("Task 7: Media Player\n")

class AudioPlayer:
    def play_audio(self):
        print("Playing audio")

class VideoPlayer:
    def play_video(self):
        print("Playing video")

class SmartPlayer(AudioPlayer, VideoPlayer):
    pass

smart_player = SmartPlayer()
smart_player.play_audio()
smart_player.play_video()

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################