class Move(object):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,type:str,category:str,move_priority=0):
        # ATTRIBUTES
        # ID info
        self.id = id # Move's number id
        self.name = name  # Move's name
        self.description = description  # Move description

        # Description
        self.type = type  # Move type
        self.category = category  # Can be special, physical,special,one-hit; can be multiple
        self.pp = pp
        self.availablepp=pp
        self.max_pp=self.pp*1.6
        self.move_priority=move_priority

        self.power=power
        self.accuracy=accuracy


        def __str__(self):
            msg = """
                     Move Name:{} \n
                     Move Description:{} \n
                     Move Type:{} \n
                     Move category:{} \n
                     Power:{} PP:{}/{} \n
                  """.format(self.name,self.description,self.type,self.category,self.power,self.available,self.pp)
            return msg


        def getname(self):
            return self.name
        # GET Methods
        def getID(self):
            return self.id

        def getDescription(self):
            return self.description

        def getType(self):
            return self.type

        def get_move_priority(self):
            return self.priority

        def getPower(self):
            return self.power

        def getAccuracy(self):
            return self.accuracy

        def getPP(self):
            return self.pp

class Physical_Move(Move):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,
                 has_contact=0,recoil=0,move_priority=0,guardable=1,unmissible=0):
        Move.__init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,move_priority=move_priority)
        self.type='physical damage'
        self.recoil=recoil
        self.has_contact=has_contact
        self.guardable=guardable
        self.unmissible=unmissible


class Special_Move(Move):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,
                 has_contact=0,recoil=0,move_priority=0,guardable=1,unmissible=0):
        Move.__init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,move_priority=move_priority)
        self.type='special damage'
        self.recoil=recoil
        self.has_contact=has_contact
        self.guardable=guardable
        self.unmissible=unmissible

class Weather_Move(Move):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,
                 weather):
        Move.__init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,category:str,move_priority=move_priority)
        self.weather=weather




class Move(object):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,type:str,category:str,has_contact:bool,
                weather=None,status_change=None,stats_change=None,
                defendable=True,critial_rate=1/24,move_priority=0,
                unmissible=0):
        # ATTRIBUTES
        # ID info
        self.id = id # Move's number id
        self.name = name  # Move's name
        self.description = description  # Move description

        # Description
        self.type = type  # Move type
        self.category = category  # Can be special, physical,special,one-hit; can be multiple
        self.pp = pp
        self.availablepp=pp
        self.max_pp=self.pp*1.6
        self.has_contact=has_contact
        self.defendable=defendable
        self.move_priority=move_priority

        # For in-battle calculations
        self.power = power  # Move's base damage
        self.accuracy = accuracy
        self.unmissible=unmissible
        self.recoil={"self_health_percentage":0,"damage_percentage":0}

        #status_change
        self.cause_status_condition= \
        {"Paralysis":{"self":0,"opponent":0}, \
             "Toxic":{"self":0,"opponent":0}, \
             "Sleep":{"self":0,"opponent":0},
             "Confusion":{"self":0,"opponent":0},
             "Freezed":{"self":0,"opponent":0},
             "Burned":{"self":0,"opponent":0},
             "Poisoned":{"self":0,"opponent":0},
             "Flinch":{"self":0,"opponent":0},
        }

        if status_change is not None:
            for status,change in status_change.items():
                for target,percentage in change.items():
                    self.cause_status_condition[status][target]=percentage


        #stats_change
        self.cause_stats_change= \
        {
        "Attack":{"self":0,"opponent":0},
        "Defense":{"self":0,"opponent":0},
        "SpAtk":{"self":0,"opponent":0},
        "SpDef":{"self":0,"opponent":0},
        "Speed":{"self":0,"opponent":0},
        "Heal":{"self":0,"opponent":0},
        "Self Damage":{"self":0,"opponent":0}
        }

        if stats_change is not None:
            for status,change in stats_change.items():
                for target,percentage in change.items():
                    self.cause_stats_change[status][target]=percentage

        #weather_change
        self.change_weather= \
        {
        "Sunny":0,
        "Rainy":0,
        "Hail":0,
        "Sand Storm":0
        }

        if weather is not None:
            self.change_weather[weather]=1

    # METHODS
    # str method
    def __str__(self):
        msg = """
                 Move Name:{} \n
                 Move Description:{} \n
                 Move Type:{} \n
                 Move category:{} \n
                 Power:{} PP:{}/{} \n
              """.format(self.name,self.description,self.type,self.category,self.power,self.available,self.pp)
        return msg

    def getname(self):
        return self.name

    # GET Methods
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getType(self):
        return self.type

    def getKind(self):
        return self.kind

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getPP(self):
        return self.pp

    def getCategory(self):
        return self.category

    def has_contact(self):
        return self.has_contact

    def get_status_condition(self):
        return self.cause_status_condition

    def get_stats_change(self):
        return self.cause_stats_change

    def defendable(self):
        return self.defendable

    def change_available_pp(self,available_pp):
        return self.availablepp



