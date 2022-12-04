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





        




