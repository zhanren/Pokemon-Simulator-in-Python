# Creating the Pokemon Class
import os
os.chdir('C:\\Users\\Brand\\OneDrive\\文档\\GitHub\\Pokemon-Simulator-in-Python')

class Pokemon(object):
    POKEMON_DICTIONARY = {}
    NATURE_DICTIONARY={}
    LEVEL = 50
    def __init__(self,pokemon,gender,iv=[31,31,31,31,31,31],ability=None,item=None,nature='timid',ev=[100,100,100,100,100,10],moves=['a','b','c','d'],dynamax_level=10,friendship=255):
        # User defined pokemon
        '''
        Pokemon initiate value:

        pokemon: pokemon defined by the game;

        moves: list of 4 strings; e.g. ['sand attack','take-down','hyperbeam','dragon claw']

        iv: list of 6 int; e.g. [31,31,31,31,31,31], represents individual value for hp, physical attack, physical defense, special attack, special defense, speed
            each value is a int between 0 and 31

        ev: list of 6 int; e.g. [0,0,252,252,6,0]; represents effort value for h, physical attack,physical defense,special attack, special defense, speed
            each value is a int between 0 and 252;
            the sum of ev needs to be 510 or less.

        ability: pokemon's ability

        friendship: pokemon's friendship, an int between 0 and 255

        characteristics: pokemon's characteristics

        dynamax_level: pokemon's dynamax level, int from 0 to 10

        '''
        pokemonInfo = []
        if len(Pokemon.POKEMON_DICTIONARY) == 0:
            fin = open("Kanto Pokemon Spreadsheet.csv", 'r')
            for line in fin:
                line = line.strip()
                pokeList = line.split(",")
                Pokemon.POKEMON_DICTIONARY[pokeList[1]] = pokeList  # Creating key (Pokemon name) value (id info) pair

            fin.close()

        # Creating an info list for the user-selected Pokemon containing all the Pokemon attributes
        for key in Pokemon.POKEMON_DICTIONARY:
            if key.lower() == pokemon.lower():
                pokemonInfo = Pokemon.POKEMON_DICTIONARY[key]

        # ATTRIBUTES
        # Referring to the pokemonInfo list to fill in the rest of the attributes
        # ID Info


        self.__id = pokemonInfo[0]
        self.name = pokemonInfo[1]
        self.level = Pokemon.LEVEL
        self.gender=gender

        # Type 系
        self.type1 = pokemonInfo[2]
        self.type2 = pokemonInfo[3]

        # Move 技能
        self.move1=moves[0]
        self.move2=moves[1]
        self.move3=moves[2]
        self.move4=moves[3]

        # iv 个体值
        self.iv=iv
        self.iv_hp=self.iv[0]
        self.iv_attack=self.iv[1]
        self.iv_defense=self.iv[2]
        self.iv_special_attack=self.iv[3]
        self.iv_special_defense=self.iv[4]
        self.iv_speed=self.iv[5]

        # ev 努力值
        self.ev=ev
        self.ev_hp=self.ev[0]
        self.ev_attack=self.ev[1]
        self.ev_defense=self.ev[2]
        self.ev_special_attack=self.ev[3]
        self.ev_special_defense=self.ev[4]
        self.ev_speed=self.ev[5]


        # BASE STATS 种族值
        self.__hp = int(pokemonInfo[4])
        self.__attack = int(pokemonInfo[5])
        self.__defense = int(pokemonInfo[6])
        self.__special_attack = int(pokemonInfo[7])
        self.__special_defense = int(pokemonInfo[8])
        self.__speed = int(pokemonInfo[9])

        #nature 性格
        self.nature=nature
        if len(Pokemon.NATURE_DICTIONARY) == 0:
            fin = open("nature.csv", 'r')
            for line in fin:
                line = line.strip()
                nature_line = line.split(",")
                Pokemon.NATURE_DICTIONARY[nature_line[0]] = nature_line

            fin.close()

        # Creating an info list for user-selected pokemon nature
        for key in Pokemon.NATURE_DICTIONARY:
            if key.lower() == nature.lower():
                nature_modifer= Pokemon.NATURE_DICTIONARY[key]

        self.__hp_modifer=float(nature_modifer[1])
        self.__attack_modifer=float(nature_modifer[2])
        self.__defense_modifer=float(nature_modifer[3])
        self.__special_attack_modifer=float(nature_modifer[4])
        self.__special_defense_modifer=float(nature_modifer[5])
        self.__speed_modifer=float(nature_modifer[6])

        #ability 特性
        self.ability=ability

        #item 携带物品
        self.item=item

        # In Battle Stats
        # Stat = ((Base * 2 + IV + (EV/4)) * Level / 100 + 5) * Nmod
        #HP = (Base * 2 + IV + (EV/4)) * Level / 100 + 10 + Level

        # These variables are used to just hold the values of the original stat for stat modification purposes

        # A list containing all the moves; used for error-checking later
        self.moveList = [self.move1.lower(), self.move2.lower(), self.move3.lower(), self.move4.lower()]

        # In Battle Stats
        # Raised or lowered based on different moves used in battle. Affects the in battle stats (more info in the Overview of Battle Mechanics in readme.txt)
        self.accuracy=1
        self.evasion=0
        self.atkStage = 0
        self.defStage = 0
        self.spAtkStage = 0
        self.spDefStage = 0
        self.speedStage = 0

    #read only property in battle stats: 六围面板数据
    @property
    def get_initial_stats(self):
        originalHP = round((self.__hp*2+self.iv_hp+(self.ev_hp/4))*self.level/100+10+self.level)*self.__hp_modifer
        originalATK = round(((self.__attack*2+self.iv_attack+(self.ev_attack/4))*self.level/100+5)*self.__attack_modifer)
        originalDEF = round(((self.__defense*2+self.iv_defense+(self.ev_defense/4))*self.level/100+5)*self.__defense_modifer)
        originalSpATK = round(((self.__special_attack*2+self.iv_special_attack+(self.ev_special_attack/4))*self.level/100+5)*self.__special_attack_modifer)
        originalSpDEF = round(((self.__special_defense*2+self.iv_special_defense+(self.ev_special_defense/4))*self.level/100+5)*self.__special_defense_modifer)
        originalSpeed = round(((self.__speed*2+self.iv_speed+(self.ev_speed/4))*self.level/100+5)*self.__speed_modifer)
        self.initial_stats=[originalHP,originalATK,originalDEF,originalSpATK,originalSpDEF,originalSpeed]
        return self.initial_stats
    # METHODS
    # Printing all the Pokemon info with the str method

    def __str__(self):
        stats=self.get_initial_stats
        HP=stats[0]
        ATK=stats[1]
        DEF=stats[2]
        SpATK=stats[3]
        SpDef=stats[4]
        Speed=stats[5]
        msg = '''
                    Pokemon: {} \n
                    Pokemon Index: {}\n
                    Ability: {}
                    HP: {}\n
                    Attack: {}\n
                    Defense: {}\n
                    Special Offense:{}\n
                    Special Defense: {}\n
                    Speed: {}\n
                    Nature: {}\n
                    Item: {}\n

              '''.format(self.name,self.__id,self.ability,HP,ATK,DEF,SpATK,SpDef,Speed,self.nature,self.item)

        return msg

    #stats during the game, will change with the game; 战斗中六围数据
    @property
    def battle_stats(self):
        battleHP = round((self.__hp*2+self.iv_hp+(self.ev_hp/4))*self.level/100+10+self.level)*self.__hp_modifer
        battleATK = round(((self.__attack*2+self.iv_attack+(self.ev_attack/4))*self.level/100+5)*self.__attack_modifer)
        battleDEF = round(((self.__defense*2+self.iv_defense+(self.ev_defense/4))*self.level/100+5)*self.__defense_modifer)
        battleSpATK = round(((self.__special_attack*2+self.iv_special_attack+(self.ev_special_attack/4))*self.level/100+5)*self.__special_attack_modifer)
        battleSpDEF = round(((self.__special_defense*2+self.iv_special_defense+(self.ev_special_defense/4))*self.level/100+5)*self.__special_defense_modifer)
        battleSpeed = round(((self.__speed*2+self.iv_speed+(self.ev_speed/4))*self.level/100+5)*self.__speed_modifer)
        return [battleHP,battleATK,battleDEF,battleSpATK,battleSpDEF,battleSpeed]
    @battle_stats.setter
    def battle_stats_change(self,change):
        return change

    def get_current_status(self):
        '''
        get in battle status

        '''
        msg = '''
                    Pokemon: {} \n
                    Pokemon Index: {}\n
                    HP: {}\nAttack: {}\n
                    Defense: {}\n
                    Special Offense:{}\n
                    Special Defense: {}\n
                    Speed: {}\n
              '''.format(self.name,self.__id,self.battleHP,self.battleATK,self.battleDEF, \
                         self.battleSpATK,self.battleSpDEF,self.battleSpeed)
        print(msg)
        return

    def get_iv(self):
        ev_list={"hp":self.iv_hp,"attack":self.iv_attack,"defense":self.iv_defense,"special_attack": self.iv_special_attack,"special_defense":self.iv_special_defense,"speed":self.iv_speed}

        msg='''
                      Individual value: \n
                      HP  Attack  Defense  SpAtk SpDef Speed\n
                      {}   {}    {}     {}  {}   {} \n
            '''.format(self.ev_hp,self.ev_attack,self.ev_defense,self.ev_special_attack,self.ev_special_defense,self.ev_speed)
        print(msg)
        return ev_list

    def get_ev(self):
        ev_list={"hp":self.ev_hp,"attack":self.ev_attack,"defense":self.ev_defense,"special_attack": self.ev_special_attack,"special_defense":self.ev_special_defense,"speed":self.ev_speed}

        msg='''
                      Effort value: \n
                      HP  Attack  Defense  SpAtk SpDef Speed\n
                      {}   {}    {}     {}  {}   {} \n
            '''.format(self.ev_hp,self.ev_attack,self.ev_defense,self.ev_special_attack,self.ev_special_defense,self.ev_speed)
        print(msg)
        return ev_list

    #change nature 设置性格
    def set_nature(self,nature):
        self.nature=nature
        nature_modifer=Pokemon.NATURE_DICTIONARY[nature.lower()]
        if nature_modifer is None:
            raise ValueError('This nature does not exist!')
        self.__hp_modifer=float(nature_modifer[1])
        self.__attack_modifer=float(nature_modifer[2])
        self.__defense_modifer=float(nature_modifer[3])
        self.__special_attack_modifer=float(nature_modifer[4])
        self.__special_defense_modifer=float(nature_modifer[5])
        self.__speed_modifer=float(nature_modifer[6])

    def set_friendship(self,friendship):
        if friendship<0 or frienship>255:
            raise ValueError("frienship needs to be an int between 0 and 255")
        self.friendship=friendship

    def set_iv(self,iv_list):
        if min(iv_list)<0 or max(iv_list)>31:
            raise ValueError('iv needs to be an int between 0 and 31!')
        self.iv_hp=iv_list[0]
        self.iv_attack=iv_list[1]
        self.iv_defense=iv_list[2]
        self.iv_special_attack=iv_list[3]
        self.iv_special_defense=iv_list[4]
        self.iv_speed=iv_list[5]

    def set_ev(self,ev_list):
        if sum(ev_list)>510:
            raise ValueError('sum of evs need be to 510 or less!')
        if min(ev_list)<0 or max(ev_list)>252:
            raise ValueError('ev needs to be an int between 0 and 252!')
        self.ev_hp=ev_list[0]
        self.ev_attack=ev_list[1]
        self.ev_defense=ev_list[2]
        self.ev_special_attack=ev_list[3]
        self.ev_special_defense=ev_list[4]
        self.ev_speed=ev_list[5]

    # Set STAT STAGE Methods
    def setAtkStage(self, atkStage):
        self.atkStage = min(5,atkStage)

    def setDefStage(self, defStage):
        self.defStage = min(5,defStage)

    def setSpAtkStage(self, spAtkStage):
        self.spAtkStage = min(5,spAtkStage)

    def setSpDefStage(self, spDefStage):
        self.spDefStage = min(5,spDefStage)

    def setSpeedStage(self, speedStage):
        self.speedStage = min(5,speedStage)

    # MOVE Methods
    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getMove3(self):
        return self.move3

    def getMove4(self):
        return self.move4

    def setMove1(self, move1):
        self.move1 = move1

    def setMove2(self, move2):
        self.move2 = move2

    def setMove3(self, move3):
        self.move3 = move3

    def setMove4(self, move4):
        self.move4 = move4

    def set_ev(self,ev_list):
        if sum(ev_list)>510:
            raise ValueError('sum of evs need be to 510 or less!')
        if min(ev_list)<0 or max(ev_list)>252:
            raise ValueError('ev needs to be an int between 0 and 252!')
        self.ev_hp=ev_list[0]
        self.ev_attack=ev_list[1]
        self.ev_defense=ev_list[2]
        self.ev_special_attack=ev_list[3]
        self.ev_special_defense=ev_list[4]
        self.ev_speed=ev_list[5]
    # Print Methods
    # These methods return strings containing information about HP and movesets
    def printHP(self):
        msg = str(self.name) + ": HP " + str("{}/{}".format(self.battleHP,self.originalHP))
        return msg

    #def printMoves(self): # Take a list of move names as argument?
    #    msg = "\nMove 1: " + self.move1.moveInfo[1] + "\nMove 2: " + self.move2.moveInfo[1] + "\nMove 3: " + self.move3.moveInfo[1] + "\nMove 4: " + self.move4.moveInfo[1]
    #    return msg

    # In Battle Methods

    # Takes a move as input and returns a string with the pokemon using that move
    #def useMove(self, move):
    #    msg = self.name + " used " + move.name + "!"
    #    return msg

    # Takes an int as input and returns a string with the pokemon losing that much HP
    #def loseHP(self, lostHP):
    #    self.battleHP -= lostHP
    #    # Making sure battlHP doesn't fall below 0
    #    if self.battleHP <= 0:
    #        self.battleHP = 0
    #    msg = self.name + " lost " + str(lostHP) + " HP!"
    #    return msg

    # Takes an int as input and returns a string with the pokemon gaining that much HP
    #def gainHP(self, gainedHP):
    #    self.__hp += gainedHP

    # Determines if the Pokemon still has HP and returns a boolean
    #def isAlive(self):
    #    if self.battleHP > 0:
    #        return True
    #    else:
    #        return False

    # If battleHP is 0, returns a string showing that the Pokemon fainted
    #def faint(self):
    #    if self.battleHP <= 0:
    #        msg = self.name + " fainted "
    #        return msg
