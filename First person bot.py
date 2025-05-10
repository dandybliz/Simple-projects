#First Person bot
N_COLS = 3 #World size
N_ROWS = 3

def main():
    print (f"Welcome to first person Karel. You're at row 1, column 1, facing East (facing column {N_COLS})")

    facing_direction = 'East'
    curr_row = 1
    curr_column = 1
    
    action = input ("What would you like to do? You can move and turn left. Press enter to finish.")
    while action != "" : #if the user enter nothing on action = exit loop
        while action != 'move' and action != 'turn left': #user can only type move or turn left
            print ('Please type only move or turn left!')
            action = input ("What would you like to do? You can move and turn left. Press enter to finish.")
        if action == 'move':
            if facing_direction == 'East' and curr_column < N_COLS : #this will check as long as bot didnt at the edge of the world he still can move
                curr_column += 1
            elif facing_direction == 'North' and curr_row < N_ROWS :
                curr_row += 1
            elif facing_direction == 'West' and curr_column > 1 :
                curr_column -= 1
            elif facing_direction == 'South' and curr_row > 1 :
                curr_row -= 1
            else :
                print ("You cannot move again!")
            print (f"You are now at row {curr_row} and column {curr_column} with facing direction to the {facing_direction}")
                
        if action == "turn left" : #iterating rotation variable for facing direction of the bot
            if facing_direction == 'East':
                facing_direction = 'North'          
            elif facing_direction == 'North' :
                facing_direction = 'West'    
            elif facing_direction == 'West':
                facing_direction = 'South'
            elif facing_direction == 'South':
                facing_direction = 'East'
            print (f"You turned left and now facing {facing_direction}")
        
        action = input ("What would you like to do? You can move and turn left. Press enter to finish.")
    print (f"You've ended up at row {curr_row} and column {curr_column} facing {facing_direction}")
     
main()
        
