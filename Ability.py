import Pokemon
import Move

class ability(object):
    def __init__(self,name:str,timing:str,description:str):
        self.name=name
        self.timing=timing
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
                Description: {}\n
            """.format(self.name,self.id,self.description)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get.timing(self):
        return self.timing


class FlashFire(ability):
    def __init__(self,user:Move,target:Pokemon):
        ability.__init__(name="Flash Fire",timing="before taking damage",
                         description="Powers up the Pokémon's Fire-type moves if it's hit by one.")
        self.user=user
        self.target=target

    def taking_effect(user,target):
        if user.getType()=="Fire" and "Fire" in target.get_type():
           damage=0
           target.
