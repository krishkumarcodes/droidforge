import os
import re
import urllib.parse
import urllib.request
import json
import time

def fetch_repo_info(repo_url):
    parts = repo_url.rstrip('/').split('/')
    if len(parts) >= 2:
        owner, repo = parts[-2], parts[-1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        try:
            req = urllib.request.Request(api_url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            response = urllib.request.urlopen(req)
            data = json.loads(response.read().decode('utf-8'))
            return {
                "latest_release_url": f"{repo_url}/releases/latest",
                "images": [data.get('owner', {}).get('avatar_url', '')]
            }
        except Exception as e:
            return None
    return None

def process_folder(folder_path):
    print(f"Processing {folder_path}...")
    readme_path = os.path.join(folder_path, "README.md")
    if not os.path.exists(readme_path): return

    with open(readme_path, "r") as f:
        content = f.read()

    table_rows = re.findall(r'\| \*\*(.*?)\*\* \| (.*?) \| (https?://github\.com/[^\s\|]+) \|.*?\|', content)

    for app_name, desc, repo_link in table_rows:
        safe_app_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', app_name)
        app_dir = os.path.join(folder_path, safe_app_name)
        os.makedirs(app_dir, exist_ok=True)
        
        info = fetch_repo_info(repo_link)
        download_link = info['latest_release_url'] if info else repo_link
        img_tags = ""
        if info and info['images']:
            for img in info['images']:
                if img:
                    img_tags += f'  <img src="{img}" width="300" style="margin: 10px;" />\n'
        
        app_readme = f"""<div align="center" id="top">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00FF41&height=120&section=header&text={urllib.parse.quote(app_name)}&fontSize=40&fontColor=00FF41&animation=fadeIn&fontAlignY=40" width="100%" />
</div>

<br>

<div align="center">
  <h2>{app_name}</h2>
  <p><em>{desc}</em></p>
</div>

---

### 📥 Download & Source
- **Source Code:** [{repo_link}]({repo_link})
- **Download:** [Get Latest Release]({download_link})

---

### 🖼️ Overview & Screenshots

<div align="center">
{img_tags}
</div>

---
<div align="center">
  <p><kbd> <a href="../README.md">⬅️ Back to Category</a> </kbd> &nbsp;|&nbsp; <kbd> <a href="#top">⬆️ Back to Top</a> </kbd></p>
</div>
"""
        with open(os.path.join(app_dir, "README.md"), "w") as f:
            f.write(app_readme)
        
        time.sleep(0.5)

import glob
folders = glob.glob("[6][5-9]-*")
folders.sort()
for f in folders:
    if os.path.isdir(f):
        process_folder(f)
