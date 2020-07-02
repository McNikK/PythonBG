class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = round(abs(number_of_cells))

    def __str__(self):
        return self.number_of_cells*'*'

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print('Уменьшаемая клетка должна быть больше чем вычитаемая клетка!')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        try:
            return Cell(round(self.number_of_cells / other.number_of_cells))
        except ZeroDivisionError:
            return print('На ноль делить нельзя!')


    def make_order(self, division):
        balance = self.number_of_cells % division
        exact_division = self.number_of_cells//division
        if self.number_of_cells > division:
            print(f'{"*"*division}\\n'*exact_division+f'{"*"*balance}')
        else:
            print(f'{"*"*self.number_of_cells}\\n')


cell1 = Cell(3)
cell2 = Cell(16)

print(cell1+cell2, 'adding')
print(cell2/cell1, 'division')
print(cell2 - cell1, 'sub')
print(cell2*cell1, 'multiplication')

cell2.make_order(5)
