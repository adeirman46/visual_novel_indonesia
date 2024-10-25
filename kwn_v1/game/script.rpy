# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("Putri", color="#b8b665")

# define irman, color red burgundy
define i = Character("Irman", color="#800000")

# image for eileen
image putri happy = im.Scale("putri.png", 1920/1.5, 1080/1.5)

image ikn = im.Scale("ikn.png", 1920, 1080)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene ikn fullscreen
    show ikn

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show putri happy

    # These display lines of dialogue.

    p "Hi, Irman, how was your day?"


    hide putri happy

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

    hide irman happy
    show putri happy

    # make italic
    p "{i} I am doing well too."

    hide putri happy
    show irman happy

    # make bold
    i "{b} That's good to hear."

    

    # This ends the game.

    return
