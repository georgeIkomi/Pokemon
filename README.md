# Pokemon Role-Playing Game

Pokemon is a role-playing game, based originally around building a small team of
monsters to battle other monsters in a quest to become the best.

This game is a Python terminal game in which users can either play against each
other, against the computer, or have the computer play itself.

![](/assets/images/readme_intro_scrn-shot.png)

# How to play

The Pokemon universe is a fictional universe that encompasses the Pokemon media 
franchise, including stories and fictional works produced by The Pokemon Company,
Nintendo, Game Freak and Creatures, Inc.

Each user/player represented by the trainer has a set of 3 Pokemon. The Pokemon are
of different types with differing characteristics and strengths (health, attack, and
defense).

The aim is that each Pokemon of the respective user/trainer will battle/fight each other,
and who ever loses all 3 Pokemon first loses the game with the opposing user/trainer emerging as the winner. The winner will have at least 1 Pokemon that's alive whilst all
3 Pokemon of the opposing user/trainer are all dead.

In this version, the user:

    1. Chooses the first trainer mode. The options presented are either "Player" or 
       "Computer".

    2. Chooses the first trainer from the list of trainers presented.

    3. Chooses the second trainer mode. Again, the options presented are "Player" and
       "Computer" respectively.

    4. Chooses the second trainer from the list of trainers presented.

Depending on the trainer mode selected and after the second trainer has been chosen, the user is either presented with a menu of game options or the game commences and is played
without any input or interaction from the user/player.

The later is the case where "Computer" has been chosen as both the first and second trainer mode. In this case, the computer plays itself in turns.

Where "Player" has been chosen as either the first or second trainer mode, the user will be presented with a set of menu options - "Info", "Change active Pokemon", "Fight", "Use healing potion", and "Exit". Useful information about the state of each Pokemon held by each user/trainer can be gleaned by selecting the "Info" option at any time during the game.

The user/trainer who's in the "Player" mode can also select any of the other game menu options at any time during the game. For example, a user might want to change their active Pokemon which perhaps had sustained substantial damage (significant dip in health level) from the preceding round.

    5. Choose the "Fight" game menu option to commence battle in turns until all the
       Pokemon held by a user/trainer are dead.

At this point, the winning user/trainer will be displayed in the terminal.

# Features

## Existing Features

* Display of Pokemon information/stats

  - This feature displays different information or stats about the
    Pokemon held by each user or tariner at various points during
    game time.

  - This is useful to the user as it serves as a single point of 
    reference for the user to glean information.

  - Also, choosing the "Info" menu option and displaying this information
    at various points during game time provides the user with information
    that could determine the trainer or user's next move. If, for example,
    a user or trainer's current active Pokemon had been battered in an earlier
    round, the user could decide to either change their active Pokemon or use a 
    healing potion on the current active Pokemon to ramp up the health level 
    before initiating the next round of battle through selection ofthe "Fight"
    menu option.

![](/assets/images/info1_scrnshot.png)

![](/assets/images/info2_scrn-shot.png)

* Change the active Pokemon

  - This feature gives the user or trainer the ability to change the current 
    active Pokemon at any point during game time.

  - This is particularly useful as the user or trainer can change the current
    active Pokemon that has sustained substantial damage in a preceding or 
    previous fight round to a Pokemon with full health for the next or subsequent
    round.

![](/assets/images/change_active_pokemon-scrn-shot.png)

* Fight

  - This feature simulates the attack of one Pokemon on an opponent Pokemon.

  - It is beneficail to the user as they can easily glean the attaccking Pokemon
    and the Pokemon being attacked. It also presents information regarding the 
    the amount of loss in health sustained by the Pokemon being attacked and the 
    the amount of health remaining.

![](/assets/images/fight_scrn-shot.png)

* Using a healing potion on a Pokemon

  - This feature gives a uaer or trainer the ability to heal any of its Pokemon
    after losing health or sustaining damage from being attacked. It facilitates
    the addition of a set amount to the Pokemon's health when selected from the
    set of game menu options.

  - This is advantageous in that it provides the trainer or user with the ability
    to prolong a Pokemon's capability to fight or attack during the course of the
    game despite sustaining damage.

![](/assets/images/use_healing_potion_scrn-shot.png)

* Exit

  - This functionality gives the user the option of exiting or quitting at any
    point during the course of the game.

  - This feature is useful as it gives the user(s) the opportunity to terminate
    the game play gracefully if the need arises to do so at any point during the
    course of the game.

![](/assets/images/exit_scrn-shot.png)

* Regenarate a Pokemon

  - This feature is in many ways similar to that of the "Use healing potion" feature
    in that it boosts the health level of a Pokemon, thereby prolonging the Pokemon's
    ability to do battle during the course of the game. This functionality is peculiar
    to a Pokemon that is regenerative in nature, and unlike the "Use healing potion"
    feature, it adds a percentage of the maximum health to the current health of the
    Pokemon.

  - This useful as it provides yet another way for a trainer's Pokemon to recuperate
    from sustaining damage in the course of being attacked by an opposing Pokemon.

