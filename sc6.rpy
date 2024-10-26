# Define characters with custom attributes and deeper personalities
init python:
    class GameCharacter:
        def __init__(self, name, title, trust=0, expertise="", viewpoint=""):
            self.name = name
            self.title = title
            self.trust = trust
            self.expertise = expertise
            self.viewpoint = viewpoint

    class PlayerStats:
        def __init__(self):
            self.knowledge = 0
            self.influence = 0
            self.reputation = 0
            self.energy = 100
            self.relationships = {}
            self.visited_places = set()
            self.choices_made = []
            self.current_crisis = None

# Game characters with distinct viewpoints and personalities
define professor = Character("Dr. Wijaya", color="#b8b665")
define diplomat = Character("Ambassador Chen", color="#4a90e2")
define economist = Character("Dr. Suharto", color="#2ecc71")
define activist = Character("Maya Kusuma", color="#e74c3c")
define general = Character("General Sudirman", color="#95a5a6")
define n = Character("Narrator", color="#ffffff")

# Initialize game variables
default player = PlayerStats()
default current_location = "Jakarta"
default day = 1
default active_crisis = None

# Custom screens
screen stats_display():
    frame:
        xalign 0.99 yalign 0.02
        vbox:
            text "Day: [day]" size 20
            text "Energy: [player.energy]%" size 20
            text "Knowledge: [player.knowledge]" size 20
            text "Influence: [player.influence]" size 20
            text "Reputation: [player.reputation]" size 20

# Game start
label start:
    $ player = PlayerStats()
    
    scene classroom
    show screen stats_display
    
    n "2024. The world is facing multiple crises, and Indonesia stands at a crossroads."
    
    show professor
    professor "Welcome to the Center for Strategic Studies."
    
    # Character creation
    $ player_name = renpy.input("What's your name?")
    
    professor "These are challenging times, [player_name]. We need clear thinking and strong leadership."
    
    professor "The South China Sea tensions are escalating, our economy faces pressures from global recession, and climate change threatens our archipelago."
    
    professor "Your analysis and decisions will help shape Indonesia's response to these challenges."

    jump main_hub

# Main gameplay hub
label main_hub:
    scene office
    menu location_choice:
        "Where would you like to go?"
        
        "Strategy Room - Discuss Current Crisis" if player.energy >= 20:
            $ player.energy -= 20
            jump strategy_room
            
        "Embassy District - Meet Key Figures" if player.energy >= 15:
            $ player.energy -= 15
            jump embassy_district
            
        "Taman Mini Indonesia - Take a Walk" if player.energy >= 10:
            $ player.energy -= 10
            jump taman_mini
            
        "Ancol Beach - Clear Your Mind" if player.energy >= 10:
            $ player.energy -= 10
            jump ancol_beach
            
        "Rest and Reflect":
            call rest_sequence
            
        "Save Progress":
            call screen save

# Location specific events
label strategy_room:
    scene conference
    
    if not active_crisis:
        $ active_crisis = renpy.random.choice([
            "south_china_sea",
            "economic_pressure",
            "climate_crisis",
            "tech_sovereignty"
        ])
    
    if active_crisis == "south_china_sea":
        call south_china_sea_crisis
    elif active_crisis == "economic_pressure":
        call economic_crisis
    elif active_crisis == "climate_crisis":
        call climate_crisis
    else:
        call tech_sovereignty_crisis
    
    return

# Crisis scenarios
label south_china_sea_crisis:
    show professor at left
    show general at right
    
    professor "Recent satellite imagery shows increased military presence in disputed waters."
    
    general "We need to show strength while avoiding direct confrontation."
    
    menu:
        "How do you assess the situation?"
        
        "Advocate for multilateral ASEAN response":
            call diplomatic_approach
            
        "Suggest increasing maritime patrols":
            call military_approach
            
        "Propose economic leverage through trade relations":
            call economic_approach
            
        "Request more time to analyze the situation":
            call analytical_approach
    
    return

label economic_crisis:
    show economist at left
    show activist at right
    
    economist "Global recession is hitting our exports hard, and inflation is rising."
    
    activist "The common people are struggling with basic necessities."
    
    menu:
        "How should Indonesia respond?"
        
        "Focus on protecting domestic industries":
            $ player.influence += 2
            economist "A reasonable approach, but we must be careful about protectionism."
            
        "Seek international investment and partnerships":
            $ player.knowledge += 2
            economist "This could bring needed capital, but we must maintain sovereignty."
            
        "Implement social support programs":
            $ player.reputation += 2
            activist "Finally, someone thinking about the people!"
            
        "Develop new export markets":
            $ player.influence += 2
            economist "Diversification is key to economic resilience."
    
    return

