from flask import Flask, render_template, request, jsonify
import os
import sys
import glob
from datetime import datetime

# Add tools to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

app = Flask(__name__)

# Helper to read text
def load_text(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read()
    return ""

# Helper to load motif
def load_motif(motif_name):
    # Map friendly name to filename
    path = os.path.join(os.path.dirname(__file__), f"../skill/motifs/{motif_name.lower()}.style.md")
    return load_text(path)

@app.route('/')
def index():
    return render_template('index.html')

def load_metaphor(metaphor_name):
    if not metaphor_name or metaphor_name == "None (Auto)":
        return ""
    path = os.path.join(os.path.dirname(__file__), f"../skill/metaphors/{metaphor_name.lower()}.md")
    return load_text(path)

@app.route('/api/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    topic = data.get('topic')
    motif = data.get('motif')
    metaphor = data.get('metaphor', 'None (Auto)')
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    motif_content = load_motif(motif)
    metaphor_content = load_metaphor(metaphor)
    
    metaphor_instr = f"3. Apply the **{metaphor}** conceptual mappings (see below)." if metaphor != "None (Auto)" else "3. Choose an appropriate conceptual metaphor."
    metaphor_section = f"\n## CONTEXT: METAPHOR ({metaphor})\n{metaphor_content}\n" if metaphor_content else ""

    prompt = f"""# VEG OPERATOR PROMPT
# Generated: {timestamp}
# Topic: {topic}
# Motif: {motif}
# Metaphor: {metaphor}

You are the **Visual Essay Generator (VEG) Operator**.

**Mission**:
1. Create a "Visual Essay Blueprint" for the topic: "{topic}".
2. Use the **{motif}** visual motif logic (see below).
{metaphor_instr}
4. Follow the strict "LOCKED" block format for text integrity.

---

## CONTEXT: MOTIF ({motif})
{motif_content}
{metaphor_section}
## INSTRUCTION
Generate a Stage 1 Blueprint with 4-6 slides. 
Ensure the "Visual Anchor" for each slide aligns with the {motif} aesthetic and {metaphor if metaphor != "None (Auto)" else "chosen"} metaphor.
"""
    return jsonify({"prompt": prompt})

@app.route('/api/lint', methods=['POST'])
def lint_blueprint():
    data = request.json
    blueprint = data.get('blueprint', '')
    errors = []
    
    if "HEADING (LOCKED):" not in blueprint:
        errors.append("❌ Missing 'HEADING (LOCKED):' blocks.")
    if "BODY TEXT (LOCKED):" not in blueprint:
        errors.append("❌ Missing 'BODY TEXT (LOCKED):' blocks.")
    if "—" in blueprint:
        errors.append("⚠️ Found em-dashes (—). Replace with hyphens.")
    if "…" in blueprint:
        errors.append("⚠️ Found ellipses (…). Replace with '...'.")
        
    status = "valid" if not errors else "invalid"
    return jsonify({"status": status, "errors": errors})

@app.route('/api/get_pdf_instruction', methods=['GET'])
def get_pdf_instruction():
    path = os.path.join(os.path.dirname(__file__), "../skill/notebooklm/instruction_note_master.md")
    return jsonify({"instruction": load_text(path)})

if __name__ == '__main__':
    # Replit usually runs on port 8080 or 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
