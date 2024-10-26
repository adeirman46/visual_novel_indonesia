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
define professor = Character("Prof. Wijaya", color="#b8b665", image="professor")
define diplomat = Character("Duta Besar Chen", color="#4a90e2", image="diplomat")
define economist = Character("Dr. Suharto", color="#2ecc71", image="economist")
define activist = Character("Maya Kusuma", color="#e74c3c", image="activist")
define general = Character("Jenderal Sudirman", color="#95a5a6", image="general")
define n = Character("Narator", color="#ffffff")

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
            text "Hari: [day]" size 20
            text "Energi: [player.energy]%" size 20
            text "Pengetahuan: [player.knowledge]" size 20
            text "Pengaruh: [player.influence]" size 20
            text "Reputasi: [player.reputation]" size 20

# Game start
label start:
    $ player = PlayerStats()
    
    scene classroom
    show screen stats_display
    
    n "2024. Dunia menghadapi berbagai krisis, dan Indonesia berada di persimpangan jalan."
    
    show professor normal
    professor "Selamat datang di Pusat Kajian Strategis."
    
    $ player_name = renpy.input("Siapa nama Anda?")
    
    professor "Ini adalah masa yang penuh tantangan, [player_name]. Kita membutuhkan pemikiran jernih dan kepemimpinan yang kuat."
    
    professor "Ketegangan di Laut China Selatan meningkat, ekonomi kita menghadapi tekanan resesi global, dan perubahan iklim mengancam kepulauan kita."
    
    professor "Analisis dan keputusan Anda akan membantu membentuk respons Indonesia terhadap tantangan-tantangan ini."

    jump main_hub

# Main gameplay hub
label main_hub:
    scene office
    menu location_choice:
        "Ke mana Anda ingin pergi?"
        
        "Ruang Strategi - Diskusi Krisis Terkini" if player.energy >= 20:
            $ player.energy -= 20
            jump strategy_room
            
        "Kawasan Kedutaan - Temui Tokoh Penting" if player.energy >= 15:
            $ player.energy -= 15
            jump embassy_district
            
        "Taman Mini Indonesia - Jalan-jalan" if player.energy >= 10:
            $ player.energy -= 10
            jump taman_mini
            
        "Pantai Ancol - Menjernihkan Pikiran" if player.energy >= 10:
            $ player.energy -= 10
            jump ancol_beach
            
        "Istirahat dan Renungkan":
            call rest_sequence
            
        "Simpan Progres":
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
    
    professor "Citra satelit terbaru menunjukkan peningkatan kehadiran militer di perairan yang dipersengketakan."
    general "Kita perlu menunjukkan kekuatan sambil menghindari konfrontasi langsung."
    
    menu:
        "Bagaimana Anda menilai situasi ini?"
        
        "Menganjurkan respons multilateral ASEAN":
            call diplomatic_approach
            
        "Menyarankan peningkatan patroli maritim":
            call military_approach
            
        "Mengusulkan pengaruh ekonomi melalui hubungan dagang":
            call economic_approach
            
        "Meminta waktu lebih untuk menganalisis situasi":
            call analytical_approach
    
    return

# Economic Crisis
label economic_crisis:
    show economist normal at left
    show activist normal at right
    
    economist "Resesi global berdampak berat pada ekspor kita."
    activist "Rakyat kecil sedang berjuang."
    
    menu:
        "Bagaimana mengatasi krisis ekonomi?"
        
        "Lindungi industri dalam negeri":
            call domestic_protection
            
        "Cari investasi asing":
            call foreign_investment
            
        "Dukung usaha kecil menengah":
            call small_business_support
    
    return

# Domestic Protection
label domestic_protection:
    show economist normal
    economist "Melindungi industri kita memiliki manfaat dan risiko."
    
    menu:
        "Langkah perlindungan mana yang harus diterapkan?"
        
        "Regulasi impor":
            $ player.knowledge += 2
            economist "Regulasi yang tepat dapat membantu industri lokal berkembang."
            
        "Subsidi industri":
            $ player.influence += 2
            economist "Dukungan strategis dapat memperkuat sektor kunci."
            
        "Pengembangan keterampilan":
            $ player.reputation += 2
            economist "Investasi pada tenaga kerja membangun kekuatan jangka panjang."
    
    return

# Climate Crisis
label climate_crisis:
    show activist normal at left
    show economist normal at right
    
    activist "Perubahan iklim mengancam pulau-pulau kita."
    economist "Dampak ekonominya bisa sangat parah."
    
    menu:
        "Bagaimana menangani perubahan iklim?"
        
        "Infrastruktur hijau":
            call green_infrastructure
            
        "Pengurangan emisi":
            call emission_reduction
            
        "Adaptasi masyarakat":
            call community_adaptation
    
    return

