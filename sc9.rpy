define professor = Character("Professor", color="#c8ffc8")
define diplomat = Character("Diplomat", color="#c8c8ff")
define economist = Character("Economist", color="#ffc8c8")
define activist = Character("Activist", color="#ffffc8")
define general = Character("General", color="#c8c8c8")
define n = Character("Narrator", color="#ffffff")

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

# And add these missing labels that are referenced but not defined
label meet_professor:
    show professor normal
    professor "Saya akan membimbing Anda dalam analisis strategis."
    return

label meet_diplomat:
    show diplomat normal
    diplomat "Diplomasi adalah seni mengelola hubungan internasional."
    return

label meet_economist:
    show economist normal
    economist "Mari kita pelajari dampak ekonomi dari setiap keputusan."
    return

label meet_activist:
    show activist normal
    activist "Suara masyarakat harus selalu didengar."
    return

label meet_general:
    show general normal
    general "Keamanan nasional adalah prioritas utama."
    return

label historical_analysis:
    "Melakukan analisis data historis..."
    return

label stakeholder_mapping:
    "Memetakan para pemangku kepentingan..."
    return

label scenario_projection:
    "Membuat proyeksi berbagai skenario..."
    return

label rest_sequence:
    "Beristirahat sejenak..."
    $ player.energy = min(100, player.energy + 30)
    show screen reward_popup("Energy +30")
    return

label game_ending:
    call enhanced_game_ending
    return

label diplomatic_approach:
    "Menerapkan pendekatan diplomatik..."
    return

label security_approach:
    "Menerapkan pendekatan keamanan..."
    return

label regional_approach:
    "Menerapkan pendekatan regional..."
    return

label trade_analysis:
    "Menganalisis aspek perdagangan..."
    return

label investment_analysis:
    "Menganalisis aspek investasi..."
    return

label maritime_economy:
    "Menganalisis ekonomi maritim..."
    return

label advanced_crisis_management:
    "Menangani krisis tingkat lanjut..."
    return

label strategic_planning:
    "Melakukan perencanaan strategis..."
    return

label impact_analysis:
    "Menganalisis dampak kebijakan..."
    return

label maritime_policy:
    "Mengembangkan kebijakan maritim..."
    return

label economic_policy:
    "Mengembangkan kebijakan ekonomi..."
    return

label cooperation_policy:
    "Mengembangkan kebijakan kerja sama..."
    return

label security_cooperation:
    "Mengembangkan kerja sama keamanan..."
    return

label economic_cooperation:
    "Mengembangkan kerja sama ekonomi..."
    return

label cultural_cooperation:
    "Mengembangkan kerja sama budaya..."
    return

init python:
    # Updated Character class with additional attributes
    class GameCharacter:
        def __init__(self, name, title, trust=0, expertise="", viewpoint=""):
            self.name = name
            self.title = title
            self.trust = trust
            self.expertise = expertise
            self.viewpoint = viewpoint
            self.relationship_level = 0
            self.events_completed = []

    # Quest class to track missions and objectives
    class Quest:
        def __init__(self, id, title, description, requirements=None, rewards=None):
            self.id = id
            self.title = title
            self.description = description
            self.requirements = requirements or {}
            self.rewards = rewards or {}
            self.completed = False
            self.active = False

    # Updated Player Stats with inventory and quests
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
            self.inventory = {}
            self.quests = []
            self.completed_quests = []
            self.active_chapter = 1
            self.unlocked_chapters = {1}  # Start with Chapter 1 unlocked
            
        def add_item(self, item_id, amount=1):
            if item_id in self.inventory:
                self.inventory[item_id] += amount
            else:
                self.inventory[item_id] = amount
                
        def remove_item(self, item_id, amount=1):
            if item_id in self.inventory:
                self.inventory[item_id] = max(0, self.inventory[item_id] - amount)
                if self.inventory[item_id] == 0:
                    del self.inventory[item_id]
                    
        def add_quest(self, quest):
            if quest not in self.quests:
                quest.active = True
                self.quests.append(quest)
                
        def complete_quest(self, quest_id):
            for quest in self.quests:
                if quest.id == quest_id and not quest.completed:
                    quest.completed = True
                    self.completed_quests.append(quest)
                    self.quests.remove(quest)
                    return True
            return False
            
        def unlock_chapter(self, chapter_num):
            self.unlocked_chapters.add(chapter_num)
            renpy.notify(f"Chapter {chapter_num} Unlocked!")

