# welcome message and game rules/movement function
def instructions():
    print('--------------------')
    print('Welcome to The Haunted Mansion Game')
    print("Collect 6 items to win the game, or be scared away by the ghost.")
    print('Move commands: go South, go North, go East, go West or exit '
          'to end game')
    print("Add to Inventory: get 'item name'")


# current room, inventory and items if applicable
def game_update(current_room, inventory, rooms):
    print('--------------------')
    print('You are in the {}'.format(current_room))  # Lets player know where they are currently
    print('Inventory:', inventory)
    if 'Item' in rooms[current_room].keys():  # item notification if room contains an item
        print('You see a {}'.format(rooms[current_room]['Item']))
        print('--------------------')


# end of game function
def win_lose(inventory, current_room):
    if len(inventory) == 6 and current_room == 'Storage Room':  # win condition
        print('Congratulations! You defeated the ghost, well done.')
        return True
    if len(inventory) < 6 and current_room == 'Storage Room':  # lose condition
        print('Oh no you encountered a ghost!  GAME OVER!')
        return True
    return False  # This lets the loop continue on unless one of the branch conditions is met


# main game play loop
def main():
    # full room list with items and villain
    rooms = {
        'Storage Room': {'West': 'Bedroom', 'Item': 'Ghost'},
        'Bedroom': {'South': 'Ballroom', 'East': 'Storage Room', 'Item': 'Defense Potion'},
        'Library': {'South': 'Music Room', 'Item': 'Guide Book'},
        'Music Room': {'West': 'Ballroom', 'North': 'Library', 'Item': 'Legendary Gem'},
        'Balcony': {'East': 'Ballroom', 'Item': 'Lockbox'},
        'Ballroom': {'North': 'Bedroom', 'South': 'Kitchen', 'East': 'Music Room', 'West': 'Balcony'},
        'Kitchen': {'North': 'Ballroom', 'East': 'Servant Quarters', 'Item': 'Flashlight'},
        'Servant Quarters': {'West': 'Kitchen', 'Item': 'Mace'}
    }

    # room where player will be when game starts
    current_room = 'Ballroom'

    # list of items player has collected
    inventory = []

    instructions()  # call instruction function to begin game

    while True:  # Enables main gameplay loop to continue
        end_game = win_lose(inventory, current_room)  # call win/loss conditions
        if end_game is True:
            break
        game_update(current_room, inventory, rooms)
        player_command = input('Enter your move:')
        if player_command.startswith('go '):  # Room movement loop
            noun = player_command[3:]
            if noun in rooms[current_room]:
                current_room = rooms[current_room][noun]  # current room updated based on  player command
            else:
                print('You can\'t go that way!')  # Error Message
        elif player_command.startswith('get '):  # Item retrieval loop
            noun = player_command[4:]
            if 'Item' in rooms[current_room].keys() and noun == rooms[current_room]['Item']:
                # update inventory
                inventory.append(noun)
                # remove item from rooms dictionary
                del rooms[current_room]['Item']
                # successful item retrieval statement
                print('{} retrieved!'.format(noun))
            else:
                print('You can\'t get {}'.format(noun))  # Error Message
        elif player_command == 'exit':  # Condition for exiting game before game completes
            print('Thank you for playing The Haunted Mansion Game. Hope you enjoyed it.')  # Exit Greeting
            break  # break command exits loop
        else:
            print('Invalid input!')  # Error Message


main()
