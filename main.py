import random

class Student:
    print('hello teacher')
    self.money = 100
    def __init__(self):
        self.height = 175
        self.age = 14

student_mark = Student()
print(student_mark.height)
print(student_mark.age)

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.money += 5
    def to_sleep(self):
         print("I will sleep")
         self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
            self.to_study()
            self.gladness = 0
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:\
            print("Passed externally…")
            self.alive = False
            self.to_chill
    def end_of_day(self):
        print("Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")

def live(self, day):
    day = "Day" + str(day) + "of" +\
    self.name + "life"
    print(f"{day:=^50}")
    live_cube = random.randint(1, 3)
if live_cube == 1:
    self.to_sleep
elif live_cube == 2:\
    self.to_sleep()
elif live_cube == 3:
    self.to_chill()
    self.end_of_day()
    self.is_alive()
    mark = Student(name="mark")
for day in range(365):
    if mark.alive == False:
        break
    mark.live(day)