# Define inventory items
define inventory_items = {
    "document": {"name": "Dokumen Penting", "description": "Berkas-berkas rahasia tentang situasi regional."},
    "laptop": {"name": "Laptop", "description": "Alat untuk mengakses dan menganalisis data."},
    "badge": {"name": "Lencana Akses", "description": "Memberikan akses ke area-area tertentu."},
    "research": {"name": "Hasil Penelitian", "description": "Data dan analisis dari berbagai krisis."}
}

# Define initial quests
define initial_quests = [
    Quest(
        "intro_meeting",
        "Pertemuan Pertama",
        "Temui semua tokoh kunci di Pusat Kajian Strategis.",
        {"meetings": 5},
        {"influence": 5, "knowledge": 5}
    ),
    Quest(
        "crisis_analysis",
        "Analisis Krisis",
        "Analisis situasi di Laut China Selatan.",
        {"analysis": 3},
        {"knowledge": 10, "document": 1}
    )
]

# Custom screens for new features
screen chapter_select():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Pilih Chapter" size 40 xalign 0.5
            
            for chapter in range(1, 6):  # 5 chapters total
                if chapter in player.unlocked_chapters:
                    textbutton f"Chapter {chapter}" action [SetVariable("player.active_chapter", chapter), Return()] style "chapter_button"
                else:
                    textbutton f"Chapter {chapter} (Terkunci)" action NullAction() style "chapter_button_locked"
            
            textbutton "Kembali" action Return() xalign 0.5

screen inventory_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Inventaris" size 40 xalign 0.5
            
            if not player.inventory:
                text "Inventaris kosong" xalign 0.5
            else:
                for item_id, amount in player.inventory.items():
                    hbox:
                        spacing 20
                        text f"{inventory_items[item_id]['name']} x{amount}"
                        text inventory_items[item_id]['description'] size 20
            
            textbutton "Tutup" action Hide("inventory_screen") xalign 0.5

screen quest_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Misi Aktif" size 40 xalign 0.5
            
            if not player.quests:
                text "Tidak ada misi aktif" xalign 0.5
            else:
                for quest in player.quests:
                    vbox:
                        spacing 10
                        text quest.title size 30
                        text quest.description size 20
                        if quest.rewards:
                            text "Rewards:" size 20
                            for reward, amount in quest.rewards.items():
                                text f"- {reward}: {amount}" size 18
            
            textbutton "Tutup" action Hide("quest_screen") xalign 0.5

screen reward_popup(reward_text):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 20
        vbox:
            spacing 10
            text "Reward!" size 40 xalign 0.5
            text reward_text size 30
            textbutton "OK" action Hide("reward_popup") xalign 0.5

# Updated main game structure
label start:
    $ player = PlayerStats()
    
    # Initialize quests
    python:
        for quest in initial_quests:
            player.add_quest(quest)
    
    call chapter1_intro
    
    return

# Chapter 1: Introduction and Basic Training
label chapter1_intro:
    scene classroom
    show screen stats_display
    
    n "2024. Dunia menghadapi berbagai krisis, dan Indonesia berada di persimpangan jalan."
    
    show professor normal
    professor "Selamat datang di Pusat Kajian Strategis."
    
    $ player_name = renpy.input("Siapa nama Anda?")
    
    professor "Ini adalah masa yang penuh tantangan, [player_name]."
    
    # Give initial items
    $ player.add_item("laptop")
    $ player.add_item("badge")
    
    show screen reward_popup("Mendapatkan: Laptop dan Lencana Akses")
    
    professor "Gunakan peralatan ini dengan bijak. Anda akan membutuhkannya dalam tugas-tugas ke depan."
    
    call chapter1_main
    
    return