# Character interactions
label embassy_district:
    scene embassy
    
    menu:
        "Who would you like to meet?"
        
        "Ambassador Chen - Discuss Regional Politics":
            call chen_meeting
            
        "Dr. Suharto - Economic Analysis":
            call suharto_meeting
            
        "Maya Kusuma - Social Impact":
            call maya_meeting
            
        "Return to Office":
            jump main_hub
    
    return

# Detailed character meetings
label chen_meeting:
    show diplomat
    
    diplomat "Ah, [player_name]. Your timing is interesting."
    
    menu:
        "What aspect of regional politics interests you most?"
        
        "Maritime security cooperation":
            diplomat "Indeed. The seas connect us all, but they can also divide us."
            call maritime_discussion
            
        "Trade route development":
            diplomat "The Belt and Road Initiative offers opportunities... and challenges."
            call trade_discussion
            
        "Cultural exchange programs":
            diplomat "Soft power should never be underestimated."
            call cultural_discussion
    
    return

# Recreational locations with meaningful interactions
label taman_mini:
    scene park
    
    n "The miniature park showcases Indonesia's diversity. As you walk, you notice different groups of visitors..."
    
    menu:
        "What catches your attention?"
        
        "Local families discussing economic hardship":
            call economic_insight
            
        "Students debating environmental policies":
            call environmental_insight
            
        "Tourism operators talking about international visitors":
            call tourism_insight
    
    return

label ancol_beach:
    scene beach
    
    n "The sunset at Ancol provides a moment for reflection. You notice..."
    
    menu:
        "Where do you focus your thoughts?"
        
        "Fish markets and local economy":
            call fishing_industry_insight
            
        "Port activities and trade":
            call maritime_trade_insight
            
        "Coastal development and climate":
            call climate_impact_insight
    
    return

# Insight labels with meaningful dialogue
label economic_insight:
    "You overhear discussions about rising prices and job security."
    
    menu:
        "How do you process this information?"
        
        "Consider policy implications":
            $ player.knowledge += 2
            "This ground-level perspective adds depth to your economic understanding."
            
        "Make notes for future reference":
            $ player.influence += 1
            "These real stories could influence future policy discussions."
    
    return

# Deep discussion topics
label maritime_discussion:
    diplomat "The South China Sea situation requires delicate balance."
    
    menu:
        "Your perspective on maritime security?"
        
        "Focus on international law":
            $ player.knowledge += 2
            diplomat "UNCLOS provides a framework, but implementation is complex."
            
        "Emphasize practical cooperation":
            $ player.influence += 2
            diplomat "Joint patrols could build trust, if managed carefully."
            
        "Consider economic implications":
            $ player.reputation += 2
            diplomat "Maritime security and economic interests are deeply connected."
    
    return

# Rest and reflection
label rest_sequence:
    scene bedroom
    
    "You take time to rest and process recent events..."
    
    $ player.energy = min(100, player.energy + 40)
    $ day += 1
    
    menu:
        "How do you spend your reflection time?"
        
        "Review international news":
            $ player.knowledge += 1
            "You gain new perspectives on global events."
            
        "Write in your journal":
            $ player.influence += 1
            "Organizing your thoughts helps clarify your position."
            
        "Meditate on decisions":
            $ player.reputation += 1
            "Clear thinking leads to better choices."
    
    return

# Crisis resolution paths
label diplomatic_approach:
    $ player.influence += 3
    diplomat "ASEAN unity could provide diplomatic leverage."
    
    menu:
        "How to build consensus?"
        
        "Focus on shared economic interests":
            call economic_diplomacy
            
        "Emphasize security cooperation":
            call security_diplomacy
            
        "Promote cultural understanding":
            call cultural_diplomacy
    
    return

# Additional location events
label climate_impact_insight:
    n "Rising sea levels threaten coastal communities."
    
    menu:
        "What aspect deserves focus?"
        
        "Infrastructure adaptation":
            call infrastructure_planning
            
        "Community resilience":
            call community_support
            
        "Economic implications":
            call economic_adaptation
    
    return

# The game continues with many more labels and scenes...
# [Additional 500+ lines of game content would follow with more
# crisis scenarios, character interactions, and decision points]

