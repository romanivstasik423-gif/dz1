class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happy = 50
        self.energy = 50

    def feed(self):
        if self.hunger > 50:
            self.hunger -= 20
            self.energy += 5
            print(f"{self.name} поїв. Смачно!")
        else:
            print(f"cat {self.name} не хоче їсти.")



class student:
    def __init__(self, name):
        self.name = name
        self.happines = 50
        self.money = 100

        def to_study(self):
            print("час заробляти")
            self.happines += 0.15
            self.money += 5


        def to_chilling(self):
            print("час полежати")
            self.hapinnes += 2

        def clean_room(self):
            print("час помити кімнату")
            self.happines -= 1
            self.money += 1

            def is_alive(self):
                if self.money < -0.5:
                    print("без роботи")
                    self.alive = False
                elif self.happines <= 0:
                    print("Дипресія")
                    self.alive = False
                elif self.happines > 5:
                    print("молодець")
                    self.alive = False