def MegaPunch(Move):



class MegaPunch(Move):
    def __init__(self):
       Move.__init__(self,
                     id=5,
                     name="MegaPunch",
                     description="The target is slugged by a punch thrown with muscle-packed power.",
                     type="Normal",
                     category="Physical",
                     power=80,
                     accuracy=85,
                     pp=20,
                     has_contact=1,
                     defendable=1)
class PayDay(Move):
    def __init__(self):
       Move.__init__(self,
                     id=6,
                     name="Pay Day",
                     description="Numerous coins are hurled at the target to inflict damage. Money is earned after the battle.",
                     type="Normal",
                     category="Physical",
                     power=40,
                     accuracy=100,
                     pp=20,
                     has_contact=0,
                     defendable=1)
class FirePunch(Move):
    def __init__(self):
       Move.__init__(self,
                     id=7,
                     name="FirePunch",
                     description="The target is punched with a fiery fist. This may also leave the target with a burn.",
                     type="Fire",
                     category="Physical",
                     power=75,
                     accuracy=100,
                     pp=15,
                     has_contact=1,
                     defendable=1,
                     status_change={"Burned":{"opponent":0.1}})
class IcePunch(Move):
    def __init__(self):
       Move.__init__(self,
                     id=8,
                     name="IcePunch",
                     description="The target is punched with an icy fist. This may also leave the target frozen.",
                     type="Ice",
                     category="Physical",
                     power=75,
                     accuracy=100,
                     pp=15,
                     has_contact=1,
                     defendable=1,
                     status_change={"Freezed":{"opponent":0.1}})
class ThunderPunch(Move):
    def __init__(self):
       Move.__init__(self,
                     id=9,
                     name="ThunderPunch",
                     description="The target is punched with an electrified fist. This may also leave the target with paralysis.",
                     type="Electric",
                     category="Physical",
                     power=75,
                     accuracy=100,
                     pp=15,
                     has_contact=1,
                     defendable=1,
                     status_change={"Paralysis":{"opponent":0.1}})
#class Scratch
class ViceGrip(Move):
    def __init__(self):
       Move.__init__(self,
                     id=11,
                     name="Vice Grip",
                     description="The target is gripped and squeezed from both sides to inflict damage.",
                     type="Normal",
                     category="Physical",
                     power=55,
                     accuracy=100,
                     pp=30,
                     has_contact=1,
                     defendable=1)
class Guillotine(Move):
    def __init__(self):
       Move.__init__(self,
                     id=12,
                     name="Guillotine",
                     description="A vicious, tearing attack with big pincers. The target faints instantly if this attack hits.",
                     type="Normal",
                     category="One-hit",
                     power=0,
                     accuracy=30,
                     pp=5,
                     has_contact=1,
                     defendable=1)
     #对速度大于自身的pokemon无效
class SwordDance(Move):
    def __init__(self):
       Move.__init__(self,
                     id=14,
                     name="Sword Dance",
                     description="A frenetic dance to uplift the fighting spirit. This sharply raises the user's Attack stat.",
                     type="Normal",
                     category="Stats-changing",
                     power=0,
                     accuracy=100,
                     pp=20,
                     has_contact=0,
                     defendable=0,
                     stats_change={"Attack":{"self":2}})
