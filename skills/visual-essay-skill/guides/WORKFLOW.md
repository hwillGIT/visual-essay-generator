# Visual Essay Workflow Guide

This guide explains **HOW** to use the Visual Essay Generator (VEG) effectively. It bridges the gap between the Python tools and the AI Chat interface.

## Prerequisites

1.  **LLM Access**: You need access to a high-reasoning model (GPT-4, Claude 3 Opus/Sonnet).
2.  **Image Generator**: Access to Midjourney (Discord or Web) or DALL-E 3.
3.  **Design Tool**: Figma, Canva, or Photoshop for final assembly.
4.  **Terminal**: To run the linter and generator scripts.

---

## Phase 1: The Operator Session

The core of this skill is the "Operator Mode" prompt. It turns your LLM into the VEG engine.

1.  **Initialize the Session**:
    *   Open `skill/prompts/mega_prompt_operator_mode.md`.
    *   Copy the **entire file content**.
    *   Paste it into a fresh chat window (ChatGPT/Claude).
    *   *System Response*: The AI should confirm it is ready and list available commands (`/new`, `/blueprint`, etc.).

2.  **Start a Project**:
    *   Type `/new` followed by your topic or raw notes.
    *   *Example*: `/new I want to write about why open source code is like a digital coral reef.`

3.  **Discovery (Optional)**:
    *   The Operator will ask questions to clarify your thesis, audience, and tone. Answer them to refine the concept.

---

## Phase 2: Blueprint Generation (Stage 1)

1.  **Generate**:
    *   When ready, the Operator will run the **Stage 1 Blueprint Generator**.
    *   It will output a Markdown code block containing the essay structure (Slides, Visual Anchors, Text).

2.  **Validation (Crucial)**:
    *   Copy the Markdown code block from the chat.
    *   Save it locally (e.g., `drafts/my_coral_reef.md`).
    *   **Run the Linter**:
        ```bash
        python tools/blueprint_linter.py drafts/my_coral_reef.md
        ```
    *   **Fix Errors**: If the linter flags "Risk Punctuation" or "Missing Blocks", ask the AI to fix it:
        *   *User*: "The linter says Slide 3 has an em-dash in the Locked Body. Please remove it and reprint the blueprint."

---

## Phase 3: Rendering (Stage 2)

1.  **Choose a Motif**:
    *   Review `skill/motifs/motifs.md` to pick a style (e.g., `Systems` or `Atlas`).
    *   *User*: `/render Systems`

2.  **Get Image Prompts**:
    *   The Operator will output a list of **Image Prompts** (optimized for Midjourney) and the **Overlay Text** for each slide.

3.  **Generate Images**:
    *   Copy the `/imagine ...` commands.
    *   Paste them into your Midjourney Discord channel.
    *   Upscale the best variants (`U1`, `U2`, etc.).
    *   Save the images to your project folder.

---

## Phase 4: Assembly

You now have **Images** (from Midjourney) and **Text** (from the Blueprint). You need to combine them.

### Option A: Manual Assembly (Figma/Canva)
1.  Create a standard frame (e.g., 1080x1350 for Instagram).
2.  Place the generated image.
3.  Overlay the **HEADING (LOCKED)** text in a large, bold font.
4.  Overlay the **BODY TEXT (LOCKED)** in a readable body font.
5.  *Tip*: Use a semi-transparent dark box behind text if the image is busy.

### Option B: The "Source Pack"
1.  If your essay uses citations (`[S1]`), create a final slide or a caption comment using `skill/citation/source_pack_template.md`.
2.  Fill in the real references.

---

## Phase 5: Series Generation (Automated)

If you have a JSON/YAML spec for 10 essays:

1.  Run the generator:
    ```bash
    python tools/series_generator.py examples/series/series_ai_augmentation_atlas.json
    ```
2.  This creates 10 `.prompt.md` files in `out/`.
3.  **For each file**:
    *   Open the file.
    *   Copy the content.
    *   Paste into a **new** LLM chat.
    *   The prompt is pre-loaded to generate the specific essay defined in the JSON.
    *   Follow Phase 2 and 3 above.
