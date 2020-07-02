from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, H=None, V=None):
        self.H = H
        self.V = V

    @abstractmethod
    def fabric_required(self):
        """ return:  self.V/6.5+0.5 for Coat
            return:  2*self.H + 0.3 For suit"""
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def fabric_required(self):
        return (self.V / 6.5) + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def fabric_required(self):
        return 2*self.H + 0.3


new_coat = Coat(40)
new_suit = Suit(1.8)

print(f'{new_coat.fabric_required():.1f}')
print(f'{new_suit.fabric_required():.1f}')