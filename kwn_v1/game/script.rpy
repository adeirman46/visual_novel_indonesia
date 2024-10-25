# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Eileen")

# define irman, color red burgundy
define i = Character("Irman", color="#800000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hi, Irman, how was your day?"

    show irman happy
    # create choices
    menu:
        "Good":
            i "It was good, thank you."
        "Bad":
            i "It was bad, thank you."
        "Neutral":
            i "It was neutral, thank you."

    i "How about you?"

    show eileen happy

    # make italic
    e "{i} I am doing well too."

    show irman happy

    # make bold
    i "{b} That's good to hear."



    # This ends the game.

    return
