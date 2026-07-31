#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CURRICULUM_PATH = os.path.join(BASE_DIR, "curriculum.json")
PROGRESS_PATH = os.path.join(BASE_DIR, "progress.json")
TITLE_OUT = os.path.join(BASE_DIR, "issue_title.txt")
BODY_OUT = os.path.join(BASE_DIR, "issue_body.txt")

def main():
    if not os.path.exists(CURRICULUM_PATH) or not os.path.exists(PROGRESS_PATH):
        print("Error: Required files not found.")
        return

    with open(CURRICULUM_PATH, "r") as f:
        curriculum = json.load(f)["curriculum"]

    with open(PROGRESS_PATH, "r") as f:
        progress = json.load(f)

    day = progress.get("current_day", 1)
    day_key = str(day)

    # Wrap around if done
    if day_key not in curriculum:
        day = 1
        day_key = "1"

    lesson = curriculum[day_key]

    # Generate title
    title = f"📚 Day {day_key}: {lesson['title']}"
    
    # Generate body in markdown with checklist format
    body = f"""# Daily Study: {lesson['title']}
**Category**: `{lesson['category']}` | **Expected Duration**: 30 Minutes

---

## 💡 Core Concept
{lesson['concept']}

---

## 🔍 Study & Research (15 minutes)
- [ ] Read or watch: **{lesson['study_material']}**
- [ ] Take notes of key concepts or terms.

---

## 🛠️ Practical Challenge (15 minutes)
- [ ] Complete this hands-on exercise:
  {lesson['practical_challenge']}

---

### 📝 Solution & Notes
*(Optional: Edit this issue and write your solution, output, or notes here!)*

---
*Close this issue once you have completed today's study. Keep up the great work!*
"""

    # Write output files
    with open(TITLE_OUT, "w") as f:
        f.write(title)

    with open(BODY_OUT, "w") as f:
        f.write(body)

    print(f"Generated files for {title}")

    # Advance progress
    progress["current_day"] = day + 1
    with open(PROGRESS_PATH, "w") as f:
        json.dump(progress, f, indent=2)

if __name__ == "__main__":
    main()
