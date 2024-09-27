class Warrior():                                            # создание класса Воина
    def __init__(self,name, power, endurance, hair_color):  # метод создания обьекта ( с атрибутами)
        self.name = name                                    # имя объекта          (характеристика)
        self.power = power                                  # сила объекта         (характеристика)
        self.endurance = endurance                          # выносливость объекта (характеристика)
        self.hair_color = hair_color                        # цвет волос  объекта  (характеристика)

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

    def info(self):                                         # метод вывода информации об объекте
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

war1 = Warrior(name= "Стёпа", power= 76, endurance= 54, hair_color= "коричневый")
war2 = Warrior(name= "Егор", power= 45, endurance= 23, hair_color= "блонд")

print(war1.name)
print(f"сила - {war1.power}")
print(f"выносливость - {war1.endurance}")
print(f"цвет волос - {war1.hair_color}")


war1.sleep()
war1.eat()
war1.attack()
war1.walk()
war1.info()

print(war2.name)
print(war2.power)
print(war2.endurance)
print(war2.hair_color)

war2.sleep()
war2.eat()
war2.attack()
war2.walk()
war2.info()