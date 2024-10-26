# Define characters
define n = Character("Narrator", color="#ffffff")
define p = Character("Professor", color="#b8b665") 
define s = Character("Student", color="#800000")

# Define images
image classroom = im.Scale("ikn.png", 1920, 1080)
image professor normal = im.Scale("putri.png", 1920/1.5, 1080/1.5)
image student normal = im.Scale("irman.png", 1920/1.5, 1080/1.5)
image narrator normal = im.Scale("soldier.png", 1920/1.5, 1080/1.5)
image indonesia = im.Scale("indonesia.png", 1920, 1080)

label start:
    scene classroom


    call variables

    while game_running:
        "[hours]:[minutes]:[seconds]"
        $ seconds += 1
        if seconds == 60:
            $ seconds = 0
            $ minutes += 1
        if minutes == 60:
            $ minutes = 0
            $ hours += 1

    show narrator normal

    n "Hi [player_name], welcome to the Introduction to Geopolitics and Geostrategy class."
    
    # n "Welcome to the Introduction to Geopolitics and Geostrategy class."

    show professor normal
    hide narrator normal

    p "Today we'll discuss Indonesia's strategic position in Asia."

    p "Indonesia's location between the Indian and Pacific Oceans makes it a key player in regional geopolitics."

    p "Let's start with some basic concepts. What aspects of geopolitics interest you most?"

    hide professor normal
    show student normal

    menu:
        "Maritime Strategy":
            s "I'm interested in Indonesia's maritime strategy and its importance."
            jump maritime_discussion
            
        "Regional Cooperation":
            s "How does Indonesia work with other Asian nations?"
            jump regional_cooperation
            
        "Economic Development":
            s "I want to learn about Indonesia's economic potential."
            jump economic_development

label maritime_discussion:
    hide student normal
    show professor normal
    
    p "Excellent choice! Indonesia's archipelagic geography makes maritime strategy crucial."
    
    p "As the world's largest archipelagic state, Indonesia connects major sea lanes of communication."
    
    p "This position brings both opportunities and responsibilities."
    
    jump main_discussion

label regional_cooperation:
    hide student normal
    show professor normal
    
    p "Indonesia plays a central role in ASEAN and regional diplomacy."
    
    p "Our position allows us to be a bridge between different regions and cultures."
    
    p "This helps maintain regional stability and promotes peaceful cooperation."
    
    jump main_discussion

label economic_development:
    hide student normal
    show professor normal
    
    p "Indonesia has vast natural resources and a large, young population."
    
    p "These factors give us significant economic potential in the Asian century."
    
    p "Strategic development of our resources and human capital is key."
    
    jump main_discussion


label variables:
    $ player_scores = 0
    $ player_name = "Ade"
    $ hours = 0
    $ minutes = 0
    $ seconds = 0
    $ game_running = True

    if player_scores == 10:
        "Score is 10"

    return


label main_discussion:
    p "Now, let's discuss how these factors interact to shape Indonesia's future."

    p "A strong understanding of geopolitics helps us make better strategic decisions."

    p "Remember, our goal is to contribute to regional peace and prosperity."

    hide professor normal
    show student normal

    s "Thank you, Professor. This helps me understand Indonesia's role better."

    hide student normal
    show professor normal

    p "You're welcome. Keep studying these concepts - they're crucial for our future."



    # End of the lesson
    return


