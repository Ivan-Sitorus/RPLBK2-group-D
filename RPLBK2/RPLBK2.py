from abc import ABC, abstractmethod

# Antarmuka besar yang menggabungkan semua fungsionalitas
class subject(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def rest(self):
        pass

# Kelas pekerja kantor yang bekerja, makan, dan beristirahat
class OfficeWorker(subject):
    def work(self):
        print("OfficeWorker is working.")

    def eat(self):
        print("OfficeWorker is eating.")

    def rest(self):
        print("OfficeWorker is resting.")

# Kelas robot yang hanya bekerja, tetapi dipaksa untuk mengimplementasikan semua metode
class Robot(subject):
    def work(self):
        print("Robot is working.")

    def eat(self):
        # Robot tidak makan, tetapi dipaksa untuk mengimplementasikan metode ini
        raise NotImplementedError("Robot doesn't eat.")

    def rest(self):
        # Robot tidak beristirahat, tetapi dipaksa untuk mengimplementasikan metode ini
        raise NotImplementedError("Robot doesn't rest.")

# Kelas hewan yang bisa makan dan istirahat, tetapi dipaksa untuk mengimplementasikan work()
class Animal(subject):
    def work(self):
        # Hewan tidak bekerja, tetapi dipaksa untuk mengimplementasikan metode ini
        raise NotImplementedError("Animal doesn't work.")

    def eat(self):
        print("Animal is eating.")

    def rest(self):
        print("Animal is resting.")

# Kelas atlet yang bekerja (berlatih), makan, dan beristirahat
class Athlete(subject):
    def work(self):
        print("Athlete is training.")

    def eat(self):
        print("Athlete is eating.")

    def rest(self):
        print("Athlete is resting.")

# Demo penggunaan
def main():
    # Instance OfficeWorker
    office_worker = OfficeWorker()
    office_worker.work()  # Output: OfficeWorker is working.
    office_worker.eat()   # Output: OfficeWorker is eating.
    office_worker.rest()  # Output: OfficeWorker is resting.

    print("-" * 30)

    # Instance Robot
    robot = Robot()
    robot.work()          # Output: Robot is working.
    
    try:
        robot.eat()       # Akan memunculkan error: NotImplementedError("Robot doesn't eat.")
    except NotImplementedError as e:
        print(e)

    try:
        robot.rest()      # Akan memunculkan error: NotImplementedError("Robot doesn't rest.")
    except NotImplementedError as e:
        print(e)

    print("-" * 30)

    # Instance Animal
    animal = Animal()
    
    try:
        animal.work()     # Akan memunculkan error: NotImplementedError("Animal doesn't work.")
    except NotImplementedError as e:
        print(e)

    animal.eat()          # Output: Animal is eating.
    animal.rest()         # Output: Animal is resting.

    print("-" * 30)

    # Instance Athlete
    athlete = Athlete()
    athlete.work()        # Output: Athlete is training.
    athlete.eat()         # Output: Athlete is eating.
    athlete.rest()        # Output: Athlete is resting.

if __name__ == "__main__":
    main()