# Chapter 1 Main Content
label chapter1_main:
    scene office
    
    menu chapter1_menu:
        "Apa yang ingin Anda lakukan?"
        
        "Bertemu dengan para ahli" if "intro_meeting" in [q.id for q in player.quests]:
            call expert_meetings
            
        "Analisis situasi awal" if "crisis_analysis" in [q.id for q in player.quests]:
            call initial_analysis
            
        "Buka Inventaris":
            show screen inventory_screen
            
        "Lihat Misi":
            show screen quest_screen
            
        "Istirahat dan Simpan":
            call rest_sequence
    
    # Check if chapter complete
    if len(player.completed_quests) >= 2:  # Both initial quests completed
        $ player.unlock_chapter(2)
        jump chapter_transition
    
    jump chapter1_menu

# Expert Meetings
label expert_meetings:
    scene conference
    
    show professor normal
    professor "Mari saya perkenalkan dengan tim ahli kita."
    
    # Meet each expert
    call meet_professor
    call meet_diplomat
    call meet_economist
    call meet_activist
    call meet_general
    
    # Complete quest
    $ player.complete_quest("intro_meeting")
    show screen reward_popup("Quest Complete: Pertemuan Pertama\nReward: +5 Influence, +5 Knowledge")
    $ player.influence += 5
    $ player.knowledge += 5
    
    return

# Initial Analysis
label initial_analysis:
    scene office
    show professor normal
    
    professor "Mari kita mulai dengan analisis situasi di Laut China Selatan."
    
    menu:
        "Bagaimana pendekatan analisis Anda?"
        
        "Analisis data historis":
            $ player.knowledge += 3
            call historical_analysis
            
        "Pemetaan stakeholder":
            $ player.influence += 3
            call stakeholder_mapping
            
        "Proyeksi skenario":
            $ player.reputation += 3
            call scenario_projection
    
    $ player.complete_quest("crisis_analysis")
    show screen reward_popup("Quest Complete: Analisis Krisis\nReward: +10 Knowledge, +1 Document")
    $ player.knowledge += 10
    $ player.add_item("document")
    
    return

# Chapter Transition
label chapter_transition:
    scene office
    show professor normal
    
    professor "Selamat, [player_name]. Anda telah menyelesaikan pelatihan dasar."
    professor "Chapter berikutnya akan membawa tantangan yang lebih besar."
    
    menu:
        "Apa yang ingin Anda lakukan?"
        
        "Lanjut ke Chapter 2":
            jump chapter2_start
            
        "Buka Chapter Select":
            call screen chapter_select
            
        "Istirahat sejenak":
            call rest_sequence
    
    return

# Style definitions for new UI elements
style chapter_button:
    xalign 0.5
    ypadding 10
    xpadding 20
    background "#4a90e2"
    hover_background "#2980b9"

style chapter_button_locked:
    xalign 0.5
    ypadding 10
    xpadding 20
    background "#95a5a6"
    hover_background "#95a5a6"

# Chapter 2: Regional Crisis Management
label chapter2_start:
    scene conference
    show professor normal
    
    $ current_chapter = 2
    
    # Initialize Chapter 2 quests
    python:
        chapter2_quests = [
            Quest(
                "maritime_crisis",
                "Krisis Maritim",
                "Tangani ketegangan di Laut China Selatan",
                {"analysis": 1, "diplomacy": 1},
                {"influence": 15, "knowledge": 10, "document": 1}
            ),
            Quest(
                "economic_pressure",
                "Tekanan Ekonomi",
                "Analisis dampak ekonomi dari ketegangan regional",
                {"research": 2},
                {"knowledge": 20, "research": 1}
            )
        ]
        for quest in chapter2_quests:
            player.add_quest(quest)

    professor "Selamat datang di fase baru, [player_name]. Situasi regional membutuhkan perhatian kita."
    
    call chapter2_main

