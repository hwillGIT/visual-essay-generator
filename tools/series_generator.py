import json
import sys
import os
import shutil

def generate_series(json_path):
    print(f"Reading spec from: {json_path}")
    with open(json_path, 'r') as f:
        spec = json.load(f)

    series_title = spec.get('series_title', 'Untitled_Series').replace(' ', '_')
    motif = spec.get('motif', 'Atlas')
    
    # Create specific output directory as requested
    output_dir = os.path.join('skills/visual-essay-skill/out', series_title)
    
    # Ensure parent dir exists
    os.makedirs(os.path.dirname(output_dir), exist_ok=True)
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    print(f"Generating series: {series_title} ({len(spec['essays'])} essays) in {output_dir}")

    for i, essay in enumerate(spec['essays']):
        title = essay['title']
        concept = essay['concept']
        safe_title = title.replace(' ', '_').replace('/', '-').replace(':', '')
        
        filename = f"{i+1:02d}_{safe_title}.prompt.md"
        filepath = os.path.join(output_dir, filename)

        content = f"""# Operator Prompt for Essay {i+1}: {title}

**Series**: {series_title}
**Motif**: {motif}
**Concept**: {concept}

---

## Instructions for the AI
1.  Read the **Stage 1 Blueprint Generator** prompt.
2.  Use the concept above as your INPUT.
3.  Generate a blueprint titled "{title}".
4.  Once the blueprint is generated and approved, apply the **{motif}** motif using the **Stage 2 Renderer**.

"""
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"  Created: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python series_generator.py <path_to_json_spec>")
        sys.exit(1)
    
    generate_series(sys.argv[1])
