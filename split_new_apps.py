import os
import re
import random

colors = ["00FF41", "FF007F", "00E5FF", "FFD700", "B533FF", "FF5733", "33FF57", "3357FF", "F033FF"]

new_apps_markdown = """
### 1. Developer Utilities (Advanced)

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Shizuku** | Allows apps to use root-level system APIs directly without needing full root access. | https://github.com/RikkaApps/Shizuku | 13.5k |
| **AppManager** | Advanced Android package manager and viewer for modifying hidden app permissions and settings. | https://github.com/MuntashirAkon/AppManager | 5.2k |
| **LeakCanary** | A memory leak detection library and background analyzer app for Android developers. | https://github.com/square/leakcanary | 29.1k |
| **Logfox** | A clean, modern logcat reader app for Android to view system and app logs on-device. | https://github.com/F0x1d/Logfox | 800 |
| **InstallWithOptions** | Shizuku-powered app installer to bypass system limits (force install, downgrade apps). | https://github.com/zacharee/InstallWithOptions | 1.5k |

### 2. Open Source Games (Unique)

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Shattered Pixel Dungeon** | A visually enhanced, deeply strategic open-source roguelike RPG with complex mechanics. | https://github.com/00-Evan/shattered-pixel-dungeon | 4.8k |
| **Mindustry** | A massive sandbox factory-building tower defense game with deep resource management. | https://github.com/Anuken/Mindustry | 22.6k |
| **Unciv** | A remarkably detailed open-source 2D remake of Civilization V optimized for mobile. | https://github.com/yairm210/Unciv | 7.4k |
| **Simon Tatham's Puzzles** | A lightweight but challenging collection of 40+ ad-free logic puzzle games. | https://github.com/chrisboyle/sgtpuzzles | 1.2k |
| **Crystal Trails** | A polished 2D pixel-art action platformer game built specifically in Godot 4. | https://github.com/dvgamelab/crystal-trails | 200 |

### 3. Photography & Video Editing (Advanced)

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **PhotonCamera** | Advanced camera app focusing on advanced computational static photography and HDR. | https://github.com/eszdman/PhotonCamera | 1.4k |
| **MotionCam** | Unique open-source camera app capable of capturing true RAW video on Android devices. | https://github.com/mirsadm/MotionCam | 1.8k |
| **FreeDCam** | A highly advanced open-source camera aimed at absolute manual control and diverse APIs. | https://github.com/defcomg/FreeDCam | 400 |
| **Fossify Gallery** | A highly customizable, privacy-focused gallery app featuring EXIF metadata stripping. | https://github.com/FossifyOrg/Gallery | 2.1k |
| **LibreCamera** | A modern, free, and privacy-first Android camera application built using Flutter. | https://github.com/iakdis/librecamera | 100 |

### 4. Offline Dictionaries & Translation

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Kiwix** | The ultimate offline reader for Wikipedia, StackExchange, and comprehensive dictionaries. | https://github.com/kiwix/kiwix-android | 1.3k |
| **Aard 2** | An advanced offline dictionary reader capable of parsing massive compressed wiki formats. | https://github.com/itkach/aard2-android | 700 |
| **dikt** | A minimalist, offline cross-platform dictionary reader designed for one-handed use. | https://github.com/maxim-saplin/dikt | 100 |
| **OSS-Dict** | An entirely offline and ad-free dictionary application dedicated strictly to definitions. | https://github.com/Akylas/OSS-Dict | 50 |
| **EnglishWhiz** | A fluid, Jetpack Compose-based offline English dictionary and thesaurus application. | https://github.com/ezechuka/EnglishWhiz | 50 |

### 5. Security & Privacy Scanners

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Exodus Privacy** | Analyzes the apps installed on your device to reveal embedded privacy trackers. | https://github.com/Exodus-Privacy/exodus-android-app | 900 |
| **TrackerControl** | Analyzes network traffic to block hidden data collection trackers and ads system-wide. | https://github.com/TrackerControl/tracker-control-android | 1.7k |
| **LibreAV** | A lightweight, open-source anti-malware app utilizing machine learning to detect threats. | https://github.com/projectmatris/antimalwareapp | 300 |
| **AndroDR** | An on-device endpoint detection tool that scans for spyware, stalkerware, and anomalies. | https://github.com/yasirhamza/AndroDR | 200 |
| **NetGuard** | A sophisticated rootless firewall that tracks and blocks individual app network accesses. | https://github.com/M66B/NetGuard | 9.0k |

### 6. Task Automation & Scripting

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Easer** | A highly flexible, event-driven automation app that orchestrates conditions and operations. | https://github.com/renyuneyun/Easer | 1.8k |
| **AutoDroid** | A privacy-friendly Android automation toolkit for creating localized triggers and actions. | https://github.com/Aditsyal/autodroid | 100 |
| **DroidWright** | An advanced automation framework offering full system script control using JavaScript. | https://github.com/tas33n/DroidWright | 50 |
| **OpenDroid** | An autonomous AI agent utilizing accessibility features for smart UI automation. | https://github.com/yashab-cyber/opendroid | 300 |
| **PrivateAgent** | An AI-driven, LLM-powered background agent to automate multi-step UI navigation tasks. | https://github.com/orailnoor/private-agent | 100 |

### 7. Blogging & Journaling (Offline)

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Logseq** | A local-first, privacy-focused Markdown outliner and knowledge-base journaling tool. | https://github.com/logseq/logseq | 31.0k |
| **Standard Notes** | A highly secure, end-to-end encrypted offline-capable note-taking and journaling app. | https://github.com/standardnotes/app | 5.0k |
| **Joplin** | An extremely robust open-source markdown journal/notebook with offline capabilities. | https://github.com/laurent22/joplin | 47.0k |
| **Markor** | A powerful, lightweight Markdown text editor specifically tailored for local journaling. | https://github.com/gsantner/markor | 3.7k |
| **Saber** | A digital, cross-platform notebook and journal specializing in handwritten offline notes. | https://github.com/saber-notes/saber | 2.3k |

### 8. Art & Drawing Apps

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Pocket Paint** | A robust drawing application featuring advanced layers, transparency, and filters. | https://github.com/Catrobat/Paintroid | 700 |
| **Fossify Paint** | A sleek and purely offline app tailored for quick sketches and doodling ideas. | https://github.com/FossifyOrg/Paint | 200 |
| **PxerStudio** | A specialized workspace and drawing tool designed explicitly for mobile pixel art. | https://github.com/BennyKok/PxerStudio | 300 |
| **Infinipaint** | An exploratory drawing canvas featuring infinite spatial constraints and zooming. | https://github.com/ErrorAtLine0/infinipaint | 100 |
| **Tux Paint** | A widely acclaimed open-source raster drawing program ported for younger mobile users. | https://github.com/tuxpaint/tuxpaint-android | 150 |

### 9. Alternative Social Media (Nostr, Lemmy, etc.)

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **Amethyst** | The premier, highly-polished Nostr social network client designed for Android devices. | https://github.com/vitorpamplona/amethyst | 1.9k |
| **Jerboa** | A natively built, modern client application for the decentralized Lemmy platform. | https://github.com/dessalines/jerboa | 1.6k |
| **Fedilab** | A customizable multi-account client supporting Mastodon, Pleroma, and Peertube. | https://github.com/tom79/Fedilab | 1.0k |
| **Infinity for Reddit** | A highly customizable and aesthetically pleasing open-source front-end for Reddit. | https://github.com/Docile-Alligator/Infinity-For-Reddit | 7.0k |
| **Squawker** | An alternative, open-source front-end designed to browse Twitter/X anonymously. | https://github.com/j-hc/squawker | 1.5k |

### 10. System Monitoring & Benchmark

| App Name | Description | GitHub Repo Link | Approx Stars |
|---|---|---|---|
| **CPU Info** | A comprehensive hardware and software information utility providing deep device statistics. | https://github.com/kgurgul/cpuinfo | 1.5k |
| **AnotherMonitor** | Tracks and visualizes CPU and memory usage of the system and individual background tasks. | https://github.com/aattz/AnotherMonitor | 400 |
| **System Monitor** | An all-in-one monitor for tracking Wi-Fi, sensors, battery, CPU, RAM, and background tasks. | https://github.com/fg2014/SystemMonitor | 200 |
| **RTMON** | A retro-aesthetic widget providing real-time statistics on device processing and network usage. | https://github.com/n1th1n-19/RTMON | 150 |
| **Running Services** | A streamlined utility app that specifically focuses on viewing background Android services. | https://github.com/biplobsd/running_services_monitor | 50 |
"""

categories = re.findall(r'### \d+\. (.*?)\n(.*?)(?=\n### |\Z)', new_apps_markdown, re.DOTALL)

with open("README.md", "r") as f:
    main_readme = f.read()

# Remove the old footer to append the new list and then add the new footer
main_readme_body = main_readme.split("---\n\n<div align=\"center\">")[0]

start_idx = 55
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

# Update the badge to say 320+ Apps
main_readme_body = main_readme_body.replace("Apps-270+-00FF41", "Apps-320+-00FF41")

with open("README.md", "w") as f:
    f.write(main_readme_body)

print(f"Successfully added {len(categories)} new categories and updated main README.")
