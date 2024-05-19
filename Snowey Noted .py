#!/usr/bin/Python3

# Credit to Engineer Man for this Evolution ... https://youtu.be/_chP0a4PMTM
# Additional Steers being Google ( W3Schools , GeeksforGeeks , StackOverFlow )
# Props Cybrary Foundations , Eyes Forward  >>> Network / Socket Programming 

# Import Modules ( os > clear the screen , random > generate the snow , time > for the delay )

import os
import random
import time

# State Varibles IOT Adjust Snowfalls Density and Decent ... )

SNOW_DENSITY = 7
DELAY = .5

# Sooo ... How are the Snow Flakes going to Look , C+P from https://www.namecheap.com/visual/font-generator/snowflake-text-symbols/

snowflakes = ['❆', '•', '·', '❅', '❈'] #unicode in a list

# IOT determin the Terminals Size

term = os.get_terminal_size() # () Denotes a Tasking 

w = term.columns # This gives the Terminals Width
h = term.lines   # This gives the Terminals Hight

grid = []        # Empty List ...

# Loop over every Element in the Range IOT give the Hight , Then Add One Row per Line and Multiply by the Width to Give a Grid 

for _ in range(h):
    grid.append([' '] * w) 

# Method too Draw said Grid ... E/O https://student.cs.uwaterloo.ca/~cs452/terminal.html for More ANSI Escape Codes

def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear') # This Clears the Screen using 'cls' on Windows and 'clear' on Linux

    print('\033[?25l') # This Specific Print Code removes the Curser IOT NOT Obstruct the Snow Storm 
    output = ''        # This NOW Builds an Output String ... See Next For Loop ...

    for row in grid:                  # For the Row in the Grid ...
        output += ''.join(row) + '\n' # Append too Output , Join Them as a String and then Add a new Row
    
    output = output.strip('\n')       # Strip the Final New Line from the End
    
    print(output, end='')             # Print the Output but Specify an End Line of Nothing IOT NOT add a New Line

# While Loop ( Infinite ... ) IOT Actually Make it Snow

while True:
    row = [] # To Generate the Snowflakes ... Starts Off with an Empty List
                    
    for _ in range(w):                             # Starts a For Loop using the Range from Width
        if random.random() < SNOW_DENSITY / 100:   # Random Generates a Number , Snow Density is is then Divided by 100
            row.append(random.choice(snowflakes))  # Which then uses Random Choice to pick a Snowflake
                                    
        else:                                      # If it DOSNT get a Snowflake ...
            row.append(' ')                        # Append a Single Space ' ' Character
                
    grid.insert(0, row)                            # With this List called row , Insert it at the Begging of Grid
    grid.pop()                                     # pop() removes the Element at the specified position ... Grid                                   
    draw_grid()          # Draws the Grid as a Tasking        
    
    time.sleep(DELAY)    # This is the Fall Rate using the Sleep Function from the Time Module ( Can be Adj from the Second Variable ) 
