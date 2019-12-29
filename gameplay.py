from Pokemon import *
from Item import *
from Ability import *
from team import *


class game_session(object):
    def __init__(self,my_team,opponent_team):
        self.my_team=my_team
        self.opponent_team=opponent_team
        self.my_on_court=0
        self.opponent_on_court=0

    def __str__(self):
        return self.my_team.my_team_detail(),self.opponent_team.opponent_team_detail()


    @property
    def on_court(self):
        my_pokemon=self.my_team[self.my_on_court]
        opponent_pokemon=self.opponent_team[self.opponent_on_court]
        print("""
                                                    {}\n


                  {}

              """.format(my_pokemon,opponent_pokemon)
        )
        return my_pokemon,opponent_pokemon












#def turn(i:int,pokemon_team1,pokemon_team2):
    #start of the turns
#    if i==1:
#        start_turn_message=
#        '''
#        Turn {} starts \n
#        Begin Battle: \n
#        Chose your pokemon: \n

#        {}   {}\n
#        {}   {}\n
#        {}   {}\n


#        '''.format(i,pokemon_team1[0].getName,pokemon_team1[0].getType,pokemon_team1[1].getName,pokemon_team1[1].getType,pokemon_team1[2].getName,pokemon_team1[2].getType)
#    else:
#        start_turn_message=
#        ''' Turn {} starts \n
#
#            {}\n

#            select an available move for {}:\n
#            Battle\n
#            Substitude \n
#            Give up
#        '''.format(i,pokemon1.battle_stats,pokemon1.getName()))

    #check who will move first
    #check which pokemon is on on_court
    #check which pokemon is in the bag
    #check begin of the turn item effect/ability effect
    #check begin of the turn field and weather effect
    #check moves from each pokemon
    #check substitution

    #pokemon1 move1

    #check move type
    #check if move is valid(still has pp)
    #check success or miss
    #check critical or not if successful
    #check damage/stats change effect
    #check post move status change (toxic, paralysis, etc)
    #check post move item/abiliity effect

    #check if pokemon1 dies
    #check if pokemon2 dies

    #check move type
    #check if move is valid(still has pp)
    #check success or miss
    #check critical or not if successful
    #check damage/stats change effect
    #check post move status change (toxic, paralysis, etc)
    #check post move item/abiliity effect

    #check if pokemon1 dies
    #check if pokemon2 dies

    #start of turn end
    #check which pokemon is on on_court
    #check which pokemon is in the bag
    #check end of the turn move damage
    #check end of the turn item effect/ability effect
    #check end of the turn field and weather effect
    #check if pokemon1 dies
    #check if pokemon2 dies
