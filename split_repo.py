import os
import re
import random

colors = ["00FF41", "FF007F", "00E5FF", "FFD700", "B533FF", "FF5733", "33FF57", "3357FF", "F033FF"]

with open("README.md", "r") as f:
    content = f.read()

# Split into header, body, footer
header_split = content.split("---", 1)
header = header_split[0]
body_and_footer = header_split[1].rsplit("---", 1)
body = body_and_footer[0]

categories = re.findall(r'### (\d+)\. (.*?)\n(.*?)(?=\n### |\Z)', body, re.DOTALL)

main_readme = header + "---\n\n## 📁 App Categories\n\n"

for num, name, table in categories:
    folder_name = f"{int(num):02d}-{name.replace(' ', '_').replace('&', 'and').replace('/', '_')}"
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
    
    main_readme += f"- [**{name}**](./{folder_name}/) ({table.count('|') // 6 - 1} apps)\n"

main_readme += """
---

<div align="center">
  <p><strong>⭐ If you found this repository useful, please give it a STAR! ⭐</strong></p>
  <p>Forged by <strong>Krish Kumar</strong></p>
  <a href="https://github.com/krishkumarcodes">
    <img src="https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=00FF41" alt="GitHub" />
  </a>
</div>
"""

with open("README.md", "w") as f:
    f.write(main_readme)

print(f"Successfully processed {len(categories)} categories.")
