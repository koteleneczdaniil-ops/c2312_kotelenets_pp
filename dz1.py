import random


class dog:
    def __init__(self,name):
        self.name = name
        self.saturation = 50
        self.energy = 100
        self.alive = True

    def to_play(self):
        print('flying')
        self.saturation -= 5
        self.energy -= 1

    def to_eat(self):
        print('eating...')
        self.saturation += 3
        self.energy += 2

    def to_sleep(self):
        print('sleeping...')
        self.energy += 3


    def is_alive(self):
        if self.saturation < -1:
            print('doggy died because he didnt eat')
            self.alive = False
        elif self.energy <= 0:
            print('doggy died because of lack of energy')
            self.alive = False

    def end_of_day(self):
        print(f'saturation = {self.saturation}')
        print(f'energy = {round (self.energy, 2)}')

    def live(self, day):
        mess = f'Day {day} of {self.name}s life'
        print(f'{mess:=^30}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_play()
        elif live_cube == 3:
            self.to_sleep()

        self.end_of_day()
        self.is_alive()


dog = dog('doggy')
for day in range(365):
    if not dog.alive:
        break
    dog.live(day)