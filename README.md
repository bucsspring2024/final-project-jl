[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14657238&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Jalatro
## CS110 Final Project Spring 2024

## Team Members

Josh Levine

***

## Project Description

Making a copy of the game Balatro, a poker deckbuilder roguelike. Allows the user to take a deck starting with 52 cards and play poker hands to acquire chips, based on pre-determined combinations of chips and multiplier, which can be increased by acquiring "joker" cards from the shop in between rounds. Three rounds per stage, with increasing total chip requirements as you progress. Money is acquired for each round completed. Special types of cards can be bought from the shop to increase multipliers for different types of hands, and to modify cards of the deck.

I am very aware that this is already a game, I plan on remaking the game from scratch to the best of my ability.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Deck of cards
2. Shop with jokers, and modifier cards
3. Scaling difficulty rounds
4. Money with purchasing value in the shop
5. Values of chips and multipliers for different levels of hands

### Classes

Card - Different cards in deck, with internal values of 'value' and 'suit'
Joker - Jokers with different internal values defining different abilities
Special - Special cards bought from shop with different properties, such as removing cards from deck, changing internal values of cards in deck, or increasing Chips and Mult for a specific Hand.
Hands - Different poker hands with internal values of 'chips' and 'mult'
Chips - Multiplier amount to find total, based on original defined value for Hands combined with the increased value from the shop
Mult - Multiplier amount to find total, based on original defined value for Hands combined with the increased value from the shop
Total - Total amount of chips required to complete each stage
Money - Total money owned, and increased by each stage with varying amounts per stage

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
