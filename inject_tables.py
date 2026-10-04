import os
import subprocess

folders = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()])

for folder in folders:
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        continue
    
    # 1. Get the old table from git
    try:
        old_content = subprocess.check_output(['git', 'show', f'e58bb82:{readme_path}']).decode('utf-8')
        old_table_part = old_content.split("*Carefully curated list of the best FOSS alternatives.*")[1]
        table = old_table_part.rsplit("---", 1)[0].strip()
    except Exception as e:
        print(f"Failed to extract table from e58bb82 for {folder}: {e}")
        continue
        
    # 2. Read the current file
    with open(readme_path, "r") as f:
        current = f.read()
        
    # 3. Replace the broken table
    try:
        head, tail = current.split("*Carefully curated list of the best FOSS alternatives.*")
        _, after_table = tail.split("---", 1)
        new_content = head + "*Carefully curated list of the best FOSS alternatives.*\n\n" + table + "\n\n---" + after_table
    except Exception as e:
        print(f"Failed to patch {folder}: {e}")
        continue
        
    # 4. Write it back
    with open(readme_path, "w") as f:
        f.write(new_content)
        
print(f"Successfully restored tables into {len(folders)} folders while preserving headers.")