label game_ending:
    scene office
    show professor
    
    professor "Your time with us has shaped important decisions, [player_name]."
    
    if player.influence > 30 and player.knowledge > 25:
        professor "Your balanced approach to challenges has served Indonesia well."
    elif player.influence > 30:
        professor "You've shown strong leadership in difficult times."
    else:
        professor "You've contributed to our understanding of complex issues."
    
    "The End"
    
    return

# [Previous code remains the same up to the crisis scenarios...]

# Additional Crisis Scenarios
label tech_sovereignty_crisis:
    show economist at left
    show activist at right
    
    economist "Our digital infrastructure relies heavily on foreign technology."
    activist "Data sovereignty and security are major concerns."
    
    menu:
        "How should we approach technological independence?"
        
        "Invest in domestic tech development":
            $ player.knowledge += 2
            economist "This requires significant investment but could secure our future."
            call domestic_tech_development
            
        "Partner with multiple international providers":
            $ player.influence += 2
            economist "Diversification could reduce dependency risks."
            call international_tech_partnership
            
        "Focus on cybersecurity first":
            $ player.reputation += 2
            general "Security should be our priority."
            call cybersecurity_focus
    
    return

label domestic_tech_development:
    menu:
        "Where should we focus our tech development?"
        
        "Digital infrastructure":
            call digital_infrastructure
            
        "Educational technology":
            call education_tech
            
        "Financial technology":
            call fintech_development
    
    return

label digital_infrastructure:
    economist "Building our own digital backbone is crucial."
    
    menu:
        "Which aspect needs immediate attention?"
        
        "5G Network Development":
            $ player.knowledge += 2
            economist "This could revolutionize our industrial capacity."
            
        "Data Center Construction":
            $ player.influence += 2
            economist "Local data centers would enhance our digital sovereignty."
            
        "Submarine Cable Projects":
            $ player.reputation += 2
            economist "Connectivity is key to our archipelagic nation."
    
    return

# Expanded Character Interactions
label suharto_meeting:
    show economist
    
    economist "The global economic landscape is shifting rapidly."
    
    menu:
        "What economic aspect interests you?"
        
        "Green economy transition":
            call green_economy_discussion
            
        "Digital economy growth":
            call digital_economy_discussion
            
        "Regional economic integration":
            call regional_integration_discussion
    
    return

label green_economy_discussion:
    economist "Indonesia's vast natural resources present unique opportunities."
    
    menu:
        "What's your view on green transition?"
        
        "Prioritize renewable energy":
            $ player.knowledge += 2
            economist "Solar and geothermal potential is immense."
            call renewable_energy_focus
            
        "Sustainable agriculture":
            $ player.influence += 2
            economist "Food security and sustainability go hand in hand."
            call agricultural_development
            
        "Eco-tourism development":
            $ player.reputation += 2
            economist "Our biodiversity could drive sustainable tourism."
            call ecotourism_strategy
    
    return

# New Location Events
label kota_tua:
    scene old_city
    
    n "The old city of Jakarta holds many stories..."
    
    menu:
        "Where do you focus your attention?"
        
        "Historical architecture":
            call heritage_preservation
            
        "Local businesses":
            call small_business_insight
            
        "Cultural activities":
            call cultural_preservation
    
    return

label monas_visit:
    scene monas
    
    n "The National Monument stands as a symbol of independence..."
    
    menu:
        "What aspect draws your attention?"
        
        "Tourism potential":
            call tourism_development
            
        "Historical significance":
            call historical_reflection
            
        "Urban development":
            call urban_planning
    
    return

# Expanded Crisis Management
label regional_security_crisis:
    show general at left
    show diplomat at right
    
    general "Regional tensions are escalating."
    diplomat "We need a balanced approach."
    
    menu:
        "How do we maintain regional stability?"
        
        "Strengthen defense capabilities":
            $ player.influence += 2
            general "A strong defense prevents conflict."
            call defense_modernization
            
        "Enhance diplomatic ties":
            $ player.reputation += 2
            diplomat "Diplomacy is our first line of defense."
            call diplomatic_initiatives
            
        "Develop economic cooperation":
            $ player.knowledge += 2
            economist "Economic interdependence promotes peace."
            call economic_cooperation
    
    return

label defense_modernization:
    general "Our military needs modernization to face current challenges."
    
    menu:
        "Where should we focus our defense modernization?"
        
        "Maritime capability":
            call maritime_defense
            
        "Cyber warfare":
            call cyber_defense
            
        "Air defense systems":
            call air_defense
    
    return

