class Parkinglot:
    def __init__(self,hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_parking_fee(self,entry_time,exit_time):

        def kirish(x):
            return int(x)+1 if x-int(x) > 0 else int(x)
        time_spent = exit_time - entry_time
        parking_fee = kirish(time_spent) * self.hourly_rate
        return parking_fee
    
class Car:
    def __init__(self,car_number,entry_time,exit_time):
        self.car_number = car_number
        self.entry_time = entry_time
        self.exit_time = exit_time

    def calculate_parking_fee(self,entry_time,exit_time):

        def kirish(x):
            return int(x)+1 if x-int(x) > 0 else int(x)
        time_spent = self.exit_time - self.entry_time
        parking_fee = kirish(time_spent) * self.hourly_rate
        return parking_fee    
    
def get_user_input():
    car_number = input("Mashina raqamini kiriting namuna 85x244ga ko'rinishida: ")
    entry_time = float(input("Kirish vaqtini kiriting: "))
    exit_time = float(input("Chiqish vaqtini kiriting: "))
    return car_number , entry_time , exit_time

if __name__ == "__main__" :
    hourly_rate = 1000
    parking_lot = Parkinglot(hourly_rate)

    car_number, entry_time, exit_time = get_user_input()

    car=Car(car_number,entry_time,exit_time)
    parking_fee = car.calculate_parking_fee(hourly_rate)
        
    car_admission_format = f"Mashina raqami {car_number}, parkingfee {parking_fee} so'm"
    print(car_admission_format)
