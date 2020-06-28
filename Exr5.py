class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовка!")


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Это {self.title}. Запускается отрисовка ручкой синего цвета!")


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Это {self.title}. Запускается отрисовка черным карандашом жесткостью HB!")


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Это {self.title}. Запускается отрисовка красным маркером!")

stationary_exmpl  = Stationary('Some Stationary')
stationary_exmpl.draw()

pen_example = Pen('Ручка')
pen_example.draw()

pencil_example = Pencil('Карандаш')
pencil_example.draw()

handle_example = Handle('Маркер')
handle_example.draw()