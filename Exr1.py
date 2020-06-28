import time

class TrficLight:

    _color = ['Red', 'Yellow', 'Green']


    def running(self):
        print(self._color[0], 'light is on. Stop!')
        time.sleep(7)
        print(self._color[1], 'light is on. Prepare.')
        time.sleep(2)
        print(self._color
              [2], 'light is on. You can go.')
        time.sleep(2)

tl =  TrficLight()
tl.running()

