def robot_movement(command):
    """Function to find row,column and direction after instructions execution"""
    column = 0
    row = 0
    direction  = 'S'

    for i in command:
        #traverse command string 
        if i == direction: continue
        else:
            #if i != 'M' then change direction and move forward in that direction
            if i != 'M':
                direction = i 
            if direction == 'S':
                if row < 3:
                    row += 1
            if direction == 'N':
                if row > 0:
                    row -= 1
            if direction == 'E':
                if column < 4:
                    column += 1
            if direction == 'W':
                if column > 0:
                    column -= 1

    return row, column, direction

#drivers code
command = input()    
valid_chars = ['N','S','E','W','M']

#Check that user gave correct input  
for i in list(command):
    if i not in valid_chars:
        raise ValueError('Invalid input provided')

row, column, direction = robot_movement(command)
print ('(',row,',',column,',',direction,')')




