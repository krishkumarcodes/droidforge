import os
import re
import random

colors = ["00FF41", "FF007F", "00E5FF", "FFD700", "B533FF", "FF5733", "33FF57", "3357FF", "F033FF"]

new_apps_markdown = """
### 1. Audio & Video Calling

| App Name | One-line description | GitHub Repo Link | Approx Star Rating |
| :--- | :--- | :--- | :--- |
| **Jitsi Meet** | Video conferencing platform | https://github.com/jitsi/jitsi-meet | 23.5k |
| **Nextcloud Talk** | Self-hosted secure audio/video calls | https://github.com/nextcloud/talk-android | 2k |
| **Meshenger** | P2P voice and video calling over local networks | https://github.com/meshenger-app/meshenger | 500 |
| **Tinode** | Messaging platform with WebRTC calls | https://github.com/tinode/chat | 10k |
| **SipDroid** | Classic SIP/VoIP client | https://github.com/i-p-tel/sipdroid | 800 |
| **Linphone** | Open source SIP client for A/V calls | https://github.com/BelledonneCommunications/linphone-android | 2k |
| **Jami** | P2P audio and video communication | https://github.com/savoirfairelinux/jami-client-android | 500 |
| **Element Android** | Matrix client with video calls | https://github.com/vector-im/element-android | 9k |
| **MiroTalk** | WebRTC P2P video conferencing | https://github.com/miroslavpejic85/mirotalk | 1.5k |
| **SipApp** | Simple voice call app using SIP | https://github.com/aminrahkan/SipApp | 100 |

### 2. Kids & Educational

| App Name | One-line description | GitHub Repo Link | Approx Star Rating |
| :--- | :--- | :--- | :--- |
| **ai4kids_android** | AI and coding puzzles for kids | https://github.com/alfredang/ai4kids_android | 50 |
| **Oppia Android** | Numeracy and literacy lessons for offline learning | https://github.com/oppia/oppia-android | 500 |
| **my-elementary** | Math, animals, and songs for children | https://github.com/fobybus/my-elementary | 100 |
| **e_learning** | App for learning English interactively | https://github.com/dardanbekteshi/e_learning | 50 |
| **LearnMath** | Tactile mental math training game | https://github.com/sidhant947/LearnMath | 50 |
| **Coloring Book** | Coloring app tailored for kids 2+ | https://github.com/niccokunzmann/coloring-book | 150 |
| **AnkiDroid** | Spaced repetition flashcards | https://github.com/ankidroid/Anki-Android | 12k |
| **QuizFlow** | Modern open-source alternative to Quizlet | https://github.com/douxxtech/QuizFlow | 100 |
| **Element Friends** | Chemistry combining game for kids | https://github.com/jeiel85/element-friends | 50 |
| **Antura and the Letters** | Literacy and language-learning game | https://github.com/vgwb/Antura | 200 |

### 3. Hardware & Gadget Companions

| App Name | One-line description | GitHub Repo Link | Approx Star Rating |
| :--- | :--- | :--- | :--- |
| **Android-Companion** | Phone notifications and control via BLE | https://github.com/Bellafaire/Android-Companion-App-For-BLE-Devices | 20 |
| **AsteroidOSSync** | Official companion app for AsteroidOS smartwatches | https://github.com/AsteroidOS/AsteroidOSSync | 250 |
| **ZSWatch** | Companion app for the open-source Zephyr smartwatch | https://github.com/ZSWatch/ZSWatch | 1.5k |
| **open-watch** | App to process smartwatch sensor data over Bluetooth | https://github.com/SMotlaq/open-watch | 150 |
| **Wristkey** | 2FA client specifically designed for Android smartwatches | https://github.com/0x4f53/Wristkey | 50 |
| **DroneKit-Android** | Library/app to control MAVLink drones | https://github.com/dronekit/dronekit-android | 400 |
| **ESP-Drone-Android** | Control quadcopters via USB OTG or BLE | https://github.com/EspressifApps/ESP-Drone-Android | 100 |
| **DroidDrone** | App to control drones over the internet | https://github.com/DroidDrone/DroidDrone | 50 |
| **OpenDroneID Android** | Scans and displays Remote ID signals from drones | https://github.com/opendroneid/android-receiver | 150 |
| **asv-drones** | Ground control station for ArduPilot/PX4 autopilots | https://github.com/asv-soft/asv-drones | 20 |

### 4. Creative Writing & Outlining

| App Name | One-line description | GitHub Repo Link | Approx Star Rating |
| :--- | :--- | :--- | :--- |
| **Markor** | Popular feature-rich Markdown editor for writing | https://github.com/gsantner/markor | 4k |
| **Orgzly** | Powerful outlining tool using Org mode | https://github.com/orgzly/orgzly-android | 3.5k |
| **Notesnook** | Privacy-focused note-taking with deep organization | https://github.com/streetwriters/notesnook | 8.5k |
| **GitJournal** | Notes linked to Git repos for ultimate version control | https://github.com/GitJournal/GitJournal | 3k |
| **Noteless** | Markdown-based writing app with tag organization | https://github.com/redsolver/noteless | 500 |
| **MarkText for Android** | WYSIWYG writing app adapted for mobile | https://github.com/Renakoni/marktext-android | 150 |
| **OpenNote-Compose** | Markdown notebook built with Jetpack Compose | https://github.com/YangDai2003/OpenNote-Compose | 50 |
| **Markdown Editor** | Native editor with tools for importing text files | https://github.com/luizlealdev/markdown-editor | 50 |
| **Quillpad** | Open-source material-design note-taking app | https://github.com/quillpad/quillpad | 800 |
| **SimpleMarkdown** | Clean, straightforward Markdown writing tool | https://github.com/wbrawner/SimpleMarkdown | 300 |

### 5. Meditation & Mindfulness

| App Name | One-line description | GitHub Repo Link | Approx Star Rating |
| :--- | :--- | :--- | :--- |
| **Medito** | Popular, completely free guided meditation app | https://github.com/meditohq/medito-app | 1.5k |
| **Mindful** | Digital wellbeing app to block distractions and build focus | https://github.com/akaMrNagar/Mindful | 50 |
| **Breathly** | Guided breathing exercises and daily relaxation | https://github.com/mmazzarolo/breathly-app | 200 |
| **Hey Linda** | Alternative meditation app with progress tracking | https://github.com/heylinda/heylinda-app | 100 |
| **Hypoxic** | Guided breathing with extensive customization | https://github.com/kenoma/Hypoxic | 50 |
| **Respira** | Minimalist app for stress management and guided breathing | https://github.com/eduardobussien/Respira | 50 |
| **DailySitting** | Small meditation timer integrating with Health Connect | https://github.com/stigmergic-org/DailySitting | 50 |
| **RelaxMeditationApp** | Modern app with calming sounds and breathing exercises | https://github.com/devsoumikpal/RelaxMeditationApp | 30 |
| **Vipassana App** | Framework to create custom guided meditation tracks | https://github.com/happyruss/vipassana_android | 20 |
| **BMonk** | Productivity and meditation timer in Kotlin | https://github.com/hardikchawla/BMonk | 10 |
"""

