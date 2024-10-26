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

label tutorial_sequence:
    professor "Let me show you how things work around here."
    
    call explain_stats
    call explain_missions
    call explain_research
    call explain_travel
    
    return

label explain_stats:
    professor "Your performance is measured across multiple areas:"
    professor "Knowledge affects your understanding of global situations."
    professor "Diplomacy influences your ability to negotiate and build relationships."
    professor "Economics determines your financial and trade decisions."
    professor "Energy limits how many actions you can take per day."
    return

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
            call save_game

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

label crisis_event:
    if len(active_crises) > 0:
        $ current_crisis = active_crises[0]
        call handle_crisis(current_crisis)
    else:
        call random_event
    return

label handle_crisis(crisis):
    if crisis == "South_China_Sea_Tension":
        call south_china_sea_crisis
    elif crisis == "Economic_Disruption":
        call economic_crisis
    elif crisis == "Regional_Conflict":
        call regional_conflict_crisis
    return

label south_china_sea_crisis:
    scene crisis_room
    
    $ success_chance = player.diplomacy * 0.4 + player.knowledge * 0.3 + player.influence * 0.3
    
    menu crisis_response:
        "How do you handle the situation?"
        
        "Diplomatic Negotiation" if player.diplomacy >= 20:
            if renpy.random.random() < success_chance:
                $ player.diplomacy += 5
                "Your diplomatic approach helps ease tensions."
            else:
                $ player.influence -= 2
                "The negotiations reach a stalemate."
            
        "Show of Force" if player.knowledge >= 15:
            if renpy.random.random() < success_chance:
                $ player.influence += 5
                "The display of strength achieves its purpose."
            else:
                $ player.diplomacy -= 3
                "The action increases regional tensions."
            
        "Economic Leverage" if player.economics >= 25:
            if renpy.random.random() < success_chance:
                $ player.economics += 5
                "Your economic strategy proves effective."
            else:
                $ player.money -= 500
                "The economic pressure backfires."
    
    return

# Research minigames
label maritime_research:
    scene lab
    $ correct_answers = 0
    
    "Answer these questions about maritime security:"
    
    menu q1:
        "What percentage of global trade passes through the Malacca Strait?"
        
        "About 25%":
            "Incorrect."
            
        "About 40%":
            $ correct_answers += 1
            "Correct!"
            
        "About 60%":
            "Incorrect."
    
    # More questions...
    
    if correct_answers >= 2:
        $ player.knowledge += 3
        $ player.research_points += 2
        "Research successful!"
    else:
        "More research needed."
    
    return

# Relationship building
label build_relationship(character):
    $ trust_gain = 0
    
    menu:
        "How do you approach the conversation?"
        
        "Professional Discussion":
            $ trust_gain = 1
            
        "Personal Connection":
            $ trust_gain = 2
            
        "Share Intel" if player.knowledge >= 10:
            $ trust_gain = 3
    
    $ player.relationships[character] = player.relationships.get(character, 0) + trust_gain
    
    return

# End of day sequence
label end_day:
    $ day_counter += 1
    $ player.energy = 100
    $ time_of_day = "Morning"
    
    if day_counter % 7 == 0:
        call weekly_report
    
    if renpy.random.random() < 0.3:
        call crisis_event
    
    jump main_hub

label weekly_report:
    scene office
    
    "Weekly Performance Report"
    "Knowledge: [player.knowledge]"
    "Diplomacy: [player.diplomacy]"
    "Economics: [player.economics]"
    "Total Research Points: [player.research_points]"
    
    if player.knowledge + player.diplomacy + player.economics > 50:
        "Excellent progress!"
        $ player.money += 500
    
    return

# Game ending
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