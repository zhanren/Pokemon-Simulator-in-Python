class item(object):
    def __init__(self,id:int,name:str,timing:str,one_time_only=1):
        self.id=id
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
            ID:      {}\n
            Description: {}\n
            """.format(self.name,self.id,self.description)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get.timing(self):
        return self.timing



def 
