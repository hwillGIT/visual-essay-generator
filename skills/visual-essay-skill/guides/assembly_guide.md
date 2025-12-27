# Visual Essay Assembly Guide

Once you have your **Images** (from Midjourney/DALL-E) and your **Locked Text** (from the Blueprint), you need to assemble them.

## The Rule of Text
> **The text in the final image must match the Blueprint EXACTLY.**

This is why we use "LOCKED" blocks. Do not let a designer or an AI summarizer change the wording during assembly.

## Design Tools

### 1. Figma (Recommended)
*   **Frame Size**:
    *   Instagram/LinkedIn Portrait: `1080 x 1350` (4:5 aspect ratio)
    *   Twitter/Slide Deck: `1920 x 1080` (16:9 aspect ratio)
*   **Typography Hierarchy**:
    *   **Header**: Impactful, usually Uppercase. Sans-serif for *Systems/Didactic*, Serif for *Atlas/Mythic*.
    *   **Body**: Highly readable. Max 40 words.
    *   **Footer**: Small citation markers (`[S1]`) and series title.

### 2. Canva
*   Use the "Bulk Create" feature if doing a Series.
*   Upload your CSV of [Image Filename, Header, Body].
*   Match the field to the text elements.

## PDF Pipeline (For NotebookLM)

If you are using **NotebookLM** to generate the source material:

1.  **Ingest**: Upload PDFs to NotebookLM.
2.  **Synthesize**: Use `skill/notebooklm/instruction_note_master.md` to get a "Structure Suggestion".
3.  **Transfer**: Paste that structure into the VEG Operator Chat as your "Draft".

## Final Check
Before publishing, run the **"Squint Test"**:
1.  Can you read the Header in 1 second?
2.  Can you read the Body in 5 seconds?
3.  Does the Image support the Metaphor, or distract from it?
