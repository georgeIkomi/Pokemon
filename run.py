class Pokemon:
    """
    This Pokemon class serves as a template for
    creating instances of this class (i.e for
    creating Pokemon objects)
    """
    def __init__(self, name, type, level):
        self.name = name
        self.level = level
        self.type = type
        self.base_max_health = 100
        self.base_attack = 100
        self.base_defense = 100
        self.regenerative = False

    def __repr__(self):
        """
        This method is used to instruct Python what
        the preferred string representation of this
        class should be. Here, it simply returns the
        .name attribute of the newly instantiated Pokemon
        object.
        """
        return self.name

    def set_stats(self):
        """
        This method initializes or sets up the specified instance
        variables for every instantiated Pokemon object at the
        start or beginning of each new game. The assigned
        initialization values for each of the instance variables
        is allotted using a lambda function (which accepts 1 parameter) 
        and a formula. The lambda function applies the formula to
        the accepted parameter and calculates the initialization value
        that is  assigned to each of the instance variables at the start
        or beginning of a new game. 
        """
        level_stat = lambda x: int(x*(2+self.level)/3)
        self.max_health = level_stat(self.base_max_health)
        self.current_health = self.max_health
        self.attack = level_stat(self.base_attack)
        self.defense = level_stat(self.base_defense)

    def info(self):
        """
        This method provides certain information about
        each Pokemon held by a trainer or player during
        game time.
        """
        print(
            f"\t{self}: {self.type}, level {self.level}")
        reg_text = ", regenerative" if self.regenerative else ""
        print(
            f"Health: {self.current_health} (of {self.max_health}){reg_text}")
        print(f"Attack: {self.attack})")
        print(f"Defense: {self.defense}")

    def lose_health(self, amount):
        """
        This method deducts health from a pokemon and 
        prints the current health remaining.
        """
        amount = min(amount, self.current_health)
        self.current_health -= amount
        print(
            f"{self} loses {amount} of health and has {self.current_health} of health now")

    def gain_health(self, amount):
        """
        This method adds to a pokemon's health and prints
        the total current health level.
        """
        amount = min(amount, self.max_health - self.current_health)
        self.current_health += amount
        print(
            f"{self} gains {amount} of health and has {self.current_health} of health now")

    def regenerate(self):
        """
        This method provides each trainer or player with
        the ability to regenerate the health level a pokemon
        after sustaining damage in the course of battling
        other pokemons. This is achieved by passing a
        percentage of the maximum health of the pokemon
        as a parameter to the gain_health method which
        then adds this amount to the health of the pokemon. 
        """
        if self.current_health < self.max_health:
            print(f"{self} regenerates")
            self.gain_health(int(self.max_health*0.2))

    def battle(self, opponent_pokemon):
        """
        This method unpacks the "attack" metric for the attacking
        pokemon and "description" metric for the pokemon being attacked
        from the battle_stats() method into the "attack" and description
        variables. The method then uses these to print out information
        about the state of play to the player/players and facilitates the
        deduction the attack value from the health of the pokemon being 
        attacked using the lose_health() method.
        """
        attack, description = self.battle_stats(opponent_pokemon)
        print(f"{self} attacks {opponent_pokemon} {description}")
        opponent_pokemon.lose_health(attack)

    def battle_stats(self, opponent_pokemon):
        """
        This method calculates the attack level (or the
        attack intensity of each pokemon) based on the types of
        of pokemons doing battle. Each type is alloted a
        value that is somewhat indicative of its attacking
        power and used in the formula for quantifying the
        attack on the opposing pokemon. Each type is also 
        allotted a description. The attack value of the 
        attacking pokemon and a brief description of 
        both the attacking and attacked pokemon are displayed 
        to the trainer or player as the pokemons fight.
        """
        types_dict = {"Water": 0, "Fire": 1, "Grass": 2}
        attack_type = (types_dict[self.type] -
                       types_dict[opponent_pokemon.type]) % 3
        attack_type_power_proportions = {0: 1, 1: 3/2, 2: 2/3}
        attack = int(self.attack/(1+opponent_pokemon.defense /
                     self.attack)*attack_type_power_proportions[attack_type])
        attack_type_description = {0: "",
                                   1: f"with element bonus: {self.type} against {opponent_pokemon.type}",
                                   2: f"with element penalty: {self.type} against {opponent_pokemon.type}"}

        return attack, attack_type_description[attack_type]

    
class AttackPokemon(Pokemon):
    """
    This AttackPokemon class serves as a template for
    creating instances of this class (i.e for
    creating subsequent AttackPokemon instances or objects), 
    and is a subclass of the parent class (Pokemon). It has
    a .__init__() method which overrides the initialization 
    .__init__() method of its superclass (Pokemon) but has the
    capability of still invoking the __init__() method of its
    parent class (Pokemon) through the use of super().
    """
    def __init__(self, name, type, level):
        super().__init__(name, type, level)
        self.base_attack = int(self.base_attack * 1.2)


