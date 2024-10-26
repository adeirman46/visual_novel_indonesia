# Define images 
image classroom = im.Scale("images/backgrounds/classroom.jpg", 1920, 1080)
image office = im.Scale("images/backgrounds/office.jpg", 1920, 1080)
image conference = im.Scale("images/backgrounds/conference.jpg", 1920, 1080)
image embassy = im.Scale("images/backgrounds/embassy.jpg", 1920, 1080)
image park = im.Scale("images/backgrounds/park.jpg", 1920, 1080)
image beach = im.Scale("images/backgrounds/beach.jpg", 1920, 1080)
image bedroom = im.Scale("images/backgrounds/bedroom.jpg", 1920, 1080)
image old_city = im.Scale("images/backgrounds/old_city.jpg", 1920, 1080)
image monas = im.Scale("images/backgrounds/monas.jpg", 1920, 1080)

# Character images
image professor normal = im.Scale("images/characters/professor.png", 600, 800)
image diplomat normal = im.Scale("images/characters/diplomat.png", 600, 800)
image economist normal = im.Scale("images/characters/economist.png", 600, 800)
image activist normal = im.Scale("images/characters/activist.png", 600, 800)
image general normal = im.Scale("images/characters/general.png", 600, 800)

# Character class and stats
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

# Define characters
define professor = Character("Dr. Wijaya", color="#b8b665", image="professor")
define diplomat = Character("Ambassador Chen", color="#4a90e2", image="diplomat")
define economist = Character("Dr. Suharto", color="#2ecc71", image="economist")
define activist = Character("Maya Kusuma", color="#e74c3c", image="activist")
define general = Character("General Sudirman", color="#95a5a6", image="general")
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
    
    show professor normal
    professor "Welcome to the Center for Strategic Studies."
    
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

# Strategy Room
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

# South China Sea Crisis
label south_china_sea_crisis:
    show professor normal at left
    show general normal at right
    
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

# Diplomatic Approach
label diplomatic_approach:
    $ player.influence += 3
    show diplomat normal
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

# Economic Diplomacy
label economic_diplomacy:
    show economist normal
    economist "Economic ties can be a powerful tool for peace."
    
    menu:
        "Which economic aspect to emphasize?"
        
        "Trade partnerships":
            $ player.knowledge += 2
            economist "Strengthening trade ties creates mutual dependencies."
            
        "Investment cooperation":
            $ player.influence += 2
            economist "Joint investments build long-term relationships."
            
        "Resource sharing":
            $ player.reputation += 2
            economist "Cooperative resource management benefits all parties."
    
    return

# Security Diplomacy
label security_diplomacy:
    show general normal
    show diplomat normal at right
    
    general "Security cooperation must be balanced with sovereignty."
    
    menu:
        "What security measures to propose?"
        
        "Joint maritime patrols":
            $ player.knowledge += 2
            general "Coordinated patrols show unity and strength."
            
        "Information sharing":
            $ player.influence += 2
            diplomat "Intelligence cooperation builds trust."
            
        "Crisis response protocols":
            $ player.reputation += 2
            general "Clear protocols prevent misunderstandings."
    
    return

# Cultural Diplomacy
label cultural_diplomacy:
    show diplomat normal
    diplomat "Cultural understanding creates lasting bonds."
    
    menu:
        "How to promote cultural exchange?"
        
        "Educational programs":
            $ player.knowledge += 2
            diplomat "Student exchanges build future relationships."
            
        "Cultural festivals":
            $ player.influence += 2
            diplomat "Celebrating diversity brings people together."
            
        "Media cooperation":
            $ player.reputation += 2
            diplomat "Shared stories create mutual understanding."
    
    return

# Military Approach
label military_approach:
    $ player.influence += 2
    show general normal
    general "A strong defense prevents conflict."
    
    menu:
        "What military strategy to adopt?"
        
        "Modernize equipment":
            $ player.knowledge += 2
            general "Modern capabilities deter aggression."
            
        "Enhance training":
            $ player.influence += 2
            general "Well-trained forces are more effective."
            
        "Improve coordination":
            $ player.reputation += 2
            general "Better coordination multiplies our strength."
    
    return

# Economic Crisis
label economic_crisis:
    show economist normal at left
    show activist normal at right
    
    economist "Global recession is hitting our exports hard."
    activist "The common people are struggling."
    
    menu:
        "How to address the economic crisis?"
        
        "Protect domestic industries":
            call domestic_protection
            
        "Seek foreign investment":
            call foreign_investment
            
        "Support small businesses":
            call small_business_support
    
    return

