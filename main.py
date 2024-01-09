class Parkinglot:
    def init(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_parking_fee(self, entry_time, exit_time):
        def kirish(x):
            return int(x) + 1 if x - int(x) > 0 else int(x)
        time_spent = exit_time - entry_time
        parking_fee = kirish(time_spent) * self.hourly_rate
        return parking_fee

class Car:
    def init(self, car_number, entry_time, exit_time):
        self.car_number = car_number
        self.entry_time = entry_time
        self.exit_time = exit_time

    def calculate_parking_fee(self, hourly_rate):
        self.hourly_rate = hourly_rate
        def kirish(x):
            return int(x) + 1 if x - int(x) > 0 else int(x)
        time_spent = self.exit_time - self.entry_time
        parking_fee = kirish(time_spent) * self.hourly_rate
        return parking_fee

    def display_number(self):
        print(f"Car Numbers: {self.car_number}")


def get_user_input():
    car_number = input("Enter car number (e.g., 85x244): ")
    entry_time = float(input("Enter entry time: "))
    exit_time = float(input("Enter exit time: "))
    davom_etish = input("Do you want to continue? Enter yes/no: ")
    return car_number, entry_time, exit_time, davom_etish


if __name__ == "__main__":
    hourly_rate = 1000
    parking_lot = Parkinglot()

    car_number, entry_time, exit_time, davom_etish = get_user_input()

    car = Car(car_number, entry_time, exit_time)
    parking_fee = car.calculate_parking_fee(hourly_rate)
    car.display_number()

    car_admission_format = f"Car number: {car_number}, parking fee: {parking_fee} UZS"
    print(car_admission_format)

    while True:
        choice = input("Welcome to the car service. Choose (1) to enter parking fee, (2) to exit: ")

        if choice == '2':
            print("Goodbye, stay safe!")
            break

        if choice not in ['1', '2']:
            print("Invalid choice, please try again.")
            continue

        if choice == '1':
            car.calculate_parking_fee(hourly_rate)
            car.display_number()