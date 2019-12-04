## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Dev progress](#updates)

## General info
This is short text game stylised for the text games from 90s. You wake up in the forest and have small world to explore.

The aim of the game for now is simple - survive and maybe even have fun.

## Technologies
Project is created with:
* Python version: 3.7
* My brain version: 1.0
* My creativity: 0.1


## Setup
To run this project you need:
* Windows OS or Mac OS
* Python version 3+

To play the game you are required to write commands showcased on the screen. Possible choices are always highlighted in brackets so it might look like this:
```
You look around. You can scratch your nose or pick up the book. (scratch/book)
```
The game will tell you if you have inputted incorrect command. Also size of letters does not matter.  
There are commands that can be called all the time, with slight exceptions, which we inform during the game:
```
* stats - allows player to check his basic stats like health and attack power
```

If player enters wrong command, the game will inform him and repeat last step.
Also author does not care you can not win the game.

## Dev progress
- [x] Prepare README
- [x] Game operates with two main locations that player can switch between
    - [x] At the **City** add **Tavern** with working *Vendor*
        - [x] Add *gambling* option for **Tavern**
        - [ ] Add changing wages in *gambling*
        - [ ] Add second game in *gambling*
    - [x] Add two small easter eggs
    - [x] At the **City** add **Order** where player can get quests
        - [x] Add story progression system
        - [x] Add finishing sequence
        - [ ] Add second quest
    - [x] At **River** add simple encounter
        - [ ] Add one more opponent to choose
        - [ ] Add random encounter if player tries to flee
    - [x] At **River** add quest location
        - [x] Allow player to enter this location only with quest
        - [x] Add additional encounter with possibility of ignoring it
        - [x] Add boss fight
            - [x] Boss can be even stronger if player makes wrong choice
    - [ ] Add **Mines** as third location (needs second quest)
    - [x] Error handling
    - [x] Name generator
    - [ ] Saving and loading the game
    - [ ] Rebuild opponents into classes and rewrite encounters to simplify the code *currently in progress*
    - [x] Add command handler to simplify code
    - [x] Add ASCII graphics