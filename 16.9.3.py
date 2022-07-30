class Client:
    def __init__(self, name, city, money):
        self.name = name
        self.city = city
        self.money = money

    def __str__(self):
        return f'"{self.name}. {self.city}. Balance: {self.money} rub."'

Ivan_Petrov = Client('Ivan Petrov', 'Moscow', 50)

print(Ivan_Petrov)
