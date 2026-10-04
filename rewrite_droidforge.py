import os
import glob

colors = ["00FF41", "FF007F", "00E5FF", "FFD700", "B533FF", "FF5733", "33FF57", "3357FF", "F033FF"]

# Read the main README to get the list of folders
with open("README.md", "r") as f:
    main_readme = f.read()

folders = [d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()]

for folder in folders:
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        continue
        
    with open(readme_path, "r") as f:
        content = f.read()
    
    # Extract name and table
    try:
        name = content.split("## 📱 ")[1].split("\n")[0].strip()
        table = content.split("## 📱 " + name + "\n\n")[1].split("<br>")[0].strip()
    except Exception as e:
        print(f"Error parsing {folder}: {e}")
        continue
        
    import random
    color = random.choice(colors)
    
    url_name = name.replace(' ', '%20').replace('&', '%26')
    
    new_content = f"""<div align="center" id="top">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,100:{color}&height=120&section=header&text={url_name}&fontSize=40&fontColor={color}&animation=fadeIn&fontAlignY=40" width="100%" alt="Header" />
  
  <br>
  
  <a href="https://github.com/krishkumarcodes/awesome-android-foss">
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
  <p><strong>⭐ If you found these apps useful, please give the <a href="https://github.com/krishkumarcodes/awesome-android-foss">main repository</a> a STAR! ⭐</strong></p>
</div>
"""
    with open(readme_path, "w") as f:
        f.write(new_content)

print(f"Rewrote {len(folders)} sub-readmes with new minimal animated design.")
