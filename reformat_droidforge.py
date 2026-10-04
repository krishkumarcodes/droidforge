import os
import glob
import random
import urllib.parse
import re

emojis = ["🚀", "📱", "🌐", "💬", "🐦", "📧", "🎵", "🎬", "🎙️", "📂", "🖼️", "📸", "📝", "⛅", "⌨️", "✨", "🗺️", "🔐", "🛡️", "🚫", "⬇️", "📄", "💼", "📅", "💪", "📰", "🔑", "🔄", "💻", "⚙️", "🎓", "🎮", "📚", "🍿", "📖", "💰", "🔍", "📋", "🎨", "🖼️", "🏪", "🔓", "🎥", "🤖", "📡", "🧰", "🕹️", "🏠", "🔭", "🧮", "🧩", "🧘", "🚆", "🥗", "🎧", "🛠️"]

shapes = ["waving", "wave", "rect", "rounded", "cylinder", "soft", "transparent", "slice"]

folders = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()])

# 1. Fix all subfolders and extract data for the table
category_data = []

for folder in folders:
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        continue
        
    with open(readme_path, "r") as f:
        content = f.read()
    
    try:
        name = content.split("> **✨ ")[1].split("** - *")[0].strip()
        table = content.split("*Carefully curated list of the best FOSS alternatives.*")[1].split("---")[0].strip()
        app_count = table.count('\n') - 1 # Approx apps
    except Exception as e:
        print(f"Error parsing {folder}: {e}")
        continue
        
    # Pick a random emoji for this category
    emoji = random.choice(emojis)
    category_data.append((name, folder, app_count, emoji))
    
    # Generate random bright hex color
    color = f"{random.randint(100, 255):02X}{random.randint(100, 255):02X}{random.randint(100, 255):02X}"
    shape = random.choice(shapes)
    
    url_name = urllib.parse.quote(name)
    url_desc = urllib.parse.quote("Curated Open Source Alternatives")
    
    new_content = f"""<div align="center" id="top">
  <img src="https://capsule-render.vercel.app/api?type={shape}&color=0:0D1117,100:{color}&height=150&section=header&text={url_name}&fontSize=40&fontColor={color}&animation=fadeIn&fontAlignY=35&desc={url_desc}&descSize=15&descAlignY=60&descAlign=50&stroke={color}&strokeWidth=1" width="100%" alt="Header" />
  
  <br>
  
  <a href="https://github.com/krishkumarcodes/droidforge">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3000&pause=1000&color={color}&center=true&vCenter=true&width=500&lines=Explore+the+best+open-source+apps;Handpicked+for+your+privacy;Ditch+the+bloatware;Forge+your+Android+experience" alt="Typing Animation" />
  </a>
</div>

<br>

> **✨ {name}** - *Carefully curated list of the best FOSS alternatives.*

{table}

---
<div align="center">
  <p><kbd> <a href="../README.md">⬅️ Return to Main Directory</a> </kbd> &nbsp;|&nbsp; <kbd> <a href="#top">⬆️ Back to Top</a> </kbd></p>
  <br>
  <p><strong>⭐ If you found these apps useful, please give the <a href="https://github.com/krishkumarcodes/droidforge">main repository</a> a STAR! ⭐</strong></p>
</div>
"""
    with open(readme_path, "w") as f:
        f.write(new_content)

print(f"Fixed {len(category_data)} sub-folder headers with super-enhanced designs.")

# 2. Update the main README with a 2-column table
with open("README.md", "r") as f:
    main_readme = f.read()

# Slice out the old category list
header_part = main_readme.split("## 📁 App Categories")[0]
footer_part = main_readme.split("---")[-2] # Get the second to last rule (before footer)
footer_part = "---\n" + main_readme.split("---")[-1] # the actual footer

new_main_readme = header_part + "## 📁 App Categories\n\n| 🗂️ Category | 🗂️ Category |\n|:---|:---|\n"

for i in range(0, len(category_data), 2):
    cat1 = category_data[i]
    col1 = f"{cat1[3]} [**{cat1[0]}**](./{cat1[1]}/) `<{cat1[2]} apps>`"
    
    if i + 1 < len(category_data):
        cat2 = category_data[i+1]
        col2 = f"{cat2[3]} [**{cat2[0]}**](./{cat2[1]}/) `<{cat2[2]} apps>`"
    else:
        col2 = ""
        
    new_main_readme += f"| {col1} | {col2} |\n"

new_main_readme += "\n<br>\n\n" + footer_part

with open("README.md", "w") as f:
    f.write(new_main_readme)

print("Main README updated with 2-column table.")