# Chapter 2 Main Content
label chapter2_main:
    scene office
    
    menu chapter2_menu:
        "Apa yang ingin Anda tangani?"
        
        "Krisis Maritim" if "maritime_crisis" in [q.id for q in player.quests]:
            call maritime_crisis_handling
            
        "Analisis Ekonomi" if "economic_pressure" in [q.id for q in player.quests]:
            call economic_pressure_analysis
            
        "Buka Inventaris":
            show screen inventory_screen
            
        "Lihat Misi":
            show screen quest_screen
            
        "Status Hubungan":
            show screen relationship_screen
            
        "Istirahat":
            call rest_sequence
    
    # Check chapter completion
    if len([q for q in player.completed_quests if q.id in ["maritime_crisis", "economic_pressure"]]) >= 2:
        $ player.unlock_chapter(3)
        jump chapter3_start
    
    jump chapter2_menu

# Maritime Crisis Handling
label maritime_crisis_handling:
    scene conference
    show diplomat normal at left
    show general normal at right
    
    diplomat "Kita perlu menangani situasi ini dengan hati-hati."
    general "Keamanan maritim adalah prioritas utama."
    
    menu:
        "Bagaimana menangani situasi ini?"
        
        "Pendekatan Diplomatik":
            call diplomatic_approach
            $ player.influence += 5
            $ player.relationships["diplomat"] = player.relationships.get("diplomat", 0) + 1
            
        "Penguatan Patroli":
            call security_approach
            $ player.knowledge += 5
            $ player.relationships["general"] = player.relationships.get("general", 0) + 1
            
        "Koordinasi Regional":
            call regional_approach
            $ player.reputation += 5
    
    $ player.complete_quest("maritime_crisis")
    show screen reward_popup("Quest Complete: Krisis Maritim\nReward: +15 Influence, +10 Knowledge, +1 Document")
    
    return

# Economic Pressure Analysis
label economic_pressure_analysis:
    scene office
    show economist normal
    
    economist "Mari kita analisis dampak ekonomi dari situasi ini."
    
    menu:
        "Fokus analisis?"
        
        "Perdagangan Regional":
            call trade_analysis
            $ player.knowledge += 8
            
        "Investasi Asing":
            call investment_analysis
            $ player.influence += 8
            
        "Sektor Maritim":
            call maritime_economy
            $ player.reputation += 8
    
    $ player.complete_quest("economic_pressure")
    show screen reward_popup("Quest Complete: Tekanan Ekonomi\nReward: +20 Knowledge, +1 Research")
    
    return

# Chapter 3: Crisis Resolution and Policy Development
label chapter3_start:
    scene office
    show professor normal
    
    $ current_chapter = 3
    
    # Initialize Chapter 3 quests
    python:
        chapter3_quests = [
            Quest(
                "policy_development",
                "Pengembangan Kebijakan",
                "Susun kebijakan strategis untuk ketahanan nasional",
                {"research": 2, "analysis": 2},
                {"influence": 25, "knowledge": 20}
            ),
            Quest(
                "regional_cooperation",
                "Kerja Sama Regional",
                "Bangun aliansi strategis dengan negara tetangga",
                {"diplomacy": 3},
                {"reputation": 25, "document": 2}
            )
        ]
        for quest in chapter3_quests:
            player.add_quest(quest)

    professor "Kita memasuki fase krusial, [player_name]. Saatnya mengembangkan solusi jangka panjang."
    
    call chapter3_main

# Chapter 3 Main Content
label chapter3_main:
    scene office
    
    menu chapter3_menu:
        "Apa yang ingin Anda kerjakan?"
        
        "Pengembangan Kebijakan" if "policy_development" in [q.id for q in player.quests]:
            call policy_development
            
        "Kerja Sama Regional" if "regional_cooperation" in [q.id for q in player.quests]:
            call regional_cooperation
            
        "Buka Inventaris":
            show screen inventory_screen
            
        "Lihat Misi":
            show screen quest_screen
            
        "Review Progress":
            call progress_review
            
        "Istirahat":
            call rest_sequence
    
    # Check chapter completion
    if len([q for q in player.completed_quests if q.id in ["policy_development", "regional_cooperation"]]) >= 2:
        $ player.unlock_chapter(4)
        jump chapter4_start
    
    jump chapter3_menu