class Cut(Move):
    def __init__(self):
       Move.__init__(self,
                     id=15,
                     name="Cut",
                     description="The target is cut with a scythe or claw.",
                     type="Normal",
                     category="Physical",
                     power=50,
                     accuracy=95,
                     pp=30,
                     has_contact=1,
                     defendable=1)
class Gust(Move):
    def __init__(self):
       Move.__init__(self,
                     id=16,
                     name="Gust",
                     description="A gust of wind is whipped up by wings and launched at the target to inflict damage.",
                     type="Fly",
                     category="Physical",
                     power=40,
                     accuracy=100,
                     pp=35,
                     has_contact=0,
                     defendable=1)
class WingAttack(Move):
    def __init__(self):
       Move.__init__(self,
                     id=17,
                     name="Wing Attack",
                     description="	The target is struck with large, imposing wings spread wide to inflict damage.",
                     type="Fly",
                     category="Physical",
                     power=60,
                     accuracy=100,
                     pp=35,
                     has_contact=0,
                     defendable=1)
class WhirlWind(Move):
    def __init__(self):
       Move.__init__(self,
                     id=18,
                     name="Whirl Wind",
                     description="The target is blown away, and a different Pokémon is dragged out. In the wild, this ends a battle against a single Pokémon.",
                     type="Normal",
                     category="Special",
                     power=0,
                     accuracy=0,
                     pp=20,
                     has_contact=0,
                     defendable=0,
                     move_priority=-6)
        #Suction Cups, Ingrain to make it ineffective
class Fly(Move):
    def __init__(self):
       Move.__init__(self,
                     id=19,
                     name="Fly",
                     description="The user flies up into the sky and then strikes its target on the next turn.",
                     type="Fly",
                     category="Physical",
                     power=90,
                     accuracy=95,
                     pp=15,
                     has_contact=1,
                     defendable=1)
       self.wait_turn=1
class Bind(Move):
    def __init__(self):
       Move.__init__(self,
                     id=20,
                     name="Bind",
                     description="Things such as long bodies or tentacles are used to bind and squeeze the target for four to five turns.",
                     type="Normal",
                     category="Physical",
                     power=15,
                     accuracy=85,
                     pp=20,
                     has_contact=1,
                     defendable=1)
       self.sustainable=[4,5]
       self.followup_damage=15
class Slam(Move):
    def __init__(self):
       Move.__init__(self,
                     id=21,
                     name="Slam",
                     description="It damages an enemy.",
                     type="Normal",
                     category="Physical",
                     power=80,
                     accuracy=75,
                     pp=20,
                     has_contact=1,
                     defendable=1)
class VineWipe(Move):
    def __init__(self):
       Move.__init__(self,
                     id=22,
                     name="Vine Wipe",
                     description="The target is struck with slender, whiplike vines to inflict damage.",
                     type="Grass",
                     category="Physical",
                     power=45,
                     accuracy=100,
                     pp=25,
                     has_contact=1,
                     defendable=1)
class Stomp(Move):
    def __init__(self):
       Move.__init__(self,
                     id=23,
                     name="Stomp",
                     description="The target is stomped with a big foot. This may also make the target flinch.",
                     type="Normal",
                     category="Physical",
                     power=65,
                     accuracy=100,
                     pp=20,
                     has_contact=1,
                     defendable=1,
                     status_change={"Flinch":{"opponent":0.3}})
       #self.power=power*2 if target.status='minimized'
       #self.unmissible=1 if target.status='minimized'

class DoubleKick(Move):
    def __init__(self):
       Move.__init__(self,
                     id=24,
                     name="Double Kick",
                     description="The target is quickly kicked twice in succession using both feet.",
                     type="Fight",
                     category="Physical",
                     power=30,
                     accuracy=100,
                     pp=30,
                     has_contact=1,
                     defendable=1)
      self.same_turn_attack=2
      #more on this