# Tech Sovereignty
label tech_sovereignty_crisis:
    show economist normal at left
    show general normal at right
    
    economist "Infrastruktur digital kita butuh kemandirian."
    general "Kedaulatan teknologi adalah keamanan nasional."
    
    menu:
        "Bagaimana mencapai kedaulatan teknologi?"
        
        "Kembangkan teknologi lokal":
            call local_tech_development
            
        "Kemitraan internasional":
            call tech_partnerships
            
        "Fokus keamanan siber":
            call cyber_security
    
    return

# Green Infrastructure
label green_infrastructure:
    show economist normal
    economist "Infrastruktur berkelanjutan adalah investasi masa depan."
    
    menu:
        "Infrastruktur mana yang diprioritaskan?"
        
        "Energi terbarukan":
            $ player.knowledge += 2
            economist "Energi bersih mendorong pertumbuhan berkelanjutan."
            
        "Transportasi publik":
            $ player.influence += 2
            economist "Transportasi lebih baik mengurangi emisi dan kemacetan."
            
        "Bangunan hijau":
            $ player.reputation += 2
            economist "Bangunan efisien menghemat sumber daya."
    
    return

# Embassy District
label embassy_district:
    scene embassy
    menu:
        "Siapa yang ingin Anda temui?"
        
        "Duta Besar Chen":
            call chen_meeting
            
        "Dr. Suharto":
            call suharto_meeting
            
        "Maya Kusuma":
            call maya_meeting
            
        "Kembali ke Kantor":
            jump main_hub
    
    return

# Character Meetings
label chen_meeting:
    show diplomat normal
    diplomat "Dinamika regional berubah dengan cepat."
    
    menu:
        "Topik apa yang ingin dibahas?"
        
        "Kerja sama maritim":
            $ player.knowledge += 2
            diplomat "Laut menghubungkan bangsa kita."
            
        "Kemitraan ekonomi":
            $ player.influence += 2
            diplomat "Perdagangan membangun jembatan."
            
        "Pertukaran budaya":
            $ player.reputation += 2
            diplomat "Pemahaman tumbuh dari ikatan budaya."
    
    return

# Recreational Activities
label taman_mini:
    scene park
    n "Keberagaman Indonesia terpampang di sini."
    
    menu:
        "Apa yang menarik perhatian Anda?"
        
        "Pameran budaya":
            $ player.knowledge += 2
            n "Tradisi kita menceritakan kisah kita."
            
        "Aktivitas ekonomi":
            $ player.influence += 2
            n "Perdagangan menghubungkan komunitas."
            
        "Program pendidikan":
            $ player.reputation += 2
            n "Pembelajaran melestarikan warisan kita."
    
    return

label ancol_beach:
    scene beach
    n "Laut memberi perspektif."
    
    menu:
        "Apa yang Anda amati?"
        
        "Aktivitas maritim":
            $ player.knowledge += 2
            n "Kapal-kapal membawa kemakmuran kita."
            
        "Pembangunan pesisir":
            $ player.influence += 2
            n "Pembangunan harus menghormati alam."
            
        "Perubahan lingkungan":
            $ player.reputation += 2
            n "Lingkungan memberi sinyal masa depan kita."
    
    return

# Rest and Reflection
label rest_sequence:
    scene bedroom
    "Waktunya istirahat dan merenung."
    $ player.energy = min(100, player.energy + 40)
    $ day += 1
    
    menu:
        "Bagaimana menggunakan waktu ini?"
        
        "Pelajari laporan":
            $ player.knowledge += 2
            "Pengetahuan membangun pemahaman."
            
        "Rencanakan strategi":
            $ player.influence += 2
            "Perencanaan yang baik memungkinkan keberhasilan."
            
        "Meditasi":
            $ player.reputation += 2
            "Pikiran jernih membuat pilihan lebih baik."
    
    jump main_hub

# Game Ending
label game_ending:
    scene office
    show professor normal
    
    professor "Keputusan Anda telah membentuk masa depan Indonesia, [player_name]."
    
    if player.influence > 35 and player.knowledge > 30:
        call best_ending
    elif player.influence > 30:
        call good_ending
    else:
        call standard_ending
    
    return

# Ending Variants
label best_ending:
    professor "Kepemimpinan Anda yang seimbang telah memposisikan Indonesia sebagai pemimpin regional."
    
    "Pencapaian:"
    "- Meningkatkan stabilitas regional"
    "- Memperbaiki ketahanan ekonomi"
    "- Memperkuat kohesi sosial"
    
    "Tamat - Ahli Strategi"
    return

label good_ending:
    professor "Pengaruh kuat Anda telah membantu mengarahkan Indonesia melalui masa-masa menantang."
    
    "Pencapaian:"
    "- Membangun aliansi kuat"
    "- Melindungi kepentingan nasional"
    "- Mempertahankan stabilitas"
    
    "Tamat - Pemimpin Terampil"
    return