# New screens for enhanced features
screen relationship_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Status Hubungan" size 40 xalign 0.5
            
            for char, level in player.relationships.items():
                hbox:
                    spacing 20
                    text char.title() size 25
                    bar value level range 10 xsize 200
                    text f"Level {level}" size 25
            
            textbutton "Tutup" action Hide("relationship_screen") xalign 0.5

screen progress_review():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Progress Review" size 40 xalign 0.5
            
            text f"Completed Quests: {len(player.completed_quests)}" size 25
            text f"Active Chapter: {player.active_chapter}" size 25
            text f"Knowledge: {player.knowledge}" size 25
            text f"Influence: {player.influence}" size 25
            text f"Reputation: {player.reputation}" size 25
            
            textbutton "Tutup" action Hide("progress_review") xalign 0.5

# Additional gameplay labels
label policy_development:
    scene conference
    show economist normal at left
    show professor normal at right
    
    professor "Kita perlu kebijakan yang komprehensif."
    
    menu:
        "Area fokus kebijakan?"
        
        "Ketahanan Maritim":
            call maritime_policy
            $ player.knowledge += 10
            $ player.add_item("research")
            
        "Ekonomi Strategis":
            call economic_policy
            $ player.influence += 10
            $ player.add_item("document")
            
        "Kerja Sama Regional":
            call cooperation_policy
            $ player.reputation += 10
    
    $ player.complete_quest("policy_development")
    show screen reward_popup("Quest Complete: Pengembangan Kebijakan\nReward: +25 Influence, +20 Knowledge")
    
    return

label regional_cooperation:
    scene embassy
    show diplomat normal
    
    diplomat "Mari kita perkuat hubungan regional kita."
    
    menu:
        "Fokus kerja sama?"
        
        "Keamanan Bersama":
            call security_cooperation
            $ player.influence += 10
            
        "Ekonomi Regional":
            call economic_cooperation
            $ player.knowledge += 10
            
        "Budaya dan Pendidikan":
            call cultural_cooperation
            $ player.reputation += 10
    
    $ player.complete_quest("regional_cooperation")
    show screen reward_popup("Quest Complete: Kerja Sama Regional\nReward: +25 Reputation, +2 Documents")
    
    return

# Chapter 4: Advanced Crisis Management
label chapter4_start:
    scene office
    show professor normal
    
    $ current_chapter = 4
    
    python:
        chapter4_quests = [
            Quest(
                "advanced_crisis",
                "Manajemen Krisis Lanjutan",
                "Tangani krisis kompleks dengan pendekatan terintegrasi",
                {"analysis": 3, "diplomacy": 2},
                {"influence": 30, "knowledge": 25, "research": 2}
            ),
            Quest(
                "strategic_planning",
                "Perencanaan Strategis",
                "Kembangkan rencana strategis jangka panjang",
                {"research": 3},
                {"knowledge": 35, "document": 3}
            )
        ]
        for quest in chapter4_quests:
            player.add_quest(quest)

    professor "Selamat datang di fase lanjutan, [player_name]. Tantangan akan semakin kompleks."
    
    call chapter4_main

# Chapter 4 Main Content
label chapter4_main:
    scene office
    
    menu chapter4_menu:
        "Pilih aktivitas:"
        
        "Manajemen Krisis" if "advanced_crisis" in [q.id for q in player.quests]:
            call advanced_crisis_management
            
        "Perencanaan Strategis" if "strategic_planning" in [q.id for q in player.quests]:
            call strategic_planning
            
        "Buka Inventaris":
            show screen inventory_screen
            
        "Lihat Misi":
            show screen quest_screen
            
        "Analisis Dampak":
            call impact_analysis
            
        "Istirahat":
            call rest_sequence
    
    # Check chapter completion
    if len([q for q in player.completed_quests if q.id in ["advanced_crisis", "strategic_planning"]]) >= 2:
        $ player.unlock_chapter(5)
        jump chapter5_start
    
    jump chapter4_menu

