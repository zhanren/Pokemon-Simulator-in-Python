# Creating the Pokemon Class
class Pokemon(object):
    import math
    POKEMON_DICTIONARY = {}
    NATURE_DICTIONARY={}
    LEVEL = 50
    STAB=1.5
    def __init__(self,pokemon,gender,iv=[31,31,31,31,31,31],ability=None,item=None,nature='timid',ev=[100,100,100,100,100,10],moves=None,dynamax_level=10,friendship=255):
        # User defined pokemon
        '''
        Pokemon initiate value:

        pokemon: pokemon defined by the game;

        moves: list of 4 Move objects; e.g. [sand_attack,take_down,hyper_beam,dragon_claw]

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
            fin = open("galar_pokedex.csv", 'r')
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
        self.gender=gender.lower()

        # Type 系
        self.__type1 = pokemonInfo[2]
        self.__type2 = pokemonInfo[3]

        self.original_type=[self.__type1,self.__type2]

        # Move 技能
        self.__moves=moves

        # iv 个体值
        self.__iv=iv
        self.__iv_hp=self.__iv[0]
        self.__iv_attack=self.__iv[1]
        self.__iv_defense=self.__iv[2]
        self.__iv_special_attack=self.__iv[3]
        self.__iv_special_defense=self.__iv[4]
        self.__iv_speed=self.__iv[5]

        # ev 努力值
        self.__ev=ev
        self.__ev_hp=self.__ev[0]
        self.__ev_attack=self.__ev[1]
        self.__ev_defense=self.__ev[2]
        self.__ev_special_attack=self.__ev[3]
        self.__ev_special_defense=self.__ev[4]
        self.__ev_speed=self.__ev[5]


        # BASE STATS 种族值
        self.__hp = int(pokemonInfo[4])
        self.__attack = int(pokemonInfo[5])
        self.__defense = int(pokemonInfo[6])
        self.__special_attack = int(pokemonInfo[7])
        self.__special_defense = int(pokemonInfo[8])
        self.__speed = int(pokemonInfo[9])

        #nature 性格
        if len(Pokemon.NATURE_DICTIONARY) == 0:
            fin = open("nature.csv", 'r')
            for line in fin:
                line = line.strip()
                nature_line = line.split(",")
                Pokemon.NATURE_DICTIONARY[nature_line[0]] = nature_line
            fin.close()

        if nature.lower() in Pokemon.NATURE_DICTIONARY:
            self.__nature=nature
            nature_modifer= Pokemon.NATURE_DICTIONARY[nature.lower()]
            self.__hp_modifer=float(nature_modifer[1])
            self.__attack_modifer=float(nature_modifer[2])
            self.__defense_modifer=float(nature_modifer[3])
            self.__special_attack_modifer=float(nature_modifer[4])
            self.__special_defense_modifer=float(nature_modifer[5])
            self.__speed_modifer=float(nature_modifer[6])
            self.__accuracy=0
            self.__evasion=0
        else:
            raise ValueError("This nature does not exists")

        # Creating an info list for user-selected pokemon nature

        #ability 特性
        self.__ability=ability

        #item 携带物品
        self.__item=item

        # In Battle Stats
        # Stat = ((Base * 2 + IV + (EV/4)) * Level / 100 + 5) * Nmod
        #HP = (Base * 2 + IV + (EV/4)) * Level / 100 + 10 + Level
        originalHP = round((self.__hp*2+self.__iv_hp+(self.__ev_hp/4))*self.level/100+10+self.level)*self.__hp_modifer
        originalATK = round(((self.__attack*2+self.__iv_attack+(self.__ev_attack/4))*self.level/100+5)*self.__attack_modifer)
        originalDEF = round(((self.__defense*2+self.__iv_defense+(self.__ev_defense/4))*self.level/100+5)*self.__defense_modifer)
        originalSpATK = round(((self.__special_attack*2+self.__iv_special_attack+(self.__ev_special_attack/4))*self.level/100+5)*self.__special_attack_modifer)
        originalSpDEF = round(((self.__special_defense*2+self.__iv_special_defense+(self.__ev_special_defense/4))*self.level/100+5)*self.__special_defense_modifer)
        originalSpeed = round(((self.__speed*2+self.__iv_speed+(self.__ev_speed/4))*self.level/100+5)*self.__speed_modifer)
        self.__initial_stats=[originalHP,originalATK,originalDEF,originalSpATK,originalSpDEF,originalSpeed]
        # These variables are used to just hold the values of the original stat for stat modification purposes

        # In Battle Stats
        # Raised or lowered based on different moves used in battle. Affects the in battle stats (more info in the Overview of Battle Mechanics in readme.txt)

        self.atkStage = 0
        self.defStage = 0
        self.spAtkStage = 0
        self.spDefStage = 0
        self.speedStage = 0
        self.accuracy_level=self.__accuracy+self.__evasion
        self.__buff=[self.atkStage,self.defStage,self.spAtkStage,self.spDefStage,self.speedStage,self.accuracy_level]

        #dynamax 超极巨化
        self.__is_dynamax=False
        self.__dynamax_level=dynamax_level

        if max(self.__iv)>31 or min(self.__iv)<0:
            raise ValueError('iv needs to be an int between 0 and 31!')

        if max(self.__ev)>252 or min(self.__ev)<0:
            raise ValueError('ev needs to be an int bettwen 0 and 252')

        if sum(self.__ev)>510:
            raise ValueError('sum of evs need be to 510 or less!')

        self.__battle_stats=self.__initial_stats.append(self.accuracy_level)

        self.__battle_hp=int(originalHP)
        self.__is_faint=0


        #pokemon condtions
        self.paralysis=0
        self.toxic=0
        self.poison=0
        self.sleep=0
        self.confuse=0
        self.unmoveable=0
        self.freeze=0
    # Property


    #read only property in battle stats: 六围面板数据
    @property
    def initial_stats(self):
        originalHP = round((self.__hp*2+self.__iv_hp+(self.__ev_hp/4))*self.level/100+10+self.level)*self.__hp_modifer
        originalATK = round(((self.__attack*2+self.__iv_attack+(self.__ev_attack/4))*self.level/100+5)*self.__attack_modifer)
        originalDEF = round(((self.__defense*2+self.__iv_defense+(self.__ev_defense/4))*self.level/100+5)*self.__defense_modifer)
        originalSpATK = round(((self.__special_attack*2+self.__iv_special_attack+(self.__ev_special_attack/4))*self.level/100+5)*self.__special_attack_modifer)
        originalSpDEF = round(((self.__special_defense*2+self.__iv_special_defense+(self.__ev_special_defense/4))*self.level/100+5)*self.__special_defense_modifer)
        originalSpeed = round(((self.__speed*2+self.__iv_speed+(self.__ev_speed/4))*self.level/100+5)*self.__speed_modifer)
        self.__initial_stats=[int(originalHP),originalATK,originalDEF,originalSpATK,originalSpDEF,originalSpeed]
        return self.__initial_stats


    @property
    def buff(self):
        return self.__buff

    @buff.setter
    def buff(self,stats_change:list):
        def buff_multiplier(i):
            if i>=0:
                return (min(i,6)+2)/2
            else:
                return 2/(min(i,6)+2)

        def accuracy_multiplier(i:int,j:int):
            if i+j>=0:
                return (min(i+j,6)+3)/3
            else:
                return 3/(min(i+j,6)+3)

        if len(stats_change) !=7:
           ValueError("Need to be a list of 7 int representing\n attack,defense,special attack,special defense,speed,accuracy,evasion")

        else:
           self.__buff=sum(zip(stats_change,self.__buff))
           HP,ATK,DEF,SpATK,SpDEF,Speed,Accuracy,Evasion=self.__battle_stats
           ATK*=buff_multiplier(stats_change[0])
           DEF*=buff_multiplier(stats_change[1])
           SpATK*=buff_multiplier(stats_change[2])
           SpDEF*=buff_multiplier(stats_change[3])
           Speed*=buff_multiplier(stats_change[4])
           Accuracy_level=accuracy_multiplier(astats_change[5],stats_change[6])
           self.__battle_stats=[ATK,DEF,SpATK,SpDEF,Accuracy_level]
           self.atkStage +=stats_change[0]
           self.defStage += stats_change[1]
           self.spAtkStage += stats_change[2]
           self.spDefStage += stats_change[3]
           self.speedStage += stats_change[4]
           self.acccuracy_level+=stats_change[5]




    @property
    def battle_stats(self):
        return self.__battle_stats



    @property
    def type(self):
        return [self.__type1,self.__type2]

    @type.setter
    def type(self,type):
        self.__type1=type[0]
        self.__type2=type[1]

    #nature
    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self,nature):
        if  nature.lower() in Pokemon.NATURE_DICTIONARY.keys():
            self.__nature=nature
            nature_modifer= Pokemon.NATURE_DICTIONARY[nature.lower()]
            self.__hp_modifer=float(nature_modifer[1])
            self.__attack_modifer=float(nature_modifer[2])
            self.__defense_modifer=float(nature_modifer[3])
            self.__special_attack_modifer=float(nature_modifer[4])
            self.__special_defense_modifer=float(nature_modifer[5])
            self.__speed_modifer=float(nature_modifer[6])
            self.initial_stats
        else:
            raise ValueError("This nature does not exists")

    #iv
    @property
    def iv(self):
        return self.__iv

    @iv.setter
    def iv(self,iv:list):
        if len(iv) !=6:
            raise ValueError('iv needs to be a list of six int')
        if max(iv)>31 or min(iv)<0 or sum(type(i) != int for i in iv)>0:
            raise ValueError('iv needs to be an int between 0 and 31!')
        else:
            self.__iv=iv
            self.__iv_hp=self.__iv[0]
            self.__iv_attack=self.__iv[1]
            self.__iv_defense=self.__iv[2]
            self.__iv_special_attack=self.__iv[3]
            self.__iv_special_defense=self.__iv[4]
            self.__iv_speed=self.__iv[5]
            self.initial_stats

    #ev
    @property
    def ev(self):
        return self.__ev

    @ev.setter
    def ev(self,ev:list):
        if len(ev) !=6:
            raise ValueError('ev needs to be a list of six int')
        if max(self.__ev)>252 or min(self.__ev)<0:
            raise ValueError('ev needs to be an int bettwen 0 and 252')
        if sum(self.__ev)>510:
            raise ValueError('sum of evs need be to 510 or less!')
        else:
            self.__ev=ev
            self.__ev_hp=self.__ev[0]
            self.__ev_attack=self.__ev[1]
            self.__ev_defense=self.__ev[2]
            self.__ev_special_attack=self.__ev[3]
            self.__ev_special_defense=self.__ev[4]
            self.__ev_speed=self.__ev[5]
            self.initial_stats



    def __str__(self):
        stats=self.__initial_stats
        HP=stats[0]
        ATK=stats[1]
        DEF=stats[2]
        SpATK=stats[3]
        SpDef=stats[4]
        Speed=stats[5]
        msg = '''
                    Pokemon: {} \n
                    Pokemon Index: {}\n
                    HP: {}       Attack: {}\n
                    Defense: {}  Special Offense:{}\n
                    Special Defense: {}   Speed: {}\n
                    Nature: {}           Ability:{}\n
                    Item: {}

                    Move: \n
              '''.format(self.name,self.__id,HP,ATK,DEF,SpATK,SpDef,Speed,self.__nature,self.ability,self.item)

        try:
            for move in self.__moves:
                    msg+='      {}   '.format(move.name)
        except:
            pass
        return msg


    def get_health_bar(self):
        if self.__is_dynamax:
           num=self.in_battle_hp//10*(0.5+0.05*self.__dynamax_level)
           len=self.initial_stats[0]//10*(0.5+0.05*self.dynamax_level)
        else:
           num=self.in_battle_hp//10
           len=self.initial_stats[0]//10
        bar="#"*int(num)+"-"*(int(len)-int(num))
        return bar


    def myteam_format(self):
        msg="""
             {} {}\n
             {}/{}  {}     {}
            """.format(self.name,self.get_health_bar(),self.in_battle_hp,self.initial_stats[0],self.gender,self.item)
        return msg

    def opponent_team_format(self):
        msg="""
            {} {}   {}
            """.format(self.name,self.get_health_bar(),self.gender)
        return msg


    def get_current_status(self):
        '''
        get in battle status

        '''
        msg = '''
                    Pokemon: {} \n
                    Pokemon Index: {}\n
                    HP: {}\n
                    Attack: {}\n
                    Defense: {}\n
                    Special Offense:{}\n
                    Special Defense: {}\n
                    Speed: {}\n
              '''.format(self.name,self.__id,self.__battle_stats[0],self.__battle_stats[1],self.__battle_stats[2],self.__battle_stats[3],self.__battle_stats[4],self.__battle_stats[5])
        print(msg)
        return

    @property
    def moves(self):
        final_list=[]
        for move in self.__moves:
            final_list.append(move.name)
        return final_list


    @moves.setter
    def moves(self,moves):
        self.__moves=moves

    def replace_move(self,move,replace:int):
        if replace<len(self.__moves) and len(self.__moves)<4:
            self.__moves.append(move)
        else:
            self.__moves[replace-1]=move

    @property
    def hp(self):
        return self.__battle_hp

    @hp.setter
    def take_damage(self,damage:int):
        self.__battle_hp=max(0,self.__battle_hp-damage)

    @hp.setter
    def heal(self,heal:int):
        if self.__is_dynamax==0:
            self.__battle_hp=min(self.__initial_stats[0],self.__battle_hp+heal)
        else:
            self.__battle_hp=min(self.__initial_stats[0]*(0.5+0.05*self.__dynamax_level),self.__battle_hp+heal)

    @property
    def dynamax_level(self):
        return self.__dynamax_level

    @dynamax_level.setter
    def dynamax_level(self,level):
        self.__dynamax_level=level

    @property
    def is_dynamax(self):
        return self.__is_dynamax

    @is_dynamax.setter
    def is_dynamax(self,dynamax):
        self.__is_dynamax=dynamax
        if dynamax==1:
            self.__battle_hp=self.__battle_hp*2

    @property
    def item(self):
        try:
            return self.__item.name
        except:
            return None

    @item.setter
    def item(self,item):
        self.__item=item

    @property
    def ability(self):
        try:
            return self.__ability.name
        except:
            return None

    @ability.setter
    def ability(self,item):
        self.__item=item

    @property
    def faint(self):
        if self.__battle_hp<=0:
            self.__is_faint=1
            return 1
        else:
            return 0



    @property
    def has_condition(self):
        return self.paralysis|self.toxic|self.sleep|self.freeze|self.poison

    @property
    def is_confused(self):
        return self.confuse

    @property
    def is_unmoveable(self):
        return self.is_unmoveable












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
