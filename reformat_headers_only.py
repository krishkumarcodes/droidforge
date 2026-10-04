import os
import random
import urllib.parse

shapes = ["waving", "wave", "rect", "rounded", "cylinder", "soft", "transparent", "slice"]

folders = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()])

for folder in folders:
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        continue
        
    with open(readme_path, "r") as f:
        content = f.read()
    
    try:
        name = content.split("> **✨ ")[1].split("** - *")[0].strip()
        table = content.split("*Carefully curated list of the best FOSS alternatives.*")[1].split("\n---\n<div align=\"center\">")[0].strip()
    except Exception as e:
        print(f"Failed to parse {folder}: {e}")
        continue
        
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
        
print(f"Successfully rewritten {len(folders)} headers and footers while preserving the table.")
