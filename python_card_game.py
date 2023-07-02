#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Author: Eden Tay
Creation date: 17/3/2023
Last modified date: 31/3/2023
Program Description: This program is a text-interface based card game
created as part of an assignment for FIT9136. The player competes with
a robot (the computer) by drawing cards from a deck and getting a winning
combination and meeting the "winning criteria" before the robot does.  
"""


# # Task 1. Game menu function

# In[2]:


def menu():
    """Game menu function. Displays menu options. 
    -------
    No parameters.
    -------
    Function does not return a value.
    """

    print("\n____________________\n\
    Please select one of the following actions \n\
    1: Start new round\n\
    2: Pick card\n\
    3: Shuffle deck\n\
    4: Show my cards\n\
    5: Check Win/Lose\n\
    6: EXIT")


# # Task 2. Create Deck function

# In[6]:


# testsuit =  ["♥", "♦", "♣", "♠"]
# card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# testdeck = []


def new_deck(deck, suit, values):
    """This function generates a new deck from a complete combination of suits 
    and values by concatenating each value with each icon in the shosen suit.
    The combined string is appended to the deck to act as a card.
    -------
    Parameters
    deck = list 
    suit = list
    values = list
    -------
    Function does not return a value.
    -------
    Example:
    suit = ["♥", "♦", "♣", "♠"]
    card_value = ["2", "3", "4"]
    testdeck = []
    new_deck(testdeck, suit2, card_values)
    >>> print(testdeck)
    ['2♥', '3♥', '4♥', '2♦', '3♦', '4♦', '2♣', '3♣', '4♣', '2♠', '3♠', '4♠']
    """

    deck.clear()  # clear old deck if any
    for icon in suit:
        for value in values:
            deck.append(str(value) + str(icon))


# deck creation test
# new_deck(testdeck, testsuit, card_value)
# print(testdeck)


# # Task 3. Shuffle Deck function

# In[4]:


# Test inputs
# import random
# suit_choice = ['♥', '♦', '♣', '♠']
"""playdeck = ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'J♥', 'Q♥',\
              'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦',\
              'J♦', 'Q♦', 'K♦', 'A♦', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣',\
              '8♣', '9♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♠', '3♠', '4♠', '5♠',\
              '6♠', '7♠', '8♠', '9♠', 'J♠', 'Q♠', 'K♠', 'A♠']
"""


def shuffle(deck, used_suits):
    """This function allows user to shuffle the deck using 
    the "random" library's shuffle function. After shuffling, 
    the deck always maintains the order where the first card is
    the 'A' card of the first suit in the suits list, the middle position
    (i.e., round((𝑛+1)/2, 0))) is the 'Q' card of the second suit in the suits list,
    and the last card is the 'K' card of the last suit in the suits list. 
    -------
    Parameters:
    deck = list 
    used_suit = list
    -------
    Function does not return a value.
    -------
    Example:
    suit = ["♥", "♦", "♣", "♠"]
    testdeck =  ['2♥', '3♥', '4♥', '2♦', '3♦', '4♦', '2♣', '3♣', '4♣', '2♠', '3♠', '4♠']
    shuffle(testdeck, suit)
    """

    import random

    #    Pre-shuffle tests:
    #    print(deck[0]) # check fixed cards positions
    #    print(deck[6]) # check position card

    total_cards = len(deck)
    fixed_cards = ['A' + used_suits[0], 'Q' + used_suits[1], 'K' + used_suits[-1]]
    present_fixed_cards = [fcard for fcard in fixed_cards if fcard in deck]
    shuffled_deck = [card for card in deck if card not in present_fixed_cards]  # new deck without fixed position cards
    random.shuffle(shuffled_deck)

    #    Test
    #    print(shuffled_deck[6]) # check position card after shuffle

    if fixed_cards[0] in present_fixed_cards:
        shuffled_deck.insert(0, fixed_cards[0])
    if fixed_cards[1] in present_fixed_cards:
        shuffled_deck.insert(int(round((total_cards + 1) / 2, 0)), fixed_cards[1])
    if fixed_cards[2] in present_fixed_cards:
        shuffled_deck.append(fixed_cards[2])

    deck.clear()
    deck.extend(shuffled_deck)
    print("Shuffle complete!")


#    Test
#    print(deck[0], deck[int(((total_cards + 1) / 2))], deck[-1]) # check fixed positions

# shuffle test
# shuffle(playdeck, suit_choice)


# # Task 4. Pick Card function

# In[5]:


""" playdeck = ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'J♥', 'Q♥', 'K♥',\
                'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'J♦','Q♦',\
                'K♦', 'A♦', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'J♣',\
                'Q♣', 'K♣', 'A♣', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠',\
                'J♠', 'Q♠', 'K♠', 'A♠']
