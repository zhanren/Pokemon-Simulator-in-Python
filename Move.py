class Move(object):
    def __init__(self,id:int,name:str,power:int,description:str,accuracy:int,pp:int,type:str,category:str,move_priority=0,has_contact=0,defendable=1):
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
        self.has_contact=has_contact

        self.power=power
        self.accuracy=accuracy
        self.defendable=defendable


    def __str__(self):
        msg = """
                    Name:{} \n
                    Description:{} \n
                    Type:{} \n
                    Category:{} \n
                    Power:{} PP:{}/{} \n
              """.format(self.name,self.description,self.type,self.category,self.power,self.availablepp,self.pp)
        return msg

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
                     pp=20)

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
                     has_contact=1)
       self.burn=0.1

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
                     has_contact=1)
       self.freeze=0.1

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
                     defendable=1)
       self.paralysis=0.1


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
                     defendable=0)
       self.attack=2
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
                     has_contact=1)
       self.flinch=0.3
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
      #more on this
