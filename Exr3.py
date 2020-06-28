class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_icnome(self):
        print(self._income['wage'] + self._income['bonus'])


supplychain = Position('Alex', 'Vasilyev', 'Manager', 5000, 30)
supplychain.get_full_name()
supplychain.get_total_icnome()




