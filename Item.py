import Pokemon
import Move

class item(object):
    def __init__(self,id:int,name:str,timing:str,one_time_only=1):
        self.id=id
        self.name=name
        self.timing=timing
        self.one_time_only=1
        self.is_fruit=0

    #timing:
    #when item effect would trigger:
    #sub in
    #sub out
    #dies
    #before taking damage
    #after taking damage
    #opponent sub in
    #opponent sub out
    #before taking damage
    #after taking damage
    #making move
    #under weather
    #weather/field
    #after heal
    #end of the turn

    def __str__(self):
        msg="""
            Ability: {}\n
            ID:      {}\n
            Description: {}\n
            """.format(self.name,self.id,self.description)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get.timing(self):
        return self.timing


class LifeOrb(item):
    def __init__(self,user:Move,target:Pokemon):
        item.__init__(name="Life Orb",timing="before dealing damage",
                      description="	An item to be held by a Pokémon. It boosts the power of moves but at the cost of some HP on each hit.")
        self.user=user
        self.target=target

    def effect(self,user,target):
        if self.power>0:
           self.power*=1.3
           self.__battle_hp-=self.__battle_hp*0.1
