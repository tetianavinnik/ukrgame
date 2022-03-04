"""The game classes"""
import time
import random

class City:
    """
    Class for room representation.
    """
    def __init__(self, name: str, open='', points='', enemy='', friend='', item='', free = False) -> None:
        """
        create new room.
        """
        self.name = name
        self.points = points
        self.open = open
        self.enemy = enemy
        self.friend = friend
        self.item = item
        self.free = free


    def set_enemy(self, character):
        """
        Set character.
        """
        self.enemy = character
    

    def get_friend(self):
        """
        Get character.
        """
        return self.friend


    def set_friend(self, character):
        """
        Set character.
        """
        self.friend = character
    

    def get_enemy(self):
        """
        Get character.
        """
        return self.enemy


    def set_item(self, item):
        """
        Set item.
        """
        self.item = item


    def get_item(self):
        """
        Get item.
        """
        return self.item


    def get_details(self):
        """
        Print details.
        """
        print(self.name)
        print('--------------------')


    def set_open(self, point):
        """
        Set open.
        """
        self.open = point


    def set_points(self, points):
        """
        Set points.
        """
        self.points = points


class BossCity(City):
    """
    Class for BossCity representation.
    """
    def __init__(self, name: str, open='', points='', enemy='', friend='', item='', free=False) -> None:
        super().__init__(name, open, points, enemy, friend, item, free)


    def boss_level_one(self):
        print("""
Вітаю! Залишилось звільнити останнє місто - Харків.
Для цього тобі знадобиться вміння управляти літаком МіГ-29.

Інструкція:

Зараз ти знаходишся під обстрілом ворожого літака,
тобі потрібно ухилятися від ракет, які ти бачиш на радарі.
Як? - Потрібно ввести одну з чотирьох команд(праворуч, ліворуч, вгору, вниз).
Будь уважним, час обмежений!
Натисни Enter, коли будеш готовий""")
        input('> ')
        win = False
        while win == False:
            times = 0
            breaks = 0
            dec = ['праворуч', 'ліворуч', 'вгору', 'вниз']
            shot = ['праворуч', 'ліворуч', 'згори', 'знизу']
            win = False
            while times != 5 or breaks != 3:
                shoot = random.choice(shot)
                print('Обережно! Обстріл {}'.format(shoot))
                start = time.time()
                decision = input('> ')
                end = time.time()
                if end-start > 6:
                    breaks += 1
                    print('Тебе підсмажили. Думай швидше!')
                elif decision not in dec:
                    breaks += 1
                    print('Такої опції немає')
                elif dec[shot.index(shoot)] == decision:
                    breaks += 1
                    print('Тебе підсмажили. Думай краще!')
                else:
                    times += 1
                    print('Так тримати!')
                if breaks == 3:
                    print('Тебе збили! Спробуй ще раз.')
                    input('> ')
                elif times == 5:
                    print('\nМолодець! Ти зміг втекти зпід обстрілу!\n')
                    win = True
                if win == True:
                    break


    def boss_level_two(self):
        print("""
Ти неймовірний! Залишилось зовсім трохи.

Настав час надерти зад рашистам, адже вони виглядають набагато краще підсмаленими.
Слідкуй за радаром і випускай ракети в напрямку ворожих літаків.
Хай щастить!
Натисни Enter, коли будеш готовий""")
        input('> ')
        win = False
        while win == False:
            times = 0
            breaks = 0
            dec = ['праворуч', 'ліворуч', 'вгору', 'вниз']
            shot = ['праворуч', 'ліворуч', 'згори', 'знизу']
            win = False
            while times != 5 or breaks != 3:
                shoot = random.choice(shot)
                print('Увага! Літак {}'.format(shoot))
                start = time.time()
                decision = input('> ')
                end = time.time()
                if end-start > 6:
                    breaks += 1
                    print('Ти пропустив свій шанс. Думай швидше!')
                elif decision not in dec:
                    breaks += 1
                    print('Такої опції немає')
                elif dec[shot.index(shoot)] != decision:
                    breaks += 1
                    print('Ти впустив свій шанс. Думай краще!')
                else:
                    times += 1
                    print('Так тримати!')
                if breaks == 3:
                    print('Ти пропустив 3 літаки підряд! Спробуй ще раз.')
                    input('> ')
                elif times == 5:
                    print('\nЙухуу! Завдяки тобі жителі Харкова змогли насолодитися рашистським салютом')
                    win = True
                if win == True:
                        break
        print("""
Ти звільнив Україну від окупантів!

Слава Україні!""")


class Person:
    """
    Class for enemy representation.
    """
    characters = []
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description   
    

    def describe(self):
        """
        Print character`s description.
        """
        print(self.name)
        print(self.description)


class Enemy(Person):
    """Class for person representation"""
    def __init__(self, name: str, description: str, weakness='') -> None:
        super().__init__(name, description)
        self.weakness = weakness


    def fight(self, fight_with):
        """
        Fight with character.
        """
        if fight_with.name == self.weakness:
            return True
        return False


    def set_weakness(self, weakness: str):
        """
        Set weakness.
        """
        self.weakness = weakness


class Friend(Person):
    """
    Class for friend representation.
    """
    def __init__(self, name: str, description: str, talk: str) -> None:
        super().__init__(name, description)
        self.talk = talk

    
    def ask_help(self, city):
        """
        Ask for knowledge.
        """
        print('[{}]: {}'.format(self.name, self.talk))
        print('{} - {}'.format(city.get_item().name, city.get_item().get_description()))
        return city.get_item()



class Item:
    """
    Class for item representation.
    """
    def __init__(self, name, description='') -> None:
        """
        Create new item.
        """
        self.name = name
        self.description = description


    def set_description(self, description: str):
        """
        Set description.
        """
        self.description = description


    def get_item(self):
        """
        Get item.
        """
        return self.name

    
    def get_name(self):
        """
        Get name.
        """
        return self.name


class Thing(Item):
    """
    Class for things representation.
    """
    def __init__(self, name, description='') -> None:
        super().__init__(name, description)


    def describe(self):
        """
        Print description of the item.
        """
        print('Тут є {} - {}'.format(self.name, self.description))


class Knowledge(Item):
    """
    Class for knowledge representation.
    """
    def __init__(self, name, description='') -> None:
        super().__init__(name, description)


    def get_description(self):
        """
        Print description of the item.
        """
        return self.description
