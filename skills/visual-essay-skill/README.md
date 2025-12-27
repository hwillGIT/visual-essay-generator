# Visual Essay Skill (VEG v1.0)

This repository module contains the complete toolset for the Visual Essay Generator (VEG). It is designed to transform abstract concepts or raw notes into high-quality, visually structured essays suitable for posting on social media, blogs, or internal knowledge bases.

## Overview

The VEG workflow consists of two main stages, guided by specific prompts and templates:

1.  **Stage 1: Blueprint Generation**: Converts raw ideas, notes, or a topic into a structured "Blueprint". This blueprint defines the core thesis, narrative arc, and exactly what text and visuals go where.
2.  **Stage 2: Rendering**: Takes the Blueprint and a specific "Motif" (visual style) to generate the final output (e.g., Midjourney prompts + final copy).

## 🌍 Web Interface (Replit / Flask)

If you are running on **Replit** (or prefer a standard Web Server), use the Flask app:

1.  **Run Command**:
    ```bash
    python3 skills/visual-essay-skill/app/replit_app.py
    ```
2.  **Access**: Open the Webview/Preview pane.
3.  **Features**:
    *   **New Essay**: Generate prompts instantly.
    *   **PDF Extraction**: Get the NotebookLM instruction.
    *   **Linter**: Paste your Markdown to validate blocks.

*(Note: The `replit.nix` file is included for instant configuration on Replit.)*

---

## 🖥️ Streamlit Interface (Local)

The best way to use VEG locally is via the **Streamlit Web App**. It provides a visual interface for all workflows without needing to memorize commands.

1.  Run the app:
    ```bash
    streamlit run skills/visual-essay-skill/app/streamlit_app.py
    ```
2.  Open your browser to the local URL (usually `http://localhost:8501`).
3.  Choose your mode:
    *   **New Essay**: Generate copy-paste prompts for Gemini.
    *   **Series Generator**: Process batch specs visually.
    *   **PDF Extraction**: Get the specialized prompts for NotebookLM.
    *   **Linter**: Paste your blueprint to validate it instantly.

---

## ⚡ CLI Tool (Alternative)

If you prefer the terminal:

```bash
python3 skills/visual-essay-skill/app/veg.py
```

---

## 📚 Manual Workflow (Advanced)

If you prefer running individual scripts:

**[Read the Step-by-Step WORKFLOW GUIDE here](guides/WORKFLOW.md)**

The guide covers:
1.  Setting up the Operator Chat session.
2.  Generating and Linting Blueprints.
3.  Rendering Images in Midjourney.
4.  Assembling the final slides.

## Directory Structure

*   `skill/`: Core documentation and prompt templates.
    *   `prompts/`: The actual prompts for Stage 1, Stage 2, and Operator Mode.
    *   `motifs/`: Definitions of visual styles (Atlas, Mythic, Systems, etc.).
    *   `notebooklm/`: Templates for ingesting content into NotebookLM for research.
    *   `citation/`: Standards for handling citations and sources.
*   `examples/`: Sample data.
    *   `blueprints/`: Reference blueprints for different essay types.
    *   `series/`: JSON/YAML configurations for generating entire series of essays.
*   `tools/`: Python scripts to automate the workflow.
    *   `series_generator.py`: Generates prompt files from a JSON/YAML series spec.
    *   `blueprint_linter.py`: Validates blueprints against strict formatting rules.
    *   `doctor.py`: Checks the health of the skill installation.
*   `schemas/`: JSON schemas for validating blueprints and series specs.

## Quickstart (Developers)

### Prerequisites

*   Python 3.8+
*   Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Generating a Series (Batch Mode)

1.  Edit `examples/series/series_ai_augmentation_atlas.json` or create your own.
2.  Run the generator:
    ```bash
    python tools/series_generator.py examples/series/series_ai_augmentation_atlas.json
    ```
3.  Find your generated prompts in `out/<Series_Title>/`.
4.  Follow the **Phase 5** instructions in the [Workflow Guide](guides/WORKFLOW.md).

### Validating a Blueprint

Ensure your blueprint follows the "LOCKED" block strictures:

```bash
python tools/blueprint_linter.py examples/blueprints/example_academic_writing_vs.blueprint.md
```

## Spelling & Integrity Guardrails

To ensure text integrity, we use **Canonical Text Blocks (LOCKED)**.
*   In the Blueprint, text designated for the final image is marked as `(LOCKED)`.
*   The Stage 2 Renderer is strictly instructed to copy this text verbatim.
*   The `blueprint_linter.py` script validates these blocks.
