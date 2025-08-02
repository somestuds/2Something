import re

with open("./readme.md", "r", encoding="utf-8") as f:
    text = f.read()

age = 14  # replace with your test age
text = re.sub(r'(<!-- _startage -->).*?(<!-- _endage -->)', rf'\1 {age} \2', text, flags=re.S)

with open("./readme.md", "w", encoding="utf-8") as f:
    f.write(text)