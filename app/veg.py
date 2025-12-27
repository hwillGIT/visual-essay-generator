import sys
import os
import json
import time
import textwrap

# Ensure we can import from tools/
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

# Mock imports for now until we move logic or import properly
# from series_generator import generate_series

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("==================================================")
    print("      VISUAL ESSAY GENERATOR (VEG v2.0)           ")
    print("           Interactive CLI Automation             ")
    print("==================================================")
    print("")

def main_menu():
    clear_screen()
    print_header()
    print("What would you like to do?")
    print("1. [New] Create a Single Visual Essay from Topic")
    print("2. [Series] Generate a Series from a Spec File")
    print("3. [PDF] Process a PDF (Simulated Extraction)")
    print("4. [Lint] Validate an Existing Blueprint")
    print("5. [Render] Generate Image Prompts from Blueprint")
    print("6. Exit")
    print("")
    
    choice = input("Select an option (1-6): ").strip()
    return choice

def flow_new_essay():
    clear_screen()
    print_header()
    print("--- NEW VISUAL ESSAY ---")
    topic = input("Enter your topic or concept: ").strip()
    
    print("\nSelect a Motif Style:")
    styles = ["Atlas", "Mythic", "Systems", "Sketchbook", "Didactic"]
    for i, s in enumerate(styles):
        print(f"{i+1}. {s}")
    
    style_idx = input(f"Choose style (1-{len(styles)}): ").strip()
    try:
        selected_style = styles[int(style_idx)-1]
    except:
        selected_style = "Atlas" # Default
        
    print(f"\nConfiguration: Topic='{topic}', Style='{selected_style}'")
    print("\n[System] Generating Operator Prompt...")
    time.sleep(1)
    
    # In a real app, this would call the LLM API. 
    # Here we generate the Prompt File for the user to paste.
    
    prompt_content = f"""
# VEG AUTO-GENERATED PROMPT

**Role**: Operator
**Task**: Create Visual Essay Blueprint
**Topic**: {topic}
**Target Motif**: {selected_style}

[INSTRUCTION]
1. Generate a Blueprint for the topic above.
2. Ensure it has 4-6 slides.
3. Use the '{selected_style}' motif logic.
4. Output the Markdown code block.
"""
    
    filename = f"out/draft_{topic.replace(' ','_')[:20]}.md"
    os.makedirs("out", exist_ok=True)
    with open(filename, "w") as f:
        f.write(prompt_content)
        
    print(f"\n[Success] Prompt generated at: {filename}")
    print("Next Step: Paste this file content into Gemini to get your Blueprint.")
    input("\nPress Enter to return...")

def flow_series():
    clear_screen()
    print_header()
    print("--- SERIES GENERATOR ---")
    print("Checking for spec files in examples/series/...")
    
    # List files
    series_dir = "examples/series"
    if not os.path.exists(series_dir):
        print(f"Error: Directory {series_dir} not found.")
        input("Press Enter...")
        return

    files = [f for f in os.listdir(series_dir) if f.endswith('.json') or f.endswith('.yaml')]
    
    if not files:
        print("No spec files found.")
        return

    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
        
    choice = input(f"\nSelect spec file (1-{len(files)}): ").strip()
    try:
        target_file = os.path.join(series_dir, files[int(choice)-1])
    except:
        print("Invalid selection.")
        return

    print(f"\nProcessing {target_file}...")
    # Call the existing tool logic (using os.system for simplicity in this proto)
    cmd = f"python tools/series_generator.py {target_file}"
    os.system(cmd)
    
    print("\n[Success] Series prompts generated.")
    input("Press Enter to return...")

def flow_pdf_ingest():
    clear_screen()
    print_header()
    print("--- PDF INGESTION (Simulated) ---")
    print("Note: Direct PDF reading requires additional libraries (PyPDF2/NotebookLM API).")
    print("This mode creates a 'Research Prompt' for you to paste into Gemini alongside your PDF upload.")
    
    pdf_path = input("\nEnter path to PDF (optional, just for naming): ").strip()
    
    print("\n[System] creating NotebookLM Ingestion Prompt...")
    
    prompt = """
# PDF VISUAL EXTRACTION PROMPT

**Task**: Analyze the uploaded PDF.
**Output**: A 'Visual Essay Structure' containing:
1. Core Thesis (1 sentence)
2. 3 Visual Metaphors found in the text.
3. 5 Key Quotes suitable for slides.
4. A proposed 'Narrative Spine' (Beginning -> Middle -> End).

[CONSTRAINT]
Do not summarize the whole PDF. Focus purely on extracting *visual* and *structural* elements for a slide deck.
"""
    
    out_file = "out/pdf_ingestion_prompt.md"
    os.makedirs("out", exist_ok=True)
    with open(out_file, "w") as f:
        f.write(prompt)
        
    print(f"\n[Success] Ingestion prompt saved to: {out_file}")
    print("Action: Upload your PDF to Gemini/NotebookLM and paste this prompt.")
    input("Press Enter to return...")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            flow_new_essay()
        elif choice == '2':
            flow_series()
        elif choice == '3':
            flow_pdf_ingest()
        elif choice == '4':
            print("\n[Info] To lint, run: python tools/blueprint_linter.py <file>")
            input("Press Enter...")
        elif choice == '5':
            print("\n[Info] To render, paste your Blueprint back into Gemini with the '/render' command.")
            input("Press Enter...")
        elif choice == '6':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    main()
