# Visual Essay Generator (VEG v2.0)

A production-ready pipeline for transforming abstract concepts, raw notes, or PDFs into high-fidelity visual narratives (slide decks, social carousels, or course materials).

*   **Workflow**: Topic -> Blueprint (Architecture) -> Render (Visuals) -> Assembly.
*   **Key Features**:
    *   **Interactive Web UI**: Run via Streamlit or Replit (No-Code).
    *   **Locked Motifs**: Enforce strict visual consistency (e.g., *Atlas*, *Systems*, *Mythic*).
    *   **Business Engine**: Translate formal diagrams (Swimlanes, Org Charts) into professional visual metaphors.
    *   **Text Integrity**: "LOCKED" block system ensures byte-perfect text retention in final images.

## 🌍 Web Interface (Replit / Flask)

If you are running on **Replit** (or prefer a standard Web Server), use the Flask app:

1.  **Run Command**:
    ```bash
    python3 app/replit_app.py
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
    streamlit run app/streamlit_app.py
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
python3 app/veg.py
```

This launches a menu where you can:
1.  **Create a New Essay**: Generates the exact Operator prompt for your topic + style.
2.  **Generate a Series**: Automatically reads your JSON/YAML specs and builds the prompt pack.
3.  **Process PDFs**: Creates the specific "Extraction Prompt" for NotebookLM.

## 📂 Repository Structure

```text
.
├── app/              # Web UIs (Streamlit/Flask)
├── skill/            # Prompts, Motifs, Metaphors
├── tools/            # Python Automation Scripts
├── examples/         # Sample Blueprints & Specs
└── README.md
```

## 🤝 Contribution

1.  Ensure all generated content is "LOCKED" or validated by linters.
