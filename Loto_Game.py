import random
from functools import reduce


class Player:

    def __init__(self, player_name, human_or_computer=None):
        self.player_name = player_name
        self.human_or_computer = human_or_computer


class Card:

    def card():
        card = []
        x = list(range(1 , 91))
        card_generator = random.sample(x, 27)
        for i in range(0 , len(card_generator) , 9):
            card.append(card_generator[i:i + 9])
        x = 0
        while x < 3:
           card[x][random.randint(0 , 8)] = '_'
           if card[x].count('_') < 4:
              continue
           x += 1

        return card

    def __str__():
        return print('\n'.join(['\t'.join(map(str, lst)) for lst in Card.card()]))


class Game:

    def game():

        print('---------Игра началсь!----------','\n')
        players_card = Card.card()
        computers_card = Card.card()
        print("----------Ваша карточка----------"'\n','\n'.join(['\t'.join(map(str, lst)) for lst in players_card]),'\n''---------------------------------','\n')
        print("------------Компьютер------------"'\n','\n'.join(['\t'.join(map(str, lst)) for lst in computers_card]),'\n''---------------------------------','\n')
        flatten_list_for_check_human = reduce(lambda i,j: i + j, players_card)
        flatten_list_for_check_computer = reduce(lambda i, j: i + j, computers_card)
        x = 0
        t = 0
        z = [x for x in range(1 , 92)]
        random.shuffle(z)

        while x < 91:

            k = z[t]
            t+=1
            print(k)

            print('Зачеркнуть цифру? (y/n)')
            players_input = input('')

            if k in flatten_list_for_check_human and players_input == 'y':
                for i in players_card:
                    for j in i:
                        if j == k:
                            players_card[players_card.index(i)][i.index(j)] = '/'
                            x += 1
                            print("----------Ваша карточка----------"'\n','\n'.join(['\t'.join(map(str, lst)) for lst in players_card]),'\n''---------------------------------','\n')

            if k not in flatten_list_for_check_human and players_input == 'n':
                    x+=1

            else:
                print('Ошибка! Игра окончена!')
                break

            if k in flatten_list_for_check_computer:
                for i in computers_card:
                    for j in i:
                        if j == k:
                            computers_card[computers_card.index(i)][i.index(j)] = '/'
                            print("------------Компьютер------------"'\n','\n'.join(['\t'.join(map(str, lst)) for lst in computers_card]),'\n''---------------------------------','\n')
            x +=1

            print(f'Осталось {91 - x} попыток!')
        

player1 = Player('Nikolay', 'human')
player2 = Player('Computer_Max', 'computer')
Game.game()