![](/assets/images/regenerate_scrn-shot.png)

* Input validation and error-checking

  - You cannot enter number input options outside the range of numbers specified as
    number options in the list of menu options.

  - You cannot enter the string equivalent of the numbered options contained in the
    list of menu options.

  - You cannot enter special characters as input values.

  - You cannot enter any input value that is not in the list of menu options.

  - Only numbers contained in the list of menu options will be considered as valid.

![](/assets/images/input1_validation_scrn-shot.png)

![](/assets/images/input_validation2_scrn-shot.png)

# Data Model

I decided to use Pokemon classes comprising of a super class and sub-classes, Trainer class, and a Game class as my model.

## Pokemon (Super class)

The main Pokemon class (super class) stores data that is common to all instances of the parent class such as the name of the Pokemon, the type of Pokemon, level, base maximum health, base attack, base defense, and regenerative set to False.

The class also has methods to help play the game and provide essential information to the user while playing the game, such as an 'info' method to print out information about the Pokemon, and a battle stats methods to enable the user monitor vital metrics about the Pokemon as they do battle.

## Pokemon (Sub-classes)

In addition to data stored by their Super class and the methods contained therein, the Pokemon Sub-classes also store data that is perculiar to the nature of the Pokemon Sub-class such as base attack for the Attack Pokemon, base defense for the Defensive Pokemon, and regenerative set to True for the Regenerative Pokemon.

## Trainer class

The Trainer class stores data that is common to all instances of this class such as the name of the trainer, the list of Pokemons held by the trainer, the active Pokemon of the trainer, and the number of potions held by the trainer.

The class also has methods to help play the game such as the info() method that prints out certain stats about the trainer like the number of Pokemon held and information about each Pokemon, and the current active Pokemon for the trainer. It also includes a method that prints out information relating to when the trainer has used a potion, on which Pokemon the potion has been used, and adjusts the health value of the Pokemon accordingly.

## Game class

Every instance of this class stores all data relating to all the trainers (collectively), all the Pokemons held by the trainers(including the number of potions held) and any other data or information that is important or useful for the purpose of playing the game.

This class contains all the methods that will enable the user to play the game such as the choose_trainers() method to enable the user choose the trainer mode and trainer that they want, the get_command() method for executing the menu option chosen by the user during game time (implemented by the start() method), and a get_computer_commands() method necessary for facilitating playing with the computer.

# Testing

  * Pokemon class & subclasses

    In testing the Pokemon class and sub-classes, a new instance of one of the sub-classes(AttackPokemon class) was created and stored in a variable.

    Each of the instance variables (.name, .level, .type, .base_max_health, etc) were then called (using the dot notation) on this new instance and printing the outcome to the terminal. The result were the corresponding values for each of the instance variables. The new instance of the Sub-class and print statements were subsequently deleted/removed.

    ![](/assets/images/pokemon_class_test1_scrn-shot.png)

    In order to test access to the following instance variables of the Pokemon class - max_health, current_health, attack, and defense, a new instance of one of the Pokemon Sub-class was created and assigned to a variable. Then an instance of the Game class was created and assigned to a variable. The .start() method was invoked on this new instance of the Game class, and with the print statement, each of the instance variables in question were then called on the instance of the Pokemon Sub-class using the dot notation. The corresponding values (last four lines of the screenshot below) for the instance variables in question were displayed in the terminal. All print statements were then subsequently removed.

    ![](/assets/images/pokemon_class_test2_scrn-shot.png)

  * Trainer class

    Testing this class involved creating new a new instance of the Pokemon Sub-classes: AttackPokemon, DefensivePokemon, and Regenerative Pokemon, and assigning each instance to a variable. As the Trainer class takes a name, and a list of pokemons as parameters, these newly created/instantiated pokemon objects will be passed into the Trainer class when creating a new instance of it.

    An instance of the Trainer class was then created and assigned to a variable. This newly created Trainer object will take a name and list of pokemon as parameters.

    Each of the instance variables (.name, .pokemons, .active, and .potions) were then called (using the dot notation) on the newly instantiated or created Trainer object and printing the outcome to the terminal. The result were the corresponding values for each of the instance variables. The new instances and print staements were subsequently removed.

    ![](/assets/images/trainer_class-test.png)

  * Game class

    In testing that an instance of the Game class is able to access the class variable and instance variables, a new instance of the class was created and assigned to variable. A list of the trainers was also created and assigned to a variable and passed into the instantiation of the Game class as a parameter.

    The class and instance variables were then called (using the dot notation) on the newly instantiated or created Game object and printing the outcome to the terminal. The result was the corresponding values for each of the instance variables and class variable. The new instances and print statements were subsequently deleted.

    ![](/assets/images/game_class-test.png)







        