class DefensivePokemon(Pokemon):
    """
    This DefensivePokemon class serves as a template for
    creating instances of this class (i.e for
    creating subsequent DefensivePokemon instances or objects), 
    and is a subclass of the parent class (Pokemon). It has
    a .__init__() method which overrides the initialization 
    .__init__() method of its superclass (Pokemon) but has the
    capability of still invoking the __init__() method of its
    parent class (Pokemon) through the use of super().
    """
    def __init__(self, name, type, level):
        super().__init__(name, type, level)
        self.base_defense = int(self.base_defense * 1.2)


class RegenerativePokemon(Pokemon):
    """
    This RegenerativePokemon class serves as a template for
    creating instances of this class (i.e for
    creating subsequent RegenerativePokemon instances or objects), 
    and is a subclass of the parent class (Pokemon). It has
    a .__init__() method which overrides the initialization 
    .__init__() method of its superclass (Pokemon) but has the
    capability of still invoking the __init__() method of its
    parent class (Pokemon) through the use of super().
    """
    def __init__(self, name, type, level):
        super().__init__(name, type, level)
        self.regenerative = True


class Trainer:
    """
    This Trainer class serves as a template for
    creating instances of this class (i.e for
    creating subsequent Trainer objects)
    """

    def __init__(self, name, pokemons, potions=3):
        """
        This method initializes newly created 
        instances of this class with the specified
        attributes.
        """
        self.name = name
        self.pokemons = pokemons
        self.active = self.pokemons[0]
        self.potions = potions

    def __repr__(self):
        """
        This method is used to instruct Python what
        the preferred string representation of this
        class should be. Here, it simply returns the
        .name attribute of the newly instantiated 
        Trainer object.
        """
        return self.name

    def info(self):
        """
        This method prints to the console information
        specific to each instance of the Trainer class
        including the number of pokemon held, number of
        potions held, information specific to each pokemon
        held, and also prints the current active pokemon to 
        the console/terminal by invoking the show_active()
        method.
        """
        print(f"\n{self} has {len(self.pokemons)} Pokemon")
        self.show_active()
        print(f"Potions: {self.potions}")
        for pokemon in self.pokemons:
            pokemom.info()

    def show_active(self):
        """
        This method prints the current active pokemon for
        each newly created instance of the Trainer class.
        """
        print(f"{self}'s active Pokemon is {self.active}")

    def battle(self, opponent_pokemon):
        """
        This method simulates the battle/fight between the
        pokemons held by different instances of the Trainer class,
        and takes the pokemon (of the opposing trainer) being attacked 
        as a parameter. It prints information regarding the current 
        attacking pokemon belonging to one trainer and the current 
        pokemon of the other trainer that's being attacked. It then
        checks to see if the current health of the pokemon being 
        attacked is equal to 0. If so, it removes the pokemon
        in question from the list of pokemons held by that trainer,
        and prints information signalling that this pokemon is
        dead. This method then checks to see if the length of 
        the list of pokemons held by the opposing trainer is 
        greater than 0. If so, it sets the current active pokemon
        to the pokemon that's next in the list of pokemons.
        Finally, it prints that information to the console/terminal.
        """
        print(f"{self} attacks {opponent_pokemon}")
        self.active.battle(opponent_pokemon.active)
        if opponent_pokemon.active.current_health == 0:
            opponent_pokemon.pokemons.remove(opponent_pokemon.active)
            print(f"{opponent_pokemon.active} dies")
            if len(opponent_pokemon.pokemons) > 0:
                opponent_pokemon.active = opponent_pokemon.pokemons[0]
                opponent_pokemon.show_active()

    def use_potion(self, pokemon):
        """
        This method (taking the pokemon as a parameter) 
        enables the trainers to use potions for the purpose 
        of healing each of the respective pokemon held. When 
        used, this method decreases the number of potions held, 
        prints information to the fact that the trainer in question
        has just used a potion on the pokemon taken in as a parameter.
        Finally it adds a pre-determined amount to the health of 
        this pokemon via the gain_health() method.
        """
        self.potions -= 1
        print(f"{self} uses potion on {pokemon}")
        pokemon.gain_health(100)


class Game:
    """
    This Game class serves as a template for
    creating instances of this class (i.e for
    creating subsequent Game objects). Each game
    play is represented by an instance of this class.
    """

    full_commands_list = ["Info", "Change active Pokemon", "Fight", "Use healing potion", "Exit"]

    def __init__(self, all_trainers):
        """
        This method initializes newly created 
        instances of this class with the specified
        attributes.
        """
        self.all_trainers = all_trainers
        self.trainers = []
        self.modes = []
        self.turn = 1
        self.computer_commands = []
        self.set_turn = True
        



