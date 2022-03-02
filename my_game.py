"""The game classes"""


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