# Domestic Protection
label domestic_protection:
    show economist normal
    economist "Protecting our industries has both benefits and risks."
    
    menu:
        "Which protection measures to implement?"
        
        "Import regulations":
            $ player.knowledge += 2
            economist "Careful regulation can help local industries grow."
            
        "Industry subsidies":
            $ player.influence += 2
            economist "Strategic support can strengthen key sectors."
            
        "Skills development":
            $ player.reputation += 2
            economist "Investing in our workforce builds long-term strength."
    
    return

# Foreign Investment
label foreign_investment:
    show economist normal
    show diplomat normal at right
    
    economist "Foreign investment can boost our economy."
    
    menu:
        "Which investment strategy to pursue?"
        
        "Infrastructure projects":
            $ player.knowledge += 2
            economist "Infrastructure development attracts more investment."
            
        "Technology sectors":
            $ player.influence += 2
            economist "Tech investment builds future capabilities."
            
        "Green industries":
            $ player.reputation += 2
            economist "Sustainable industries secure our future."
    
    return

# Small Business Support
label small_business_support:
    show economist normal
    show activist normal at right
    
    activist "Small businesses are the backbone of our economy."
    
    menu:
        "How to support small businesses?"
        
        "Financial assistance":
            $ player.knowledge += 2
            economist "Access to capital is crucial for growth."
            
        "Technical training":
            $ player.influence += 2
            economist "Skills development enables success."
            
        "Market access":
            $ player.reputation += 2
            economist "Connecting to markets creates opportunities."
    
    return

# Climate Crisis
label climate_crisis:
    show activist normal at left
    show economist normal at right
    
    activist "Climate change threatens our islands."
    economist "The economic impact could be severe."
    
    menu:
        "How to address climate change?"
        
        "Green infrastructure":
            call green_infrastructure
            
        "Emission reduction":
            call emission_reduction
            
        "Community adaptation":
            call community_adaptation
    
    return

# Green Infrastructure
label green_infrastructure:
    show economist normal
    economist "Sustainable infrastructure is an investment in our future."
    
    menu:
        "Which infrastructure to prioritize?"
        
        "Renewable energy":
            $ player.knowledge += 2
            economist "Clean energy powers sustainable growth."
            
        "Public transportation":
            $ player.influence += 2
            economist "Better transit reduces emissions and congestion."
            
        "Green buildings":
            $ player.reputation += 2
            economist "Efficient buildings save resources."
    
    return

# Emission Reduction
label emission_reduction:
    show economist normal
    show activist normal at right
    
    economist "Reducing emissions requires broad changes."
    
    menu:
        "Which emission reduction strategy?"
        
        "Industrial regulations":
            $ player.knowledge += 2
            economist "Clear standards guide industry transition."
            
        "Clean technology":
            $ player.influence += 2
            economist "Technology enables cleaner production."
            
        "Behavior change":
            $ player.reputation += 2
            activist "Individual actions add up to big changes."
    
    return

# Community Adaptation
label community_adaptation:
    show activist normal
    activist "Communities need help adapting to climate change."
    
    menu:
        "How to support community adaptation?"
        
        "Early warning systems":
            $ player.knowledge += 2
            activist "Better warnings save lives."
            
        "Resilient agriculture":
            $ player.influence += 2
            activist "Food security is crucial for stability."
            
        "Coastal protection":
            $ player.reputation += 2
            activist "Protecting coasts preserves communities."
    
    return

# Tech Sovereignty
label tech_sovereignty_crisis:
    show economist normal at left
    show general normal at right
    
    economist "Our digital infrastructure needs independence."
    general "Tech sovereignty is national security."
    
    menu:
        "How to achieve tech sovereignty?"
        
        "Develop local technology":
            call local_tech_development
            
        "International partnerships":
            call tech_partnerships
            
        "Cybersecurity focus":
            call cyber_security
    
    return

# Embassy District Events
label embassy_district:
    scene embassy
    menu:
        "Who would you like to meet?"
        
        "Ambassador Chen":
            call chen_meeting
            
        "Dr. Suharto":
            call suharto_meeting
            
        "Maya Kusuma":
            call maya_meeting
            
        "Return to Office":
            jump main_hub
    
    return

# Character Meetings
label chen_meeting:
    show diplomat normal
    diplomat "Regional dynamics are shifting rapidly."
    
    menu:
        "What topic to discuss?"
        
        "Maritime cooperation":
            $ player.knowledge += 2
            diplomat "The seas connect our nations."
            
        "Economic partnership":
            $ player.influence += 2
            diplomat "Trade builds bridges."
            
        "Cultural exchange":
            $ player.reputation += 2
            diplomat "Understanding grows from cultural ties."
    
    return

# Recreational Activities
label taman_mini:
    scene park
    n "Indonesia's diversity is on display."
    
    menu:
        "What catches your attention?"
        
        "Cultural exhibitions":
            $ player.knowledge += 2
            n "Our traditions tell our story."
            
        "Economic activities":
            $ player.influence += 2
            n "Commerce connects communities."
            
        "Educational programs":
            $ player.reputation += 2
            n "Learning preserves our heritage."
    
    return

label ancol_beach:
    scene beach
    n "The sea brings perspective."
    
    menu:
        "What do you observe?"
        
        "Maritime activity":
            $ player.knowledge += 2
            n "Ships carry our prosperity."
            
        "Coastal development":
            $ player.influence += 2
            n "Development must respect nature."
            
        "Environmental changes":
            $ player.reputation += 2
            n "The environment signals our future."
    
    return

# Rest and Reflection
label rest_sequence:
    scene bedroom
    "Time to rest and reflect."
    $ player.energy = min(100, player.energy + 40)
    $ day += 1
    
    menu:
        "How to use this time?"
        
        "Study reports":
            $ player.knowledge += 2
            "Knowledge builds understanding."
            
        "Plan strategies":
            $ player.influence += 2
            "Good planning enables success."
            
        "Meditate":
            $ player.reputation += 2
            "Clear minds make better choices."
    
    jump main_hub

# Game Ending
label game_ending:
    scene office
    show professor normal
    
    professor "Your decisions have shaped Indonesia's future, [player_name]."
    
    if player.influence > 35 and player.knowledge > 30:
        call best_ending
    elif player.influence > 30:
        call good_ending
    else:
        call standard_ending
    
    return

# Ending Variants
label best_ending:
    professor "Your balanced leadership has positioned Indonesia as a regional leader."
    
    "Achievements:"
    "- Enhanced regional stability"
    "- Improved economic resilience"
    "- Strengthened social cohesion"
    
    "The End - Master Strategist"
    return

label good_ending:
    professor "Your strong influence has helped guide Indonesia through challenging times."
    
    "Achievements:"
    "- Built strong alliances"
    "- Protected national interests"
    "- Maintained stability"
    
    "The End - Skilled Leader"
    return

label standard_ending:
    professor "You've contributed to Indonesia's development in meaningful ways."
    
    "Achievements:"
    "- Gained valuable experience"
    "- Developed important insights"
    "- Laid groundwork for future progress"
    
    "The End - Promising Analyst"
    return

# Additional Crisis Management Labels
label local_tech_development:
    show economist normal
    economist "Building our own technology base is crucial for independence."
    
    menu:
        "Which tech sector to prioritize?"
        
        "Digital infrastructure":
            $ player.knowledge += 2
            economist "Strong infrastructure enables innovation."
            
        "Software development":
            $ player.influence += 2
            economist "Local software reduces foreign dependence."
            
        "Hardware manufacturing":
            $ player.reputation += 2
            economist "Manufacturing capability ensures supply chain security."
    
    return

label tech_partnerships:
    show diplomat normal
    diplomat "Strategic partnerships can accelerate our development."
    
    menu:
        "What kind of partnerships?"
        
        "Research collaboration":
            $ player.knowledge += 2
            diplomat "Joint research builds mutual capacity."
            
        "Technology transfer":
            $ player.influence += 2
            diplomat "Knowledge sharing accelerates progress."
            
        "Joint ventures":
            $ player.reputation += 2
            diplomat "Combined resources achieve more."
    
    return

label cyber_security:
    show general normal
    general "Digital security is national security."
    
    menu:
        "Which security aspect needs focus?"
        
        "Infrastructure protection":
            $ player.knowledge += 2
            general "Critical systems must be secured."
            
        "Data sovereignty":
            $ player.influence += 2
            general "Control over data is strategic power."
            
        "Cyber defense":
            $ player.reputation += 2
            general "Active defense protects our interests."
    
    return

# Additional Character Meeting Labels
label suharto_meeting:
    show economist normal
    economist "Economic trends shape national destiny."
    
    menu:
        "Which economic issue to discuss?"
        
        "Industrial policy":
            $ player.knowledge += 2
            economist "Strategic industries need careful nurturing."
            
        "Trade relations":
            $ player.influence += 2
            economist "Trade partnerships build prosperity."
            
        "Development planning":
            $ player.reputation += 2
            economist "Long-term planning ensures sustainable growth."
    
    return

label maya_meeting:
    show activist normal
    activist "Social justice must guide development."
    
    menu:
        "What social issue to address?"
        
        "Income inequality":
            $ player.knowledge += 2
            activist "Equality creates stable societies."
            
        "Environmental justice":
            $ player.influence += 2
            activist "Environmental protection serves everyone."
            
        "Education access":
            $ player.reputation += 2
            activist "Education transforms lives."
    
    return

# Environmental Impact Labels
label environmental_insight:
    show activist normal
    activist "Environmental changes affect everyone."
    
    menu:
        "Which environmental issue needs attention?"
        
        "Air quality":
            $ player.knowledge += 2
            activist "Clean air is a basic right."
            
        "Water resources":
            $ player.influence += 2
            activist "Water security is life security."
            
        "Forest preservation":
            $ player.reputation += 2
            activist "Forests are our natural heritage."
    
    return

label tourism_insight:
    show economist normal
    economist "Tourism can drive sustainable development."
    
    menu:
        "How to develop tourism?"
        
        "Cultural tourism":
            $ player.knowledge += 2
            economist "Cultural experiences attract visitors."
            
        "Eco-tourism":
            $ player.influence += 2
            economist "Nature-based tourism preserves environments."
            
        "Community tourism":
            $ player.reputation += 2
            economist "Local communities should benefit directly."
    
    return

# Maritime Focus Labels
label maritime_trade_insight:
    show economist normal
    economist "Maritime trade is our historical strength."
    
    menu:
        "Which maritime aspect to develop?"
        
        "Port infrastructure":
            $ player.knowledge += 2
            economist "Modern ports enable trade growth."
            
        "Shipping capacity":
            $ player.influence += 2
            economist "Our own ships secure our trade routes."
            
        "Maritime services":
            $ player.reputation += 2
            economist "Services add value to maritime trade."
    
    return

label fishing_industry_insight:
    show activist normal
    activist "Sustainable fishing protects livelihoods."
    
    menu:
        "How to support fishing communities?"
        
        "Modern equipment":
            $ player.knowledge += 2
            activist "Better tools improve efficiency."
            
        "Sustainable practices":
            $ player.influence += 2
            activist "Sustainability ensures long-term survival."
            
        "Community support":
            $ player.reputation += 2
            activist "Strong communities maintain traditions."
    
    return

# Strategic Development Labels
label economic_development:
    show economist normal
    economist "Economic development must be inclusive and sustainable."
    
    menu:
        "Which development strategy to pursue?"
        
        "Industrial modernization":
            $ player.knowledge += 2
            economist "Modern industry creates better jobs."
            
        "Digital economy":
            $ player.influence += 2
            economist "Digital transformation opens new opportunities."
            
        "Green growth":
            $ player.reputation += 2
            economist "Sustainable growth secures our future."
    
    return

label social_development:
    show activist normal
    activist "Social development is the foundation of progress."
    
    menu:
        "Which social aspect needs focus?"
        
        "Healthcare access":
            $ player.knowledge += 2
            activist "Health is fundamental to development."
            
        "Education quality":
            $ player.influence += 2
            activist "Quality education transforms society."
            
        "Social protection":
            $ player.reputation += 2
            activist "Safety nets protect vulnerable communities."
    
    return

# Infrastructure Development Labels
label infrastructure_planning:
    show economist normal
    economist "Infrastructure shapes development possibilities."
    
    menu:
        "Which infrastructure to prioritize?"
        
        "Transportation networks":
            $ player.knowledge += 2
            economist "Connectivity drives growth."
            
        "Digital infrastructure":
            $ player.influence += 2
            economist "Digital networks enable modern economy."
            
        "Urban development":
            $ player.reputation += 2
            economist "Smart cities improve life quality."
    
    return

# The game continues with branching pathways and consequences...

