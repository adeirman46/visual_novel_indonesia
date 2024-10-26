# Define characters
define n = Character("Narrator", color="#ffffff")
define p = Character("Professor", color="#b8b665") 
define s = Character("Student", color="#800000")
define g = Character("Guide", color="#4a90e2")
define e = Character("Expert", color="#2ecc71")

# Regional guides
define g_sumatra = Character("Pak Rahman", color="#4a90e2")
define g_java = Character("Bu Kartini", color="#4a90e2")
define g_kali = Character("Pak Dayak", color="#4a90e2")
define g_sula = Character("Bu Minahasa", color="#4a90e2")
define g_papua = Character("Pak Papua", color="#4a90e2")

# Define images
image classroom = im.Scale("ikn.png", 1920, 1080)
image professor normal = im.Scale("putri.png", 1920/1.5, 1080/1.5)
image student normal = im.Scale("irman.png", 1920/1.5, 1080/1.5)

# Game variables
default knowledge_score = 0
default diplomatic_score = 0
default economic_score = 0
default visited_locations = []

label start:
    # Player name input
    $ player_name = renpy.input("What is your name, student?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Student"

    scene classroom
    show professor normal

    p "Welcome to the Advanced Geopolitics and Strategic Studies program, [player_name]."
    
    p "In these challenging times, understanding global dynamics is more crucial than ever."
    
    menu start_choice:
        p "What interests you most about current global affairs?"
        
        "Maritime security and South China Sea":
            $ diplomatic_score += 1
            jump maritime_chapter
            
        "Global economy and technology":
            $ economic_score += 1
            jump economy_chapter
            
        "Regional conflicts and their impact":
            $ knowledge_score += 1
            jump conflict_chapter

label maritime_chapter:
    scene classroom
    show professor normal
    
    p "Let's start with maritime security in the Malacca Strait and surrounding waters."
    
    p "Around forty percent of global trade passes through these waters."
    
    menu maritime_focus:
        p "What aspect should we focus on?"
        
        "Strategic importance":
            jump maritime_strategy
            
        "Security challenges":
            jump maritime_security
            
        "Economic impact":
            jump maritime_economy

label maritime_strategy:
    $ knowledge_score += 2
    
    p "The Malacca Strait is one of the world's most crucial maritime chokepoints."
    
    p "It connects the Indian Ocean to the South China Sea and Pacific Ocean."
    
    menu strait_discussion:
        p "What concerns you most about the strait?"
        
        "Naval presence":
            p "Various nations maintain naval forces here to protect their interests."
            $ knowledge_score += 1
            
        "Trade security":
            p "Any disruption here could affect global supply chains."
            $ economic_score += 1
            
        "Regional cooperation":
            p "Countries must work together to ensure safe passage."
            $ diplomatic_score += 1
    
    jump south_china_sea

label south_china_sea:
    scene classroom
    
    p "Now let's discuss the South China Sea situation."
    
    p "Indonesia's Natuna Islands region faces unique challenges."
    
    menu natuna_issues:
        p "What aspect of the Natuna situation interests you?"
        
        "Resource rights":
            jump natuna_resources
            
        "Maritime boundaries":
            jump natuna_borders
            
        "Diplomatic approaches":
            jump natuna_diplomacy

label natuna_resources:
    $ economic_score += 2
    
    p "The Natuna Sea contains significant natural gas reserves."
    
    p "This makes it both an economic asset and a security priority."
    
    menu resource_discussion:
        p "How should Indonesia approach resource development here?"
        
        "Aggressive development":
            p "That could increase tensions with neighbors."
            $ diplomatic_score -= 1
            
        "Cooperative approach":
            p "Working with neighbors while asserting our rights."
            $ diplomatic_score += 2
            
        "Focus on conservation":
            p "Environmental protection is also important."
            $ knowledge_score += 1
    
    jump economy_chapter

label economy_chapter:
    scene classroom
    
    p "Let's examine global economic trends affecting Indonesia."
    
    p "From automotive industry changes to technological competition."
    
    menu economy_focus:
        p "Which sector interests you most?"
        
        "Technology and Innovation":
            jump tech_sector
            
        "Traditional Industries":
            jump traditional_sector
            
        "Future Development":
            jump development_sector

label tech_sector:
    $ economic_score += 2
    
    p "Indonesia's tech sector is growing rapidly."
    
    p "We're seeing competition between Western and Chinese technologies."
    
    menu tech_discussion:
        p "What should be our focus?"
        
        "Digital infrastructure":
            p "Building robust networks is crucial."
            $ economic_score += 1
            
        "Tech education":
            p "We need skilled workers for the future."
            $ knowledge_score += 1
            
        "International partnerships":
            p "Balancing relationships is key."
            $ diplomatic_score += 1
    
    jump regional_development

label regional_development:
    scene classroom
    
    p "Let's explore development across different Indonesian regions."
    
    menu region_choice:
        p "Which region would you like to study?"
        
        "Java's industrial centers":
            jump java_development
            
        "Kalimantan's resources":
            jump kalimantan_development
            
        "Papua's potential":
            jump papua_development

label end_assessment:
    scene classroom
    show professor normal
    
    p "Well done, [player_name]. Let's review what you've learned."
    
    if knowledge_score > 10:
        p "You've shown excellent understanding of geopolitical concepts."
    elif economic_score > 10:
        p "Your grasp of economic factors is impressive."
    else:
        p "You've gained valuable insights into regional dynamics."
    
    p "Remember, these issues are complex and interconnected."
    
    p "Our role is to understand them and work towards regional stability and prosperity."
    
    "Final Scores:"
    "Knowledge: [knowledge_score]"
    "Economic Understanding: [economic_score]"
    "Diplomatic Awareness: [diplomatic_score]"
    
    return

# Additional labels to be expanded
label maritime_security:
    p "Security challenges include piracy and territorial disputes."
    jump south_china_sea

label maritime_economy:
    p "Maritime trade is crucial for global commerce."
    jump south_china_sea

label natuna_borders:
    p "Maritime boundaries require careful diplomatic handling."
    jump economy_chapter

label natuna_diplomacy:
    p "Diplomatic solutions are preferred for territorial issues."
    jump economy_chapter

label traditional_sector:
    p "Traditional industries must adapt to changing times."
    jump regional_development

label development_sector:
    p "Future development must be sustainable and inclusive."
    jump regional_development

label java_development:
    p "Java remains our economic powerhouse."
    jump end_assessment

label kalimantan_development:
    p "Kalimantan balances development with conservation."
    jump end_assessment

label papua_development:
    p "Papua has unique development challenges and opportunities."
    jump end_assessment

label conflict_chapter:
    p "Regional conflicts affect Southeast Asian security."
    jump maritime_chapter