import Pokemon

class build_team(object):
    def __init__(self,team,rule=None):
        self.team=team
        self.rule={
            "Single":["1v1","3v3","6p3","6v6"],
            "Double":["2v2","4v4","6v6","6p4"]
        }


    def __str__(self):
        msg=""
        for pokemon in self.team:
            print(pokemon.myteam_format())
        return msg


    def my_team_detail(self,mute=False):
        if mute:
            return self.team
        else:
            for pokemon in self.team:
                print(pokemon)
            return self.team

    def opponent_team_detail(self,mute=False):
        if mute:
            return self.team
        else:
            for pokemon in self.team:
                print(pokemon.opponent_team_format())
            return self.team

    def get_pokemon(self,)