"""


def drawcard(deck):
    """This function randomly draws a card from deck. It then
    removes the drawn card from deck. This function is used by 
    both the player and robot.
    -------
    Parameters:
    deck = list 
    -------
    Function returns a "card" in string format. 
    -------
    Example:
    testdeck =  ['2♥', '3♥', '4♥', '2♦', '3♦', '4♦', '2♣', '3♣', '4♣', '2♠', '3♠', '4♠']
    print(drawcard(testdeck))
    print(testdeck)
    >>>
    '4♥'
    ['2♥', '3♥', '2♦', '3♦', '4♦', '2♣', '3♣', '4♣', '2♠', '3♠', '4♠']
    """

    import random

    if len(deck) == 0:  # prevent invalid draw
        return ''
    #    print(len(deck))
    card = random.choice(deck)
    deck.remove(card)
    #    print(card)
    #    print(len(deck))
    return card


# pick card test
# drawcard(playdeck)


# # Task 5. Show Cards function
# 

# In[6]:


# testhand = ['6♥', '3♥', '4♥', '9♥', '7♥']


def show(hand):
    """Funtion displays the player's hand.
    -------
    Parameters:
    hand = list 
    -------
    Function does not return a value. 
    -------
    Example:
    testhand = ['6♥', '3♥', '4♥', '9♥', '7♥']
    show(testhand)
    >>>
    6♥ 3♥ 4♥ 9♥ 7♥
    """

    print(f"\nYour cards: {' '.join(hand)}")


# show card test
# show(playhand)


# # Task 6. Check Result functions
# 

# In[7]:


# Test Values:
# testsuit = ['♥', '♦', '♣', '♠']
# testhand = ['8♠', 'A♣', '2♣', '2♥', '2♦', '10♣']


def matching_values(hand, suits):
    """Function checks for conditions 1 and 2 for winning the game.
    Condition 1: Hand has same value cards for all defined suits.
    Condition 2: Hand has same calue cards for at least (total defined suits)-1
    -------
    Parameters:
    hand = list 
    suits = list
    -------
    If condition 1 is met, funtion returns True.
    If only condition 2 is met, return the highest count of same value cards.
    If neither conditions met, return 0.
    -------
    Example:
    suit = ["♥", "♦", "♣", "♠"]
    testhand =  ['2♥', '2♦', '2♣', '2♠', '3♠', '4♠']
    matching_values(testhand, suit)
    >>>
    True
    """

    while len(hand) == 0:
        return 0
    hand_val = [card[0:-1] for card in hand]  # create temporary deck of only values
    #        print(hand_val)    # test temporary deck
    matches = 0
    for value in hand_val:  # find repeated values
        repeats = hand_val.count(value)
        while repeats == len(suits) or repeats == 6:
            # print("Full suit. Stop.")
            return True
        while repeats > matches and hand_val.count(value) >= len(suits) - 1:
            matches = repeats
            # print(matches) # test condition filter
            return matches
    return 0


# Test function:

# print(matching_values(testhand, testsuit))


# In[9]:


# Test values:
# testconvert = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
# testhand = ['K♥', 'J♦', '10♣', '8♠', 'Q♠', 'A♠']


def convert_letter(hand, conversion_values):
    """Function converts non-numerical card values in a hand to numerical
    and converts the card values string to integer.
    -------
    Parameters:
    hand = list
    conversion_values = dict
    -------
    Funtion returns a new list containing integers.
    -------
    Example:
    convert = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    testhand = ['J♥', 'J♦', '2♣', 'K♠', 'Q♠', 'A♠']
    print(convert_letter(testhand, convert))
    >>>
    ['11', '11', '2', '13', '12', '1']
    """
    hand_value = [conversion_values[card[:-1]] if card[:-1]
                  in conversion_values.keys() else int(card[:-1]) for card in hand]
    return hand_value


# Test function:
# print(convert_letter(testhand, testconvert))


# In[9]:


# test variables for check result
# suit_choice = ['♥', '♦', '♣', '♠']
# player_hand = ['8♠', 'A♣', '2♣', '8♥', '10♣']
# robot_hand = ['10♥', '4♠', 'Q♠', '9♥']

def result(player_cards, robot_cards, suit):
    """Function compares the combination of cards held by the player and the robot
    to determine if the player has won the game.
    -------
    Parameters:
    player_cards = list
    robot_cards = list
    suit = list
    -------
    Function returns True if player wins
    False if robot wins
    -------
    Example:
    testsuit = ['😃', '😈', '😵', '🤢', '😨']
    testplayer = ['A😃', 'A😈', 'A😵', 'A🤢', 'A😨', K😨']
    testrobot = ['2😃', '3😃', '2😵', '2🤢', 4😨', 5😨']
    print(result(testplayer, testrobot, testsuit))
    >>>
    👏👏👏 YOU WON 👏 👏 👏
    Player had all suits of the same value
    True
    """
    #   code returns True if player has more than (suit length - 1) cards of same suit
    #   and more of them than robot does

    player_condi1 = matching_values(player_cards, suit)
    robot_condi1 = matching_values(robot_cards, suit)

    if len(robot_cards) == 0 and len(player_cards) >= 1:
        print("👏👏👏 YOU WON 👏 👏 👏\nRobot did not have any cards")
        return True
    if player_condi1 is True:
        print("👏👏👏 YOU WON 👏 👏 👏\nPlayer had all suits of the same value")
        return True
    if robot_condi1 is True:
        print("🤖PLAYER LOST THE ROUND... 🤖\nRobot had all suits of the same value")
        return False
    if player_condi1 > robot_condi1:
        print("👏👏👏 YOU WON 👏 👏 👏\nPlayer had all but 1 suits of the same value")
        return True
    if player_condi1 < robot_condi1:
        print("🤖PLAYER LOST THE ROUND... 🤖\nRobot had all but 1 suits of the same value")
        return False

    #   code returns True if player has more cards in second suit than robot. False if robot has more
    player_condi3 = (''.join(player_cards)).count(suit[1])
    robot_condi3 = (''.join(robot_cards)).count(suit[1])
    if player_condi3 > robot_condi3:
        print("👏👏👏 YOU WON 👏 👏 👏\nPlayer had more suit 2 cards")
        return True
    if player_condi3 < robot_condi3:
        print("🤖PLAYER LOST THE ROUND... 🤖\nRobot won with more suit 2 cards")
        return False

    #   code returns True if player has higher card average
    #   Lines 57-62 converts J to 11, Q to 12, K to 13, A to 1
    conversion_chart = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    player_values = convert_letter(player_cards, conversion_chart)
    robot_values = convert_letter(robot_cards, conversion_chart)

    #   calculate and compare card averages
    player_average = sum(player_values) / len(player_cards)
    robot_average = sum(robot_values) / len(robot_cards)

    if player_average > robot_average:
        print(f"👏👏👏 YOU WON 👏 👏 👏\nPlayer has a higher average.\n\
              Player's average = {round(player_average, 3)}\n\
              Robot's average = {round(robot_average, 3)}")
        return True

    elif player_average < robot_average:
        print(f"🤖PLAYER LOST THE ROUND... 🤖\nRobot has a higher average.\n\
              Robot's average = {round(robot_average, 3)}\n\
              Player's average = {round(player_average, 3)}")
        return False

    elif player_average == robot_average:
        print("🫢---- DRAW! ----🤖")
        return

    else:
        print("Error occured, invalid results.")


# check result test
# print(result(player_hand, robot_hand, suit_choice))


# # Task 7. Play Game functions

# In[10]:


# Test variables
# suit1 = ['♥', '♦', '♣', '♠']
# suit2 = ['😃', '😈', '😵', '🤢', '😨']
# suit3 = ['🤡', '👹', '👺', '👻', '👽', '👾', '🤖']
# suit_list = [suit1, suit2, suit3]

def game_intro(allsuits):
    """Function displays guide to using the menu and the rules of the game when called.
    -------
    Parameters:
    suit_list = list of lists
    -------
    Function returns no value.
    """
    # print guide to menu and suit selection
    print(f"Welcome to the game. To select an option from the menu,",
          "simply key the number on the left.",
          "\nWhen starting a game, you may choose a suit for the deck.",
          "The list of available suits are:\n")
    for i in range(len(allsuits)):
        print(f"{i + 1}) {allsuits[i]}\n")
    print("To select a suit when starting a new game,",
          "key in the corresponding suit number\nwhen you are selecting",
          "the \"Start new round\" option from the game menu.",
          "\ni.e.     < 1 2 > or < 1 3 >",
          "\nif no suit options were made, a new game will start with suit 1.\n")
    # print summarised rules
    print("\n_________________________RULES_______________________________",
          "\nThe rules of this game are simple. You are playing against a robot.",
          "\nEach turn, you may draw a card from the deck or compare your cards using",
          "the \"check results\" option.\n-[NOTE]- You can hold a MAXIMUM of 6 cards.",
          "\nTo win, you must meet one of the following requirements",
          "(listed in order of importance):",
          "\n\n1) You have all cards of the same value,",
          "for every suit icon available, in your hand.\n",
          "e.g. ['5♣','5♠', '5♦','5♥', '6♦', '3♦']",
          "\nIf the number of suit icons > 6, you must have",
          "6 different icons of the same value in your hand.",
          "\n\n2) You have all cards of the same value except one,",
          "for every suit icon available, in your hand",
          "\ne.g. ['5♣','5♠', '5♦','6♥', '6♦', '3♦']",
          "\n\n3) You hold more cards from the 2nd icon of the playing suit than your oponent",
          "\n\n4) You have a higher average card value than your oponent.",
          "\n\nIf you fail to meet a requirement while the robot does, you lose the round.",
          "\n\nGood Luck!")


# test function
# game_intro(suit_list)


# In[11]:


def reset_cards(maindeck, player, robot):
    """Function resets the playing deck and participants' cards 
    by clearing them to prepare for a new round.
    -------
    Parameters:
    main = list
    player = list
    robot = list
    -------
    Function returns no value.
    """
    maindeck.clear()
    player.clear()
    robot.clear()


# In[12]:


def show_all_hands(player, robot):
    """Displays hands of all players when results are shown.
    -------
    Parameters:
    player = list
    robot = list
    -------
    Function does not return a value.
    """
    show(player)
    print(f"Robot's cards: {' '.join(robot)}")


# In[ ]:


def play():
    """
    Manages all aspects of gameplay. When the function is invoked,
    it should display a menu that allows the user to select
    menu options and card suit types by typing a number or letter.
    When number of cards in hand reach 6, final result will be displayed
    and automatically restart the game until user exits game.
    -------
    Funtion has no parameters.
    -------
    Function returns no value.
    """
    import random

    suit1 = ["♥", "♦", "♣", "♠"]
    suit2 = ["😃", "😈", "😵", "🤢", "😨"]
    suit3 = ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]
    suits = [suit1, suit2, suit3]
    card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    playdeck = []
    player_hand = []
    robot_hand = []

    game_intro(suits)
    force_restart = [0, 0]
    while True:
        menu()
        if force_restart[0] == 1:
            user_option = '1'
        else:
            user_option = input("Choice: ")
        #        print(user_option)
        if len(user_option) < 1:
            continue
        user_option = [int(num) for num in user_option if num.isnumeric()]
        #        print(user_option)

        #        --- start new game ---
        if user_option[0] == 1 or force_restart[0] == 1:
            reset_cards(playdeck, player_hand, robot_hand)
            print("Starting a new round...")
            if len(user_option) == 2 and sum(user_option) > 4:
                print("\nInvalid suit selected. Please select a suit from 1 to 3 instead.")
                continue

            if len(user_option) == 1 and force_restart[1] == 0:
                suit_choice = suits[0]
                print(f"\nSuit for this round: {suit_choice}")
                new_deck(playdeck, suit_choice, card_value)
                #                print(playdeck) # check new_deck()
                shuffle(playdeck, suit_choice)
                print("Deck ready.\n--- ROUND STARTED ---")
            #                print(playdeck) # check shuffle

            else:
                if force_restart[0] == 1:
                    suit_choice = force_restart[1]
                elif len(user_option) < 2 or user_option[1] < 1:
                    suit_choice = suits[0]
                else:
                    suit_choice = suits[user_option[1] - 1]
                print(f"\nSuit for this round: {suit_choice}")
                new_deck(playdeck, suit_choice, card_value)
                shuffle(playdeck, suit_choice)
                print("Deck ready.\n--- ROUND STARTED ---")
            force_restart[0] = 0
        #                print(playdeck) # check shuffle

        #        --- pick a card ---
        elif user_option[0] == 2:
            while len(playdeck) == 0:
                print("\n🚫Invalid move. DECK IS EMPTY🚫\nPlease start a new round")
                continue
            player_hand.append(drawcard(playdeck))
            #            randomized robot draw
            robo_draw = random.randint(0, 2)  # increase range to increase chance of robot drawing
            if robo_draw >= 1:
                robot_hand.append(drawcard(playdeck))
            #                print("robot drew a card")
            if len(robot_hand) >= 6 or len(player_hand) >= 6:
                show_all_hands(player_hand, robot_hand)
                result(player_hand, robot_hand, suit_choice)
                reset_cards(playdeck, player_hand, robot_hand)
                force_restart[0] = 1
                force_restart[1] = suit_choice
            else:
                show(player_hand)

        #        --- shuffle deck ---
        elif user_option[0] == 3:
            if len(playdeck) == 0:
                print("\n🚫Invalid move. DECK IS EMPTY🚫\nPlease start a new round")
                continue
            shuffle(playdeck, suit_choice)

        #        --- show hand ---
        elif user_option[0] == 4:
            if len(player_hand) == 0:
                print("\n🚫Invalid move. You have no cards in hand.🚫")
                continue
            show(player_hand)

        #        --- check results ---
        elif user_option[0] == 5:
            if len(player_hand) == 0:
                print("\n🚫Invalid move. You have no cards in hand.🚫")
                continue
            show(player_hand)
            print(f"Robot's cards: {' '.join(robot_hand)}")
            if result(player_hand, robot_hand, suit_choice) is True:  # player wins
                #                print("CONGRATS! YOU WON THE ROUND \O/")
                reset_cards(playdeck, player_hand, robot_hand)
            elif result(player_hand, robot_hand, suit_choice) is False:  # robot wins
                #                print("🤖PLAYER LOST THE ROUND... 🤖")
                reset_cards(playdeck, player_hand, robot_hand)
            else:
                print("Start new round for rematch")
                reset_cards(playdeck, player_hand, robot_hand)

        elif user_option[0] == 6:
            print("... QUITTING THE GAME ...")
            reset_cards(player_hand, robot_hand, suit_choice)
            print("...👋 Goodbye 👋...")
            break


# play game!
play()

# In[ ]:
