class Warrior():
    def __init__(self,name, power, endurance, hair_color):          # метод создания обьекта
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):                                        # метод спать
        print(f"{self.name} лёг спать")
        self.endurance += 2                                 # добовляется выносливости 2 очка

    def eat(self):                                          # метод кушать
        print(f"{self.name} сел кушать")
        self.power += 1                                     # добовляется сила 1 очко

    def attack(self):                                       # метод атака
        print(f"{self.name} атакует")
        self.endurance -= 6                                 # отнимаем выносливости 6 очков

    def walk(self):                                         # метод ходить
        print(f"{self.name} ходит")

    def info(self):                                        # метод вывода информации об объекте
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")