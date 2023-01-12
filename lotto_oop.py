import random
class Lotto:

    def __init__(self,n):
        self.n = n
        self.lotto_numbers =[]
        for i in range(n):
            self.lotto_numbers.append(sorted(random.sample(range(1,46),6)))

    def update_numbers(self):
        self.lotto_numbers =[]
        for i in range(self.n):
            self.lotto_numbers.append(sorted(random.sample(range(1,46),6)))
        return self.lotto_numbers

    def pprint(self):
        for numbers in self.lotto_numbers:
            print('여러분의 행운번호 !')
            print(numbers)
            print('=============')

