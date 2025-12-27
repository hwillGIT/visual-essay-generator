# Nano Banana Assembly Guide

This guide details how to turn VEG Blueprints into final assets using **Nano Banana**.

## The Rule of Text
> **The text in the final image must match the Blueprint EXACTLY.**

## Workflow

1.  **Input Source**:
    *   Get your generated Image Prompts from Gemini (Stage 2 output).
    *   *Note*: Clean up specific Midjourney parameters (like `--v 6.0` or `--style raw`) if Nano Banana does not recognize them. Keep the descriptive text and aspect ratio (`--ar 16:9`).
    *   Get your **LOCKED** text blocks from the Blueprint (Stage 1 output).
    *   *Note*: Ensure your output format in Nano Banana is set to **Landscape (16:9)** to match the prompt generator.

2.  **Nano Banana Execution**:
    *   Copy the prompt for **Slide 1** into Nano Banana.
    *   When Nano Banana asks for overlay text (or if using a template):
        *   Copy `HEADING (LOCKED)` -> Title Field.
        *   Copy `BODY TEXT (LOCKED)` -> Body Field.
    *   **Do not edit the text.** If the text is too long, go back to Gemini and ask it to shorten the blueprint, then re-lint.

3.  **PDF Generation**:
    *   Once all slides are generated in Nano Banana, export the set.
    *   If Nano Banana supports direct PDF export, use that setting to ensure text remains vector-based (crisp) if possible.
    *   Otherwise, export high-res PNGs and combine:
        *   *Mac*: Select all images -> Right Click -> Quick Actions -> Create PDF.
        *   *Windows*: Select all -> Print -> Microsoft Print to PDF.

## Troubleshooting

*   **Text Cutoff**: If Nano Banana truncates the body text, your blueprint might be exceeding the 40-word limit. Run the `blueprint_linter.py` again or check the word count.
*   **Style Inconsistency**: Ensure you included the **Motif Tokens** (e.g., "vintage map style") in every single Nano Banana prompt.