# Final Chapter: Strategic Leadership
label chapter5_start:
    scene conference
    show professor normal
    
    $ current_chapter = 5
    
    python:
        final_quests = [
            Quest(
                "final_crisis",
                "Krisis Final",
                "Tunjukkan kepemimpinan dalam menghadapi krisis besar",
                {"analysis": 4, "diplomacy": 3, "research": 2},
                {"influence": 50, "knowledge": 40, "reputation": 30}
            )
        ]
        for quest in final_quests:
            player.add_quest(quest)

    professor "Ini adalah ujian terakhir kepemimpinan Anda, [player_name]."
    
    call chapter5_main

# Chapter 5 Main Content
label chapter5_main:
    scene office
    
    menu chapter5_menu:
        "Pilih tindakan final:"
        
        "Hadapi Krisis Final" if "final_crisis" in [q.id for q in player.quests]:
            call final_crisis_resolution
            
        "Review Semua Progress":
            call final_progress_review
            
        "Persiapkan Strategi":
            call strategy_preparation
            
        "Istirahat Terakhir":
            call rest_sequence
    
    # Check for game completion
    if "final_crisis" not in [q.id for q in player.quests]:
        jump game_ending
    
    jump chapter5_menu

# Final Crisis Resolution
label final_crisis_resolution:
    scene conference
    show professor normal at left
    show general normal at right
    
    professor "Ini adalah momen yang menentukan."
    
    menu final_choice:
        "Bagaimana Anda akan menangani krisis final?"
        
        "Pendekatan Diplomatik Menyeluruh":
            call diplomatic_finale
            $ player.influence += 20
            $ player.reputation += 15
            
        "Strategi Ketahanan Nasional":
            call resilience_finale
            $ player.knowledge += 20
            $ player.influence += 15
            
        "Kepemimpinan Regional":
            call leadership_finale
            $ player.reputation += 20
            $ player.knowledge += 15
    
    $ player.complete_quest("final_crisis")
    show screen reward_popup("Quest Complete: Krisis Final\nReward: +50 Influence, +40 Knowledge, +30 Reputation")
    
    return

# Final Progress Review
label final_progress_review:
    scene office
    show professor normal
    
    professor "Mari kita evaluasi perjalanan Anda."
    
    python:
        total_score = player.knowledge + player.influence + player.reputation
        completed_quests = len(player.completed_quests)
        relationship_score = sum(player.relationships.values())
        
        final_assessment = ""
        if total_score > 500:
            final_assessment = "Luar Biasa"
        elif total_score > 300:
            final_assessment = "Sangat Baik"
        else:
            final_assessment = "Baik"
    
    call screen final_progress_screen(total_score, completed_quests, relationship_score, final_assessment)
    
    return

# New final progress screen
screen final_progress_screen(total_score, completed_quests, relationship_score, assessment):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Evaluasi Akhir" size 40 xalign 0.5
            
            text f"Total Score: {total_score}" size 30
            text f"Completed Quests: {completed_quests}" size 30
            text f"Relationship Score: {relationship_score}" size 30
            text f"Final Assessment: {assessment}" size 30
            
            null height 20
            
            text "Pencapaian:" size 25
            text f"- Knowledge: {player.knowledge}" size 20
            text f"- Influence: {player.influence}" size 20
            text f"- Reputation: {player.reputation}" size 20
            
            null height 20
            
            textbutton "Lanjutkan" action Return() xalign 0.5

# Continuing Strategy Preparation
label strategy_preparation:
    scene office
    show professor normal
    
    menu strategy_prep:
        "Persiapan apa yang diperlukan?"
        
        "Konsultasi Tim":
            $ player.influence += 5
            show economist normal at left
            show diplomat normal at right
            economist "Mari kita review strategi ekonomi kita."
            diplomat "Jangan lupa aspek diplomatik kita."
            $ player.add_item("research")
            
        "Analisis Data":
            $ player.knowledge += 5
            show professor normal
            professor "Data yang baik adalah dasar keputusan yang tepat."
            $ player.add_item("document")
            
        "Koordinasi Lapangan":
            $ player.reputation += 5
            show general normal
            general "Eksekusi di lapangan sama pentingnya dengan perencanaan."
    
    show screen reward_popup("Persiapan Selesai!\nMendapatkan: +5 Stats dan Item Baru")
    
    return

