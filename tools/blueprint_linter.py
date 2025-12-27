import re
import sys
import os

def lint_blueprint(filepath):
    print(f"Linting: {filepath}")
    with open(filepath, 'r') as f:
        content = f.read()

    errors = []
    
    # 1. Check for LOCKED blocks
    headings = re.findall(r'HEADING \(LOCKED\):\s*\n(.*?)\n', content, re.DOTALL)
    bodies = re.findall(r'BODY TEXT \(LOCKED\):\s*\n(.*?)\n', content, re.DOTALL)

    if not headings:
        errors.append("ERROR: No HEADING (LOCKED) blocks found.")
    if not bodies:
        errors.append("ERROR: No BODY TEXT (LOCKED) blocks found.")

    if len(headings) != len(bodies):
        errors.append(f"ERROR: Mismatch in block counts. Headings: {len(headings)}, Bodies: {len(bodies)}.")

    # 2. Validate Headings
    for i, h in enumerate(headings):
        h = h.strip()
        if len(h) > 80:
            errors.append(f"WARNING: Heading {i+1} is too long ({len(h)} chars). Max 80.")

    # 3. Validate Bodies
    for i, b in enumerate(bodies):
        b = b.strip()
        # Check for risky punctuation
        if '—' in b:
            errors.append(f"WARNING: Body {i+1} contains em-dash (—). Use hyphen (-).")
        if '…' in b:
            errors.append(f"WARNING: Body {i+1} contains ellipsis (…). Use '...'.")
        if '“' in b or '”' in b:
            errors.append(f"WARNING: Body {i+1} contains smart quotes. Use straight quotes.")
        
        # Check for double spaces
        if '  ' in b:
            errors.append(f"WARNING: Body {i+1} contains double spaces.")

    if errors:
        for e in errors:
            print(e)
        return False
    else:
        print("PASS: Blueprint looks good.")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python blueprint_linter.py <path_to_blueprint>")
        sys.exit(1)
    
    lint_blueprint(sys.argv[1])
