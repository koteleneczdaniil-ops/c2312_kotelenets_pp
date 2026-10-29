import random

brand_of_car = {
    'BMW' : {'fuel': 100, 'strength': 100, 'consumption': 6},
    'Lada' : {'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo' : {'fuel': 120, 'strength': 150, 'consumption': 8},
    'Ferrari' : {'fuel': 80, 'strength': 120, 'consumption': 14}
}
job_list = {
    'Java developer': {'salary': 50, 'gladness_less': 10},
    'Python developer': {'salary': 40, 'gladness_less': 3},
    'C++ developer': {'salary': 45, 'gladness_less': 25},
    'Rust developer': {'salary': 35, 'gladness_less': 1}
}
hobby_list = {
    'Drawing': {'gladness_plus': 5},
    'collector': {'gladness_plus':2},
    'taking photos':  {'gladness_plus': 10}
}



class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.home = home
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def hobby(self):
        self.gladness = self.gladness + (hobby_list[self.job]['gladness_plus'])
        print('Gonna go do my favourite hobby ! Yay')


    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('i buy fuel !')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('i buy food !')
            self.money -= 50
            self.home.food += 50
        elif manage == 'sweets':
            print('HOORAY ! SWEETS !')
            self.gladness += 10
            self.satiety += 2
            self.money-= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -=50

    def days_indexes(self, day):
        mes1 = f'Today is the {day} day of {self.name}s life !'
        print(f'{mes1:=^50}')
        mes2 = f'{self.name}s indexes'
        print(f'{mes2:-^50}')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        mes3 = f'Home indexes'
        print(f'{mes3:-^50}')
        print(f'Money - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        mes4 = f'{self.car.brand} car indexes'
        print(f'{mes4:-^50}')
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')


    def is_alive(self):
        if self.gladness < 0:
            print('depression...')
            return False

        if self.satiety < 0:
            print('Dead x')
            return False

        if self.money < -500:
            print('Bankrupt...')
            return False

    def live(self, day):

        if self.is_alive()== False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car ! {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f'I got a job ! {self.job.job} with salary of {self.job.salary} $ !')
        if self.hobby is None:
            self.hobby()

        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety > 20:
            print('Ill go eat something... im really hungry.')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('Ill go clean my house... its so messy.')
                self.clean_home()
            else:
                print('Im gonna go chill...im so tired...')
                self.chill()
        elif self.money < 0:
            print('Lock in ! Start working !')
            self.work()
        elif self.car.strenght < 15:
            print('I need to repair my car !')
            self.to_repair()
        elif dice == 1:
            print('Im gonna go chill...im so tired...')
            self.chill()
        elif dice == 2:
            print('Lock in ! Start working !')
            self.work()
        elif dice == 3:
            print('cleaning time...ugh')
            self.clean_home()
        elif dice == 4:
            print('Time for treats ! Yummers')
            self.shopping(manage='sweets')

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):

        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move !')
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

class  Hobby:
    def __init__(self, hobby_list):
        self.hobby = random.choice(list(hobby_list))
        self.gladness_plus = hobby_list[self.hobby]['gladness_plus']

vasya_man = Human(name='Vasya')

for day in range(1, 8):
    if vasya_man.live(day) == False:
        break