import streamlit as st
import os
import sys
import json
import yaml
import glob
from datetime import datetime

# Add tools directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

# Import tool logic (if available, otherwise we reimplement for the UI)
try:
    from series_generator import generate_series
except ImportError:
    pass # We will handle this with direct calls if module import fails

st.set_page_config(
    page_title="VEG v2.0 Operator",
    page_icon="🎨",
    layout="wide"
)

def load_text(path):
    with open(path, 'r') as f:
        return f.read()

def main():
    st.title("🎨 Visual Essay Generator (VEG v2.0)")
    st.markdown("Automated pipeline for generating structured visual narratives.")

    # Sidebar Navigation
    st.sidebar.header("Workflow Phase")
    mode = st.sidebar.radio(
        "Choose Action:",
        ["1. New Essay (Topic)", "2. Series Generator", "3. PDF Extraction", "4. Blueprint Linter"]
    )

    st.sidebar.divider()
    st.sidebar.info(
        "**Workflow Tip**:\n"
        "1. Generate Prompt here.\n"
        "2. Copy-Paste into Gemini.\n"
        "3. Copy Gemini output to Local File.\n"
        "4. Lint/Render."
    )

    # --- MODE 1: NEW ESSAY ---
    if mode == "1. New Essay (Topic)":
        st.header("1. Create New Visual Essay")
        st.write("Generate the **Operator Prompt** for a single essay topic.")
        
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Enter Topic/Concept:", placeholder="e.g. The Philosophy of Water")
        with col2:
            motif = st.selectbox("Select Visual Style (Motif):", ["Atlas", "Mythic", "Systems", "Sketchbook", "Didactic"])
            metaphor = st.selectbox("Select Conceptual Metaphor:", ["None (Auto)", "Nature", "Architecture", "Machine", "Alchemy", "Business"])
        
        if st.button("Generate Operator Prompt", type="primary"):
            if not topic:
                st.error("Please enter a topic.")
            else:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Load Metaphor context if selected
                metaphor_context = ""
                if metaphor != "None (Auto)":
                    meta_path = os.path.join(os.path.dirname(__file__), f"../skill/metaphors/{metaphor.lower()}.md")
                    if os.path.exists(meta_path):
                        with open(meta_path, 'r') as f:
                            metaphor_context = f"\n## CONTEXT: METAPHOR ({metaphor})\n{f.read()}\n"

                prompt = f"""
# VEG OPERATOR PROMPT
# Generated: {timestamp}
# Topic: {topic}
# Motif: {motif}
# Metaphor: {metaphor}

You are the **Visual Essay Generator (VEG) Operator**.

**Mission**:
1. Create a "Visual Essay Blueprint" for the topic: "{topic}".
2. Use the **{motif}** visual motif logic (see below).
{f"3. Apply the **{metaphor}** conceptual mappings (see below)." if metaphor != "None (Auto)" else "3. Choose an appropriate conceptual metaphor."}
4. Follow the strict "LOCKED" block format for text integrity.

---

## CONTEXT: MOTIF ({motif})
(Paste the contents of skills/visual-essay-skill/skill/motifs/{motif.lower()}.style.md here)
{metaphor_context}
## INSTRUCTION
Generate a Stage 1 Blueprint with 4-6 slides. 
Ensure the "Visual Anchor" for each slide aligns with the {motif} aesthetic and {metaphor if metaphor != "None (Auto)" else "chosen"} metaphor.
"""
                st.success("Prompt Generated!")
                st.code(prompt, language="markdown")
                st.caption("Copy this block and paste it into your Gemini/LLM chat.")

    # --- MODE 2: SERIES GENERATOR ---
    elif mode == "2. Series Generator":
        st.header("2. Series Generator")
        st.write("Generate prompts for an entire season (10+ essays) from a single Spec File.")
        
        # Scan for example files
        example_dir = os.path.join(os.path.dirname(__file__), "../examples/series")
        example_files = glob.glob(os.path.join(example_dir, "*.json")) + glob.glob(os.path.join(example_dir, "*.yaml"))
        example_names = [os.path.basename(f) for f in example_files]
        
        tab1, tab2 = st.tabs(["Select Existing Spec", "Upload New Spec"])
        
        selected_file = None
        
        with tab1:
            if example_names:
                choice = st.selectbox("Choose an Example Spec:", example_names)
                if choice:
                    selected_file = os.path.join(example_dir, choice)
                    with st.expander("Preview Spec Content"):
                        st.code(load_text(selected_file))
            else:
                st.warning("No example specs found.")

        with tab2:
            uploaded = st.file_uploader("Upload .json or .yaml spec", type=["json", "yaml"])
            if uploaded:
                # Save temp file
                selected_file = os.path.join("out", uploaded.name)
                os.makedirs("out", exist_ok=True)
                with open(selected_file, "wb") as f:
                    f.write(uploaded.getbuffer())
                st.success(f"Loaded {uploaded.name}")

        if st.button("Generate Series Prompts", type="primary"):
            if selected_file:
                # Run the tool script via subproccess or direct import
                # We use os.system to ensure environment consistency for now
                cmd = f"python3 {os.path.join(os.path.dirname(__file__), '../tools/series_generator.py')} {selected_file}"
                os.system(cmd)
                
                # Check output
                # Assuming the script writes to ../out/<series_title>
                # We need to find where it wrote.
                st.success("Generation Complete! Files written to `out/` folder.")
                
                # Show generated files
                st.write("### Generated Prompts:")
                # Simple list of recent files in out/
                out_root = os.path.join(os.path.dirname(__file__), "../out")
                if os.path.exists(out_root):
                    series_dirs = os.listdir(out_root)
                    for d in series_dirs:
                        d_path = os.path.join(out_root, d)
                        if os.path.isdir(d_path):
                            st.write(f"📂 **{d}**")
                            files = os.listdir(d_path)
                            for f in files:
                                st.text(f"  📄 {f}")
            else:
                st.error("Please select or upload a spec file.")

    # --- MODE 3: PDF EXTRACTION ---
    elif mode == "3. PDF Extraction":
        st.header("3. PDF to Visual Essay")
        st.write("Convert a PDF/Article into a Visual Essay structure.")
        
        st.info("Step 1: Upload your PDF to **NotebookLM** or attach it to **Gemini 1.5 Pro**.")
        st.info("Step 2: Copy the instruction below and paste it as the prompt.")
        
        st.divider()
        
        master_instruction_path = os.path.join(os.path.dirname(__file__), "../skill/notebooklm/instruction_note_master.md")
        if os.path.exists(master_instruction_path):
            instruction = load_text(master_instruction_path)
            st.text_area("Master Instruction (Copy this):", value=instruction, height=400)
        else:
            st.error("Instruction template not found.")

    # --- MODE 4: LINTER ---
    elif mode == "4. Blueprint Linter":
        st.header("4. Blueprint Validator")
        st.write("Check your generated Blueprint for errors before rendering.")
        
        blueprint_text = st.text_area("Paste your Blueprint Markdown here:", height=300)
        
        if st.button("Validate Blueprint"):
            if not blueprint_text:
                st.error("Paste text first.")
            else:
                # Simple in-memory lint
                errors = []
                if "HEADING (LOCKED):" not in blueprint_text:
                    errors.append("❌ Missing 'HEADING (LOCKED):' blocks.")
                if "BODY TEXT (LOCKED):" not in blueprint_text:
                    errors.append("❌ Missing 'BODY TEXT (LOCKED):' blocks.")
                if "—" in blueprint_text:
                    errors.append("⚠️ Found em-dashes (—). Replace with hyphens.")
                if "…" in blueprint_text:
                    errors.append("⚠️ Found ellipses (…). Replace with '...'.")
                
                if errors:
                    for e in errors:
                        st.error(e)
                else:
                    st.success("✅ Blueprint looks good! Ready for Rendering.")

if __name__ == "__main__":
    main()