categories = re.findall(r'### \d+\. (.*?)\n(.*?)(?=\n### |\Z)', new_apps_markdown, re.DOTALL)

with open("README.md", "r") as f:
    main_readme = f.read()

# Remove the old footer to append the new list and then add the new footer
main_readme_body = main_readme.split("---\n\n<div align=\"center\">")[0]

start_idx = 65
new_links = ""

for name, table in categories:
    folder_name = f"{start_idx:02d}-{name.replace(' ', '_').replace('&', 'and').replace('/', '_').replace('(', '').replace(')', '').replace(',', '')}"
    os.makedirs(folder_name, exist_ok=True)
    
    color = random.choice(colors)
    sub_readme = f"""<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,100:{color}&height=150&section=header&text={name.replace(' ', '%20').replace('&', '%26')}&fontSize=40&fontColor={color}&animation=fadeIn&fontAlignY=40" width="100%" alt="Header" />
</div>

## 📱 {name}

{table.strip()}

<br>

<div align="center">
  <p><strong>⭐ If you found these apps useful, please give the main repository a STAR! ⭐</strong></p>
  <a href="../README.md">⬅️ Back to Main Directory</a>
</div>
"""
    with open(f"{folder_name}/README.md", "w") as f:
        f.write(sub_readme)
    
    new_links += f"- [**{name}**](./{folder_name}/) ({table.strip().count('|') // 4 - 2} apps)\n"
    start_idx += 1

main_readme_body += new_links

# Add the new requested footer
main_readme_body += """
---

<div align="center">
  <p><strong>⭐ If you found this repository useful, please give it a STAR! ⭐</strong></p>
  <p>Forged by <strong>Krish Kumar</strong></p>
  <a href="https://github.com/krishkumarcodes">
    <img src="https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=00FF41" alt="GitHub" />
  </a>
</div>
"""

# Update the badge to say 370+ Apps
main_readme_body = main_readme_body.replace("Apps-320+-00FF41", "Apps-370+-00FF41")

with open("README.md", "w") as f:
    f.write(main_readme_body)

print(f"Successfully added {len(categories)} new categories and updated main README.")
