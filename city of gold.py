import os


# Helper to clear the terminal screen cross-platform
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ANSI Color Codes for terminal formatting
class Colour:
    yellow = "\033[93m"
    green = "\033[92m"
    cyan = "\033[96m"
    blue = "\033[94m"
    purple = "\033[95m"
    red = "\033[91m"
    reset = "\033[0m"


def play_game():
    clear()
    print(
        Colour.yellow
        + r"""
  .----------------------------------------------------.
 /  .-.                                            .-.  \
|  /   \         The Mysterious Quest for         /   \  |
| |\_.  |                                        |    /| |
|\|  | /|           the City of Gold...          |\  | |/|
| `---' |                                        | `---' |
|       |----------------------------------------|       |
\       |                                        |       /
 \     /                                          \     /
  `---'                                            `---'
"""
        + Colour.reset
    )
    print("You are a brave young adventurer looking for the")
    print("mysterious hidden city of gold.")
    print("You believe it is hidden in this forest somewhere and")
    print("after many weeks of exploring, you have discovered a")
    print("mysterious looking cave. You walk inside...\n")
    input(Colour.green + "Press [enter] to play" + Colour.reset)
    cave()


def cave():
    while True:
        clear()
        print(Colour.cyan + "You are in a cave." + Colour.reset)
        print(r"        ___..-.")
        print(r"     ._/  __ \_`-.__")
        print(r"     / .'/##\_ `-.  \--.")
        print(r"     .-_/#@@##\  /-' `\_")
        print(r"jgs - /########\_  \._   `-")
        print(r"    ' '''''''''' '''''''\n")
        print("You can go [north], [south], [east] or [west].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "north":
            waterfall()
            break
        elif direction == "south":
            forest()
            break
        elif direction == "east":
            stream()
            break
        elif direction == "west":
            underground()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def waterfall():
    while True:
        clear()
        print(
            Colour.cyan + "You are underneath a giant waterfall." + Colour.reset
        )
        print(r"""
          ~-~`~-~-~-~-~-~-~'~-~-~
        ~ejm~-~- -~-~-~-~
       !
       !!
      ':
       !!
     ' :
      '! '
     ! :'
      :'!
      ':!
     ' '!
      :'!
      '!!
-~'~-~':!
  ~-~-~!'
   ~-~!' 
""")
        print("You can go [south] or [east].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "south":
            cave()
            break
        elif direction == "east":
            clearing()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def forest():
    while True:
        clear()
        print(Colour.cyan + "You are in a dense forest." + Colour.reset)
        print(r"""
      ---\=,__,>,_`-.  
 --z--;\" /_/   `. `.   |
 --'//`/'  `     \   '. |
 ,_\---_\._   :   `.\ |/
//--'> ___ ``-,_   \  \
'=-`',' / `-, __`-. |
//7;<\     / ,--._ ` |
-/;\'/` -='/|(    \ \
 // '\   // | `    | |
  `     .        :  | 
           :       `  
    :          |:  ||
   |   :      : |   |""")
        print("To the south, you can hear some low growling noises.")
        print("You can go [south] or [north].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "south":
            print("You are eaten by some grizzly bears... argh!!")
            game_over()
            break
        elif direction == "north":
            cave()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def stream():
    while True:
        clear()
        print(
            Colour.cyan
            + "You are next to a stream of crystal clear water."
            + Colour.reset
        )
        print("You can go [east] or [north].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "east":
            valley()
            break
        elif direction == "north":
            clearing()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def underground():
    clear()
    print(
        Colour.cyan
        + "You are underground. It is very dark here and rather unsafe."
        + Colour.reset
    )
    print("To the east is the cave from which you came.")
    print("You can go [north], [south], [east] or [west].")
    direction = input("Where would you like to go: ").strip().lower()

    if direction == "east":
        cave()
    else:
        print(
            "While you are stumbling along in the dark, you trip and fall down a chasm!"
        )
        input(Colour.green + "Press [enter] to continue." + Colour.reset)
        game_over()


def clearing():
    while True:
        clear()
        print(
            Colour.cyan
            + "You find yourself in a bright forest clearing."
            + Colour.reset
        )
        print("You can go [north], [south], [east] or [west].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "south":
            stream()
            break
        elif direction == "north":
            hut()
            break
        elif direction == "east":
            hill()
            break
        elif direction == "west":
            waterfall()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def hut():
    clear()
    print(
        Colour.cyan
        + "You are outside an old hut. It looks abandoned and run-down."
        + Colour.reset
    )
    print(r"""
                    /\ 
                /\  //\\
         /\    //\\///\\\        /\
        //\\  ///\////\\\\  /\  //\\
       /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
  /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
 / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  
/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^ 
\ ^  _\___________________|  |_____^ ^
^\  /______________________________\ ^
^  /________________________________\ 
^    ||___|___||||||||||||___|__|||   
  ^  ||___|___||||||||||||___|__|||   
 ^   ||||||||||||||||||||||||||||||ooo
oooooooooooooooooooooooooooooooooooooo
""")
    print("Suddenly out of the entrance, a troll charges at you with a giant club!")
    direction = input("Hurry!! Where do you go: ").strip().lower()

    if direction == "south":
        print(
            "You manage to sprint back the way you came as the troll runs out of breath."
        )
        input(Colour.green + "Press [enter] to continue." + Colour.reset)
        clearing()
    else:
        print(
            "You run about aimlessly but the troll catches you and has you for dinner!!"
        )
        input(Colour.green + "Press [enter] to continue." + Colour.reset)
        game_over()


def valley():
    while True:
        clear()
        print(
            Colour.cyan
            + "You stand at the bottom of a deep valley. It is cold in the shadows."
            + Colour.reset
        )
        print("You can go [north] or [west].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "north":
            hill()
            break
        elif direction == "west":
            stream()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def hill():
    while True:
        clear()
        print(
            Colour.cyan
            + "You are on top of a hill overlooking a valley."
            + Colour.reset
        )
        print(r"""                           
                        .-.  
            ^^         /   \ 
          _        .--'/\_ \
         / \_    _/ ^     \/
        /    \  /    .'   _/ 
       /\/\  /\/ :' __  ^/  ^
      /    \/  \  _/  \-' __/
    /\  .-   `. \/     \ / -.
   /  `-.__ ^   / .-'.--'    
 @/        `.  / /      `-.  
""")
        print("You feel a tingle of magic in the air.")
        print(
            "Next to you, a shimmering "
            + Colour.purple
            + "portal "
            + Colour.reset
            + "opens up to the cave that you started in."
        )
        print("You can go [south], [west] or through the [portal].")
        direction = input("Where would you like to go: ").strip().lower()

        if direction == "south":
            valley()
            break
        elif direction == "west":
            clearing()
            break
        elif direction in ["through the portal", "portal"]:
            magic_cave()
            break
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)


def magic_cave():
    clear()
    print(
        Colour.cyan
        + "You are back in the cave you started in."
        + Colour.reset
    )
    print(r"        ___..-.")
    print(r"     ._/  __ \_`-.__")
    print(
        r"     / .'/"
        + Colour.blue
        + "~~"
        + Colour.reset
        + r"\_ `-.  \--."
    )
    print(
        r"     .-_/"
        + Colour.blue
        + "~~~~~"
        + Colour.reset
        + r"\  /-' `\_"
    )
    print(
        r"jgs - /"
        + Colour.blue
        + "~~~~~~~~"
        + Colour.reset
        + r"\_  \._   `-"
    )
    print(r"    ' '''''''''' '''''''")
    print("However, there seems to be a magic staircase leading downwards.")
    print("You can go [north], [south], [east], [west] or [down].")
    direction = input("Where would you like to go: ").strip().lower()

    if direction == "down":
        finish()
    else:
        print("The magic staircase shimmers and then vanishes.")
        input(Colour.green + "Press [enter] to continue." + Colour.reset)

        if direction == "north":
            waterfall()
        elif direction == "south":
            forest()
        elif direction == "east":
            stream()
        elif direction == "west":
            underground()
        else:
            print("You can't go that way!")
            input(Colour.green + "Press [enter] to continue." + Colour.reset)
            cave()


def finish():
    clear()
    print("You have discovered the magical lost city of gold!")
    print(
        Colour.yellow
        + r"""
                     X_x
                    / \\\
                    |n| |
                  )(|_|-'X
                 /  \\Y// \
                 |A | | |A|
                 |  | | |_|
          )(__X,,|__|MEB;;;-,)(,
         /  \\\;;;;;;;;;;;;/    \
         |A | |            | U  |
        )_|  | |____)-----( |    |
       ///|__|-'////       \|___)=(__X
      /////////////         \///   \/ \
      |           |  U    U |//     \u|
      |   )_,-,___|_)=(     | |  U  |_|_X
      |  ///   \\|//   \    | |  __ |/// \
    )_')(//     \Y/     >---)=( /  \|  | |-
   //// ,\ u   u |   u /////   \|  ||__|A|-
  |  | .. |      |    ///// ,-, \__||------
 -'--'_::_|______'----| u | | | |----------
                      |___|_|_|_|----------
                         `---------------
"""
        + Colour.reset
    )
    print(
        "You fill your bags and pockets with all the treasures and gold they can hold. You have fulfilled your quest!"
    )
    print("Now, where was the exit again...?")
    input(Colour.green + "Press [enter] to continue." + Colour.reset)
    game_over()


def game_over():
    answer = (
        input(
            Colour.red
            + "Your adventure is over. Would you like to play again? [y/n]: "
            + Colour.reset
        )
        .strip()
        .lower()
    )
    if answer == "y":
        play_game()
    else:
        print("Goodbye, hope you had fun!")


# Entry point
if __name__ == "__main__":
    play_game()
