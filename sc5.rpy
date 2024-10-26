# Define characters with custom attributes
init python:
    class GameCharacter:
        def __init__(self, name, trust=0, expertise=""):
            self.name = name
            self.trust = trust
            self.expertise = expertise

    # Stats class for player attributes
    class PlayerStats:
        def __init__(self):
            self.knowledge = 0
            self.diplomacy = 0
            self.economics = 0
            self.influence = 0
            self.energy = 100
            self.money = 1000
            self.inventory = []
            self.research_points = 0
            self.relationships = {}
            self.visited_places = set()
            self.completed_missions = set()
            self.current_mission = None

# Define persistent game data
default persistent.achievements = set()
default persistent.unlocked_locations = set()

# Game characters
define professor = Character("Professor Wijaya", color="#b8b665", image="professor")
define assistant = Character("Assistant Dewi", color="#4a90e2", image="assistant")
define diplomat = Character("Ambassador Chen", color="#e74c3c", image="diplomat")
define economist = Character("Dr. Suharto", color="#2ecc71", image="economist")
define military = Character("General Sudirman", color="#95a5a6", image="military")
define n = Character("Narrator", color="#ffffff")

# Initialize game variables
default player = PlayerStats()
default current_location = "Jakarta"
default time_of_day = "Morning"
default day_counter = 1
default active_crises = []
default mission_log = []
default current_event = None

# Custom screens
screen stats_display():
    frame:
        xalign 0.99 yalign 0.02
        vbox:
            text "Day: [day_counter]" size 20
            text "Time: [time_of_day]" size 20
            text "Money: $[player.money]" size 20
            text "Energy: [player.energy]%" size 20
            text "Knowledge: [player.knowledge]" size 20
            text "Diplomacy: [player.diplomacy]" size 20
            text "Economics: [player.economics]" size 20
            text "Research Points: [player.research_points]" size 20

screen mission_tracker():
    frame:
        xalign 0.01 yalign 0.02
        vbox:
            text "Current Mission:" size 20
            if player.current_mission:
                text "[player.current_mission]" size 18
            text "Active Crises:" size 20
            for crisis in active_crises:
                text "- [crisis]" size 18 color "#ff0000"

# Game start
label start:
    # Initialize game settings
    $ player = PlayerStats()
    $ time_of_day = "Morning"
    $ day_counter = 1
    
    scene classroom
    show screen stats_display
    show screen mission_tracker
    
    n "Welcome to the Indonesian Institute of Geopolitical Studies."
    
    # Character creation
    $ player_name = renpy.input("Enter your name:")
    $ player_background = menu([
        ("Military Strategy", "military"),
        ("Economic Analysis", "economic"),
        ("Diplomatic Relations", "diplomatic"),
        ("Technology Research", "tech")
    ])
    
    # Apply background bonuses
    if player_background == "military":
        $ player.knowledge += 5
    elif player_background == "economic":
        $ player.economics += 5
    elif player_background == "diplomatic":
        $ player.diplomacy += 5
    elif player_background == "tech":
        $ player.research_points += 5

    show professor normal
    
    professor "Welcome, [player_name]. You're joining us at a critical time."
    
    professor "The world is facing multiple crises, and Indonesia's role has never been more important."
    
    call tutorial_sequence
    
    jump main_hub

# Tutorial sequence
label tutorial_sequence:
    professor "Let me show you how things work around here."
    
    call explain_stats
    call explain_missions
    call explain_research
    call explain_travel
    
    return

# Tutorial explanation labels
label explain_stats:
    professor "Your performance is measured across multiple areas:"
    professor "Knowledge affects your understanding of global situations."
    professor "Diplomacy influences your ability to negotiate and build relationships."
    professor "Economics determines your financial and trade decisions."
    professor "Energy limits how many actions you can take per day."
    return

label explain_missions:
    professor "Missions are your primary objectives."
    professor "Complete them to gain experience and resources."
    professor "Some missions have time limits, so manage your time wisely."
    professor "You can track active missions in your mission log."
    return

label explain_research:
    professor "Research is crucial for understanding global dynamics."
    professor "Use the Research Center to study various topics."
    professor "Research points can be spent to gain new insights."
    professor "Higher knowledge leads to better decision-making."
    return

label explain_travel:
    professor "Field experience is valuable."
    professor "Visit different locations to gather information."
    professor "Travel costs energy but provides unique opportunities."
    professor "Some locations only become available as you progress."
    return

# Main gameplay labels
label main_hub:
    scene institute
    
    menu hub_menu:
        "Where would you like to go?"
        
        "Research Center" if player.energy >= 10:
            $ player.energy -= 10
            jump research_center
            
        "Diplomatic Office" if player.energy >= 10:
            $ player.energy -= 10
            jump diplomatic_office
            
        "Economic Analysis Wing" if player.energy >= 10:
            $ player.energy -= 10
            jump economic_wing
            
        "Travel to Field Location" if player.energy >= 20:
            $ player.energy -= 20
            jump travel_menu
            
        "Rest and Recover Energy":
            call rest_sequence
            
        "Save Game":
            call screen save

