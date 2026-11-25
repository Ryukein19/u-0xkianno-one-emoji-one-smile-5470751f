import os
# One-emoji entry: the emoji below is the entire submission.
# Writes the emoji to /output/entry.txt.
LINE = "😏"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