# Final Crisis Variants
label diplomatic_finale:
    scene conference
    show diplomat normal at left
    show professor normal at right
    
    diplomat "Pendekatan diplomatik Anda menunjukkan hasil."
    
    menu diplomatic_actions:
        "Langkah selanjutnya?"
        
        "Konferensi Regional":
            $ player.influence += 10
            diplomat "Forum multilateral bisa menjadi solusi."
            
        "Negosiasi Bilateral":
            $ player.knowledge += 10
            diplomat "Pendekatan satu-per-satu bisa lebih efektif."
            
        "Mediasi Internasional":
            $ player.reputation += 10
            diplomat "Pihak ketiga bisa membantu proses ini."
    
    $ player.add_item("document", 2)
    show screen reward_popup("Diplomatic Success!\nReward: +10 Stats, 2 Documents")
    
    return

label resilience_finale:
    scene office
    show general normal at left
    show economist normal at right
    
    general "Ketahanan nasional adalah prioritas utama."
    
    menu resilience_actions:
        "Fokus ketahanan?"
        
        "Keamanan Maritim":
            $ player.influence += 10
            general "Pengamanan wilayah maritim adalah kunci."
            
        "Ekonomi Strategis":
            $ player.knowledge += 10
            economist "Fondasi ekonomi yang kuat adalah benteng terbaik."
            
        "Kohesi Sosial":
            $ player.reputation += 10
            economist "Persatuan dalam keberagaman adalah kekuatan kita."
    
    $ player.add_item("research", 2)
    show screen reward_popup("Resilience Enhanced!\nReward: +10 Stats, 2 Research")
    
    return

label leadership_finale:
    scene conference
    show professor normal
    show diplomat normal at right
    
    professor "Ini saatnya Indonesia menunjukkan kepemimpinan regional."
    
    menu leadership_actions:
        "Bentuk kepemimpinan?"
        
        "Inisiatif Regional":
            $ player.influence += 15
            diplomat "ASEAN bisa menjadi platform yang tepat."
            
        "Inovasi Kebijakan":
            $ player.knowledge += 15
            professor "Kita bisa menjadi model untuk kawasan."
            
        "Diplomasi Budaya":
            $ player.reputation += 15
            diplomat "Soft power kita bisa menjadi instrumen yang efektif."
    
    $ player.add_item("document")
    $ player.add_item("research")
    show screen reward_popup("Leadership Established!\nReward: +15 Stats, New Items")
    
    return

# Enhanced Game Ending System
label enhanced_game_ending:
    scene conference
    show professor normal
    
    python:
        # Calculate final scores
        total_score = player.knowledge + player.influence + player.reputation
        relationship_total = sum(player.relationships.values())
        quest_completion = len(player.completed_quests)
        
        # Determine ending type
        if total_score > 600 and relationship_total > 25:
            ending_type = "best"
        elif total_score > 400 or relationship_total > 20:
            ending_type = "good"
        else:
            ending_type = "standard"
            
        # Calculate achievements
        achievements = []
        if player.knowledge > 200:
            achievements.append("Master Strategist")
        if player.influence > 200:
            achievements.append("Regional Leader")
        if player.reputation > 200:
            achievements.append("Respected Diplomat")
        if quest_completion > 15:
            achievements.append("Quest Master")
        if len(player.inventory) > 10:
            achievements.append("Resource Manager")

    call screen final_assessment(total_score, relationship_total, quest_completion, achievements)
    
    if ending_type == "best":
        call best_ending_enhanced
    elif ending_type == "good":
        call good_ending_enhanced
    else:
        call standard_ending_enhanced
    
    return