label standard_ending:
    professor "Anda telah berkontribusi pada pembangunan Indonesia dengan cara yang berarti."
    
    "Pencapaian:"
    "- Mendapatkan pengalaman berharga"
    "- Mengembangkan wawasan penting"
    "- Meletakkan dasar untuk kemajuan masa depan"
    
    "Tamat - Analis Menjanjikan"
    return

# Maritime Focus
label maritime_trade_insight:
    show economist normal
    economist "Perdagangan maritim adalah kekuatan historis kita."
    
    menu:
        "Aspek maritim mana yang perlu dikembangkan?"
        
        "Infrastruktur pelabuhan":
            $ player.knowledge += 2
            economist "Pelabuhan modern mendorong pertumbuhan perdagangan."
            
        "Kapasitas pelayaran":
            $ player.influence += 2
            economist "Kapal sendiri mengamankan jalur perdagangan kita."
            
        "Layanan maritim":
            $ player.reputation += 2
            economist "Layanan menambah nilai perdagangan maritim."

# Fishing Industry
label fishing_industry_insight:
    show activist normal
    activist "Perikanan berkelanjutan melindungi mata pencaharian."
    
    menu:
        "Bagaimana mendukung komunitas nelayan?"
        
        "Peralatan modern":
            $ player.knowledge += 2
            activist "Alat yang lebih baik meningkatkan efisiensi."
            
        "Praktik berkelanjutan":
            $ player.influence += 2
            activist "Keberlanjutan menjamin kelangsungan hidup jangka panjang."
            
        "Dukungan komunitas":
            $ player.reputation += 2
            activist "Komunitas kuat mempertahankan tradisi."
    
    return

# Strategic Development Labels
label economic_development:
    show economist normal
    economist "Pembangunan ekonomi harus inklusif dan berkelanjutan."
    
    menu:
        "Strategi pembangunan mana yang harus dikejar?"
        
        "Modernisasi industri":
            $ player.knowledge += 2
            economist "Industri modern menciptakan pekerjaan lebih baik."
            
        "Ekonomi digital":
            $ player.influence += 2
            economist "Transformasi digital membuka peluang baru."
            
        "Pertumbuhan hijau":
            $ player.reputation += 2
            economist "Pertumbuhan berkelanjutan mengamankan masa depan kita."
    
    return

# Social Development
label social_development:
    show activist normal
    activist "Pembangunan sosial adalah fondasi kemajuan."
    
    menu:
        "Aspek sosial mana yang perlu difokuskan?"
        
        "Akses kesehatan":
            $ player.knowledge += 2
            activist "Kesehatan adalah dasar pembangunan."
            
        "Kualitas pendidikan":
            $ player.influence += 2
            activist "Pendidikan berkualitas mengubah masyarakat."
            
        "Perlindungan sosial":
            $ player.reputation += 2
            activist "Jaring pengaman melindungi masyarakat rentan."
    
    return

# Infrastructure Planning
label infrastructure_planning:
    show economist normal
    economist "Infrastruktur membentuk kemungkinan pembangunan."
    
    menu:
        "Infrastruktur mana yang diprioritaskan?"
        
        "Jaringan transportasi":
            $ player.knowledge += 2
            economist "Konektivitas mendorong pertumbuhan."
            
        "Infrastruktur digital":
            $ player.influence += 2
            economist "Jaringan digital memungkinkan ekonomi modern."
            
        "Pembangunan perkotaan":
            $ player.reputation += 2
            economist "Kota cerdas meningkatkan kualitas hidup."
    
    return

# Local Tech Development
label local_tech_development:
    show economist normal
    economist "Membangun basis teknologi sendiri penting untuk kemandirian."
    
    menu:
        "Sektor teknologi mana yang diprioritaskan?"
        
        "Infrastruktur digital":
            $ player.knowledge += 2
            economist "Infrastruktur kuat memungkinkan inovasi."
            
        "Pengembangan perangkat lunak":
            $ player.influence += 2
            economist "Perangkat lunak lokal mengurangi ketergantungan asing."
            
        "Manufaktur perangkat keras":
            $ player.reputation += 2
            economist "Kemampuan manufaktur menjamin keamanan rantai pasokan."
    
    return

# Tech Partnerships
label tech_partnerships:
    show diplomat normal
    diplomat "Kemitraan strategis dapat mempercepat pembangunan kita."
    
    menu:
        "Kemitraan seperti apa?"
        
        "Kolaborasi penelitian":
            $ player.knowledge += 2
            diplomat "Penelitian bersama membangun kapasitas bersama."
            
        "Transfer teknologi":
            $ player.influence += 2
            diplomat "Berbagi pengetahuan mempercepat kemajuan."
            
        "Usaha patungan":
            $ player.reputation += 2
            diplomat "Sumber daya gabungan mencapai lebih banyak."
    
    return

