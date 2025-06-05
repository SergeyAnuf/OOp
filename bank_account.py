import random

class BankAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balans = 0
        self.account = self.generate_account()
        print(f'Создан аккаунт :{self.first_name} {self.last_name}')


    def generate_account(self):
        result = ''
        i = 1
        while i <= 16:
            result += str(random.randint(0, 9))
            i += 1
        print(result)
        return result


    def add_ballans(self, summ):
        self.balans = self.balans + summ
        print(f'Текущий баланс после пополнения: {self.balans}')


    def cash_out(self, substr):
        if substr > self.balans:
            print('Поменяйте сумму снятия')
        else:
            self.balans -= substr
            print(f'Текущий баланс после снятия: {self.balans}')


    def send_money(self, other_user, cash):
        if cash <= self.balans:
            self.balans -= cash
            other_user.balans += cash
        print(f'{other_user.first_name} получил {cash}')



user = BankAccount('Serg', 'An')

user.add_ballans(200)
#user.cash_out(200)

user1 = BankAccount('Serg', 'Ze')

user.send_money(user1, 200)

print(user1.balans)