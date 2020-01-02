import Pokemon
import Move

class Item(object):
    def __init__(self,name:str,timing:str,description=None,one_time_only=True):
        self.name=name
        self.timing=timing
        self.one_time_only=one_time_only
        self.is_fruit=0
        self.description=description

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
            Name: {}\n
            Description: {}\n
            """.format(self.name,self.description)
        return msg


class LifeOrb(Item):
    def __init__(self,user=None,target=None):
        Item.__init__(self,name="Life Orb",timing="before dealing damage",
                      description="	An item to be held by a Pokémon. It boosts the power of moves but at the cost of some HP on each hit.",
                      one_time_only=False)
        self.user=user
        self.target=target

    def effect(self,user,target):
        if user.power>0:
           user.power*=1.3
           target.__battle_hp-=target.__battle_hp*0.1
