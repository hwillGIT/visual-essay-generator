import os
import sys

def check_structure():
    required_files = [
        "skills/visual-essay-skill/README.md",
        "skills/visual-essay-skill/Makefile",
        "skills/visual-essay-skill/tools/series_generator.py",
        "skills/visual-essay-skill/skill/prompts/mega_prompt_operator_mode.md"
    ]
    
    missing = []
    for f in required_files:
        if not os.path.exists(f):
            missing.append(f)
            
    if missing:
        print("Doctor: FAILED")
        print("Missing critical files:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("Doctor: PASS")
        print("Visual Essay Skill is healthy.")
        sys.exit(0)

if __name__ == "__main__":
    check_structure()