# Economic Development Scenarios
label economic_cooperation:
    economist "Regional economic cooperation could be our path forward."
    
    menu:
        "Which approach should we prioritize?"
        
        "ASEAN integration":
            call asean_integration
            
        "Indo-Pacific partnerships":
            call indo_pacific_strategy
            
        "Global trade networks":
            call global_trade
    
    return

label asean_integration:
    diplomat "ASEAN's potential remains largely untapped."
    
    menu:
        "How can we deepen ASEAN integration?"
        
        "Standardize regulations":
            $ player.knowledge += 2
            economist "Regulatory harmony could boost regional trade."
            
        "Develop infrastructure":
            $ player.influence += 2
            economist "Connectivity is crucial for integration."
            
        "Promote cultural exchange":
            $ player.reputation += 2
            activist "Understanding builds stronger bonds."
    
    return

# Environmental Challenges
label climate_crisis:
    show activist at left
    show economist at right
    
    activist "Climate change threatens our archipelago."
    economist "The economic costs could be devastating."
    
    menu:
        "How should we address climate challenges?"
        
        "Green infrastructure development":
            call green_infrastructure
            
        "Community adaptation programs":
            call community_adaptation
            
        "International climate cooperation":
            call climate_cooperation
    
    return

label green_infrastructure:
    economist "Sustainable infrastructure requires significant investment."
    
    menu:
        "Which project should take priority?"
        
        "Coastal protection":
            $ player.influence += 2
            "Sea walls and mangrove restoration could protect coastal communities."
            
        "Green energy systems":
            $ player.knowledge += 2
            "Renewable energy would reduce our carbon footprint."
            
        "Sustainable transportation":
            $ player.reputation += 2
            "Public transit development could transform our cities."
    
    return

# Social Development Focus
label community_adaptation:
    activist "Communities need support to adapt to changing conditions."
    
    menu:
        "How can we support community adaptation?"
        
        "Education programs":
            call education_initiative
            
        "Local business support":
            call business_support
            
        "Healthcare access":
            call healthcare_improvement
    
    return

# New Diplomatic Scenarios
label diplomatic_initiatives:
    diplomat "Strategic diplomacy can advance our interests."
    
    menu:
        "Which diplomatic initiative should we pursue?"
        
        "Regional leadership":
            call regional_leadership
            
        "Global partnerships":
            call global_partnerships
            
        "Cultural diplomacy":
            call cultural_diplomacy
    
    return

# Technology Development
label tech_development:
    show economist
    
    economist "Technology could transform our economy."
    
    menu:
        "Which tech sector should we prioritize?"
        
        "Digital infrastructure":
            call digital_development
            
        "Education technology":
            call education_tech
            
        "Financial innovation":
            call fintech_innovation
    
    return

# Additional Character Development
label maya_meeting:
    show activist
    
    activist "Social justice and development must go hand in hand."
    
    menu:
        "What social issue concerns you most?"
        
        "Income inequality":
            call inequality_discussion
            
        "Environmental justice":
            call environmental_justice
            
        "Education access":
            call education_access
    
    return

# Strategic Planning
label strategic_planning:
    show professor
    
    professor "Long-term planning is crucial for our nation's future."
    
    menu:
        "Which aspect needs most attention?"
        
        "Economic diversification":
            call economic_planning
            
        "Social development":
            call social_planning
            
        "Environmental protection":
            call environmental_planning
    
    return

# Maritime Focus
label maritime_strategy:
    show general
    
    general "Our maritime domain requires careful management."
    
    menu:
        "What should be our maritime priority?"
        
        "Port development":
            call port_development
            
        "Fisheries protection":
            call fisheries_management
            
        "Maritime security":
            call maritime_security
    
    return

# Concluding Scenarios
label game_conclusion:
    scene office
    show professor
    
    professor "Your decisions have shaped our nation's path."
    
    if player.influence > 35 and player.knowledge > 30:
        call best_ending
    elif player.influence > 30:
        call good_ending
    else:
        call standard_ending
    
    return

label best_ending:
    professor "Your balanced approach has positioned Indonesia as a regional leader."
    
    "Achievements:"
    "- Enhanced regional stability"
    "- Improved economic resilience"
    "- Strengthened social cohesion"
    
    "The End - Master Strategist"
    return

# End of extended script