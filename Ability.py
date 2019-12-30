import Pokemon
import Move

class ability(object):
    def __init__(self,name:str,timing:str,description:str,one_time_only=0):
        self.name=name
        self.timing=timing
        self.one_time_only=one_time_only
        #timing:
        #when item effect would trigger:
        #sub in
        #sub out
        #dies
        #before dealing damage
        #after dealing damage
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
                Description: {}\n
            """.format(self.name,self.id,self.description)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.namess

    def get_timing(self):
        return self.timing


class FlashFire(ability):
    def __init__(self,user:Move,target:Pokemon):
        ability.__init__(name="Flash Fire",timing="before taking damage",
                         description="Powers up the Pokémon's Fire-type moves if it's hit by one.")
        self.user=user
        self.target=target

    @property
    def taking_effect(user:Move,target:Pokemon):
        if user.getType()=="Fire" and "Fire" in target.type:
           user.damage=0
           target.__battle_stats[1]*=1.5
           target.__battle_stats[3]*=1.5


class Disguise(ability):
    def __init__(self,user:Move,target:Pokemon):
        ability.__init__(name="Disguise",timing="after taking damage",
                         description="Once per battle, the shroud that covers the Pokémon can protect it from an attack.",
                         one_time_only=1)
        self.user=user
        self.target=target

    def effect(user:Move,target:Pokemon):
        if user.damage>0:
            user.damage=0
            target.__battle_hp-=round(target.__initial_stats[0]*1/8)
            self.type=self.original_type