# Cyber Security
label cyber_security:
    show general normal
    general "Keamanan digital adalah keamanan nasional."
    
    menu:
        "Aspek keamanan mana yang perlu fokus?"
        
        "Perlindungan infrastruktur":
            $ player.knowledge += 2
            general "Sistem kritis harus diamankan."
            
        "Kedaulatan data":
            $ player.influence += 2
            general "Kontrol atas data adalah kekuatan strategis."
            
        "Pertahanan siber":
            $ player.reputation += 2
            general "Pertahanan aktif melindungi kepentingan kita."
    
    return

# Additional Character Meetings
label suharto_meeting:
    show economist normal
    economist "Tren ekonomi membentuk takdir bangsa."
    
    menu:
        "Isu ekonomi mana yang akan dibahas?"
        
        "Kebijakan industri":
            $ player.knowledge += 2
            economist "Industri strategis perlu pembinaan cermat."
            
        "Hubungan perdagangan":
            $ player.influence += 2
            economist "Kemitraan dagang membangun kemakmuran."
            
        "Perencanaan pembangunan":
            $ player.reputation += 2
            economist "Perencanaan jangka panjang menjamin pertumbuhan berkelanjutan."
    
    return

# Maya Meeting
label maya_meeting:
    show activist normal
    activist "Keadilan sosial harus memandu pembangunan."
    
    menu:
        "Isu sosial mana yang perlu ditangani?"
        
        "Kesenjangan pendapatan":
            $ player.knowledge += 2
            activist "Kesetaraan menciptakan masyarakat stabil."
            
        "Keadilan lingkungan":
            $ player.influence += 2
            activist "Perlindungan lingkungan melayani semua orang."
            
        "Akses pendidikan":
            $ player.reputation += 2
            activist "Pendidikan mengubah kehidupan."
    
    return

# Environmental Issues
label environmental_insight:
    show activist normal
    activist "Perubahan lingkungan mempengaruhi semua orang."
    
    menu:
        "Isu lingkungan mana yang perlu perhatian?"
        
        "Kualitas udara":
            $ player.knowledge += 2
            activist "Udara bersih adalah hak dasar."
            
        "Sumber daya air":
            $ player.influence += 2
            activist "Keamanan air adalah keamanan hidup."
            
        "Pelestarian hutan":
            $ player.reputation += 2
            activist "Hutan adalah warisan alam kita."
    
    return

# Tourism Development
label tourism_insight:
    show economist normal
    economist "Pariwisata dapat mendorong pembangunan berkelanjutan."
    
    menu:
        "Bagaimana mengembangkan pariwisata?"
        
        "Wisata budaya":
            $ player.knowledge += 2
            economist "Pengalaman budaya menarik pengunjung."
            
        "Ekowisata":
            $ player.influence += 2
            economist "Wisata berbasis alam melestarikan lingkungan."
            
        "Wisata komunitas":
            $ player.reputation += 2
            economist "Masyarakat lokal harus mendapat manfaat langsung."
    
    return

# Analytical Approach
label analytical_approach:
    show professor normal
    professor "Analisis mendalam diperlukan untuk keputusan yang tepat."
    
    menu:
        "Aspek mana yang perlu dianalisis?"
        
        "Data historis":
            $ player.knowledge += 2
            professor "Sejarah memberi pelajaran berharga."
            
        "Tren saat ini":
            $ player.influence += 2
            professor "Memahami situasi terkini sangat penting."
            
        "Proyeksi masa depan":
            $ player.reputation += 2
            professor "Perencanaan ke depan membutuhkan visi jelas."
    
    return

# Military Approach
label military_approach:
    show general normal
    general "Pertahanan kuat mencegah konflik."
    
    menu:
        "Strategi militer mana yang diadopsi?"
        
        "Modernisasi peralatan":
            $ player.knowledge += 2
            general "Kemampuan modern menangkal agresi."
            
        "Peningkatan pelatihan":
            $ player.influence += 2
            general "Pasukan terlatih lebih efektif."
            
        "Perbaikan koordinasi":
            $ player.reputation += 2
            general "Koordinasi lebih baik melipatgandakan kekuatan kita."
    
    return

# Economic Approach
label economic_approach:
    show economist normal
    economist "Pengaruh ekonomi bisa menjadi alat yang efektif."
    
    menu:
        "Pendekatan ekonomi mana yang dipilih?"
        
        "Insentif perdagangan":
            $ player.knowledge += 2
            economist "Insentif dapat mempengaruhi perilaku."
            
        "Kerja sama investasi":
            $ player.influence += 2
            economist "Investasi menciptakan kepentingan bersama."
            
        "Pengembangan pasar":
            $ player.reputation += 2
            economist "Pasar baru membuka peluang baru."
    
    return