# Enhanced Ending Variants
label best_ending_enhanced:
    scene conference
    show professor normal at left
    show diplomat normal at right
    
    professor "Selamat, [player_name]. Anda telah mencapai hasil yang luar biasa."
    diplomat "Kepemimpinan Anda telah membawa perubahan positif di kawasan."
    
    show screen achievements_display
    
    menu:
        "Bagaimana perasaan Anda dengan pencapaian ini?"
        
        "Bangga dengan tim":
            professor "Kerja sama tim adalah kunci kesuksesan kita."
            
        "Fokus pada hasil":
            diplomat "Hasil yang dicapai akan berdampak panjang."
            
        "Siap tantangan baru":
            professor "Perjalanan kepemimpinan tidak pernah berakhir."
    
    call ending_credits
    return

label good_ending_enhanced:
    scene conference
    show professor normal
    
    professor "Anda telah menunjukkan potensi kepemimpinan yang baik."
    
    show screen achievements_display
    
    menu:
        "Apa pembelajaran terpenting Anda?"
        
        "Pentingnya adaptasi":
            professor "Fleksibilitas adalah kunci dalam dunia yang dinamis."
            
        "Kekuatan kolaborasi":
            professor "Bersama kita bisa mencapai lebih banyak."
            
        "Nilai pengalaman":
            professor "Setiap tantangan adalah pelajaran berharga."
    
    call ending_credits
    return

label standard_ending_enhanced:
    scene conference
    show professor normal
    
    professor "Anda telah menyelesaikan program dengan baik."
    
    show screen achievements_display
    
    menu:
        "Apa rencana Anda ke depan?"
        
        "Terus belajar":
            professor "Pembelajaran adalah proses seumur hidup."
            
        "Aplikasikan pengalaman":
            professor "Pengalaman adalah guru terbaik."
            
        "Cari tantangan baru":
            professor "Setiap akhir adalah awal yang baru."
    
    call ending_credits
    return

# New screens for enhanced ending system
screen final_assessment(total_score, relationship_total, quest_completion, achievements):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Penilaian Akhir" size 40 xalign 0.5
            
            text f"Total Score: {total_score}" size 30
            text f"Relationship Score: {relationship_total}" size 30
            text f"Completed Quests: {quest_completion}" size 30
            
            null height 20
            
            text "Achievements Earned:" size 30
            for achievement in achievements:
                text f"- {achievement}" size 25
            
            null height 20
            
            textbutton "Lanjutkan" action Return() xalign 0.5

screen achievements_display():
    frame:
        xalign 0.98
        yalign 0.02
        vbox:
            spacing 10
            text "Achievements" size 25
            for achievement in achievements:
                text achievement size 20

# Credits Sequence
label ending_credits:
    scene black with dissolve
    
    show text "Strategic Leadership Simulator" with dissolve
    pause 2
    hide text with dissolve
    
    show text "Final Statistics" with dissolve
    pause 1
    show text f"Knowledge: {player.knowledge}\nInfluence: {player.influence}\nReputation: {player.reputation}" with dissolve
    pause 3
    hide text with dissolve
    
    show text "Thank you for playing!" with dissolve
    pause 2
    hide text with dissolve
    
    return

# Game Over Screen
screen game_over():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Game Complete!" size 40 xalign 0.5
            
            text f"Final Score: {total_score}" size 30
            text f"Achievements Unlocked: {len(achievements)}" size 30
            
            null height 20
            
            hbox:
                spacing 30
                textbutton "New Game" action Start()
                textbutton "Load Game" action ShowMenu("load")
                textbutton "Quit" action Quit()

# Define custom styles for new UI elements
style achievement_text:
    size 20
    color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]

style final_score_text:
    size 30
    color "#ffffff"
    text_align 0.5
    xalign 0.5

style credit_text:
    size 40
    color "#ffffff"
    text_align 0.5
    xalign 0.5
    yalign 0.5

screen stats_display():
    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 20
        
        vbox:
            spacing 10
            text "Stats" size 30
            text f"Knowledge: {player.knowledge}" size 20
            text f"Influence: {player.influence}" size 20
            text f"Reputation: {player.reputation}" size 20
            text f"Energy: {player.energy}" size 20