class Client:
    def __init__(self, name, city, money):
        self.name = name
        self.city = city
        self.money = money

    def __str__(self):
        return f'"{self.name}. {self.city}. Balance: {self.money} rub."'

    def get_guests(self):
        return f'{self.name}, {self.city}'

Ivan_Petrov = Client('Ivan Petrov', 'Moscow', 50)
Sergey_Sidorov = Client('Sergey Sidorov', 'Saint-Petersbourg', 100)
Marina_Vasilieva = Client('Marina Vasilieva', 'Tula', 0)

List_of_guests = [Ivan_Petrov, Sergey_Sidorov, Marina_Vasilieva]
for guests in List_of_guests:
    print(guests.get_guests())
