# Event Driven Agent Framework

A modular framework for building, managing, and deploying specialized AI agent skills. This repository serves as a collection of production-ready "Skills" that can be run interactively or integrated into larger agentic workflows.

## 📚 Available Skills

### 1. [Visual Essay Generator (VEG v2.0)](skills/visual-essay-skill/README.md)
**Location**: `skills/visual-essay-skill/`

A complete pipeline for transforming abstract concepts, raw notes, or PDFs into high-fidelity visual narratives (slide decks, social carousels, or course materials).

*   **Workflow**: Topic -> Blueprint (Architecture) -> Render (Visuals) -> Assembly.
*   **Key Features**:
    *   **Interactive Web UI**: Run via Streamlit or Replit (No-Code).
    *   **Locked Motifs**: Enforce strict visual consistency (e.g., *Atlas*, *Systems*, *Mythic*).
    *   **Business Engine**: Translate formal diagrams (Swimlanes, Org Charts) into professional visual metaphors.
    *   **Text Integrity**: "LOCKED" block system ensures byte-perfect text retention in final images.

## 🚀 Getting Started

To use the tools in this repository, clone the repo and install the shared dependencies (or skill-specific dependencies).

```bash
git clone https://github.com/hwillGIT/event-driven-agent-framework.git
cd event-driven-agent-framework
```

### Running the Visual Essay Generator
You can run the VEG Web Interface immediately:

```bash
# Install dependencies
pip install -r skills/visual-essay-skill/requirements.txt

# Run the Streamlit App
streamlit run skills/visual-essay-skill/app/streamlit_app.py
```

## 📂 Repository Structure

```text
.
├── skills/
│   └── visual-essay-skill/   # VEG v2.0 Module
│       ├── app/              # Web UIs (Streamlit/Flask)
│       ├── skill/            # Prompts, Motifs, Metaphors
│       ├── tools/            # Python Automation Scripts
│       └── examples/         # Sample Blueprints & Specs
└── README.md
```

## 🤝 Contribution

1.  Pick a Skill module to improve.
2.  Follow the pattern: `skill/` (prompts), `tools/` (code), `app/` (UI).
3.  Ensure all generated content is "LOCKED" or validated by linters.
