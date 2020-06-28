class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_count(self):
        thickness_sm = 3 # sm
        mass_per_square = 30 # kg
        print('Mass', '=', f'{self._length*self._width*thickness_sm*mass_per_square/1000:.2f}', 'ton(s)')

mas_calucation = Road(5000, 20)
mas_calucation.mass_count()