# Location labels
label research_center:
    scene lab
    
    menu research_menu:
        "What would you like to research?"
        
        "Maritime Security" if player.research_points >= 5:
            $ player.research_points -= 5
            call maritime_research
            
        "Economic Trends" if player.research_points >= 5:
            $ player.research_points -= 5
            call economic_research
            
        "Regional Conflicts" if player.research_points >= 5:
            $ player.research_points -= 5
            call conflict_research
            
        "Back to Hub":
            jump main_hub

label diplomatic_office:
    scene office
    "Welcome to the Diplomatic Office"
    menu:
        "Meet with Ambassador Chen" if player.energy >= 15:
            $ player.energy -= 15
            call diplomat_meeting
        "Review International Relations" if player.energy >= 10:
            $ player.energy -= 10
            call review_relations
        "Back to Hub":
            jump main_hub
    return

label economic_wing:
    scene office
    "Welcome to the Economic Analysis Wing"
    menu:
        "Analyze Trade Data" if player.energy >= 15:
            $ player.energy -= 15
            call trade_analysis
        "Study Market Trends" if player.energy >= 10:
            $ player.energy -= 10
            call market_study
        "Back to Hub":
            jump main_hub
    return

# Travel system
label travel_menu:
    menu:
        "Where would you like to travel?"
        
        "Natuna Islands" if "natuna" not in player.visited_places:
            $ player.visited_places.add("natuna")
            jump natuna_mission
            
        "Malacca Strait" if "malacca" not in player.visited_places:
            $ player.visited_places.add("malacca")
            jump malacca_mission
            
        "Papua Development Zone" if "papua" not in player.visited_places:
            $ player.visited_places.add("papua")
            jump papua_mission
            
        "Return to Hub":
            jump main_hub

# Mission labels
label natuna_mission:
    scene natuna
    $ player.current_mission = "Investigate South China Sea Situation"
    
    menu natuna_actions:
        "How do you approach the situation?"
        
        "Conduct Maritime Patrol" if player.energy >= 30:
            $ player.energy -= 30
            call natuna_patrol
            
        "Meet Local Fishermen" if player.energy >= 20:
            $ player.energy -= 20
            call fishermen_dialogue
            
        "Analyze Satellite Data" if player.energy >= 25:
            $ player.energy -= 25
            call satellite_analysis
            
        "Return to Hub":
            jump main_hub

# Additional gameplay mechanics
label rest_sequence:
    "You take some time to rest..."
    $ player.energy = min(100, player.energy + 50)
    $ time_of_day = "Evening" if time_of_day == "Morning" else "Morning"
    if time_of_day == "Morning":
        $ day_counter += 1
    "Energy restored to [player.energy]%"
    return

label diplomat_meeting:
    show diplomat normal
    diplomat "Welcome to my office."
    $ player.diplomacy += 2
    return

label trade_analysis:
    "You analyze recent trade data..."
    $ player.economics += 2
    return

label market_study:
    "You study market trends..."
    $ player.economics += 1
    return

label review_relations:
    "You review international relations..."
    $ player.diplomacy += 1
    return

# Research outcomes
label maritime_research:
    "You conduct research on maritime security..."
    $ player.knowledge += 3
    return

label economic_research:
    "You study economic trends..."
    $ player.economics += 3
    return

label conflict_research:
    "You analyze regional conflicts..."
    $ player.knowledge += 3
    return

# Field mission components
label natuna_patrol:
    "You patrol the Natuna waters..."
    $ player.knowledge += 3
    return

label fishermen_dialogue:
    "You meet with local fishermen..."
    $ player.diplomacy += 2
    return

label satellite_analysis:
    "You analyze satellite data..."
    $ player.knowledge += 2
    return

# Mission management
label malacca_mission:
    scene malacca
    "You arrive at the Malacca Strait..."
    menu:
        "Investigate shipping routes":
            $ player.knowledge += 2
        "Return to Hub":
            jump main_hub
    return

label papua_mission:
    scene papua
    "You arrive in Papua..."
    menu:
        "Study development projects":
            $ player.economics += 2
        "Return to Hub":
            jump main_hub
    return

# End game
label game_ending:
    scene classroom
    
    professor "Congratulations on completing your tenure, [player_name]."
    
    if player.knowledge > 30 and player.diplomacy > 30 and player.economics > 30:
        professor "You've shown exceptional understanding of global affairs."
        "Achievement Unlocked: Master Strategist"
        $ persistent.achievements.add("master_strategist")
    else:
        professor "You've made good progress in understanding global dynamics."
    
    "Final Stats:"
    "Knowledge: [player.knowledge]"
    "Diplomacy: [player.diplomacy]"
    "Economics: [player.economics]"
    "Missions Completed: [len(player.completed_missions)]"
    
    return