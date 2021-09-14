from random import randint

##The introduction to the game is written out below
print "Welcome to Rayan's Text Adventure Game!\nObjective of the game: Find the key to the secret box, the location to both of which are hidden until you land on the spot where they are hidden. Enter N, E, S, or W to navigate the map or enter \"inventory\" to view your inventory.\nHow to Win: Pick up the key, add it to your inventory and then use it on the secret box. You have 35 actions to do so (including failed actions).\nGood Luck!"
start = raw_input("Enter anything to start the game: ")

##If the user entered anything then the game will begin
if(len(start) > 0):
    map = []

    inventory = []

    ##The following is the initial construction of the map that is printed out every turn
    line_a = "  |"
    line_b = "--+--+--+--+--"
    def print_a():
        map.append([line_a] * 4)

    def print_b():
        map.append([line_b])
    
    print_a()
    print_b()
    print_a()
    print_b()
    print_a()
    print_b()
    print_a()
    print_b()
    print_a()
    map.append(["\n"])

    ##Create a function to easily print the map after every turn
    def print_board():
        print "\nMap:\nEach square is a position on the map\n"
        for row in map:
            print "".join(row)

    ##The initial printing out of the map
    print_board()

    ##The initial row and column of the player
    player_x = 5
    player_y = 1

    ##The program randomly generates a location (row and column) for the key and box
    key_x = randint(1,5)
    key_y = randint(1,5)

    box_x = randint(1,5)
    box_y = randint(1,5)

    ##Everything contained in the following for loop is what occurs in a single turn for the user
    for turn in range(35):
        location = "Row:\t" + str(player_x) + "\nColumn:\t" + str(player_y)
        ## A function to display the user's position at any given point
        def print_location():
            print "\nYou are at:"
            print location
    
        print_location()

        ##This is where users can enter their actions
        move = raw_input("\nWhere would you like to go? (Enter N/E/S/W or inventory) \n")
        def ask_move():
            move

        ask_move()

        ##A function to analyze the player's move and return the appropriate results
        def after_move():
            print_board()
            ##If the player and key are in the same position
            if(player_x == key_x and player_y == key_y):
                print "You found the key!"
                inventory.append(["key"])
                print "The key has been added to your inventory."
            ##If the player and the box are in the same position
            elif(player_x == box_x and player_y == box_y):
                print "You found the secret box! (remember where this is)"
            ##If the move was not productive
            else:
                print "There is no key or box here."
            print "\nAmount of turns left: " + str(34 - turn)

        ##Function that allows the user to view their inventory
        def view_inventory():
            print inventory

        ##The following block of statements computes the user's input and adjusts their position accordingly
        if(move == "N" and player_x == 1) or (move == "S" and player_x == 5) or (move == "W" and player_y == 1) or (move == "E" and player_y == 5):
            print "Invalid move, you are attempting to leave the map."
        elif(move == "N"):
            player_x = player_x - 1
            after_move()
        elif(move == "S"):
            player_x = player_x + 1
            after_move()
        elif(move == "W"):
            player_y -= 1
            after_move()
        elif(move == "E"):
            player_y += 1
            after_move()
        elif(move == "inventory"):
            view_inventory()
        else:
            print "Invalid move. Please try again."

        ##Game ending conditions
        if(player_x == box_x and player_y == box_y and len(inventory) > 0):
            print "Congratulations! You unlocked the secret box and you won!!"
            break

        if(turn == 34):
            print "Game over, you ran out of turns to complete the objective."
            break
