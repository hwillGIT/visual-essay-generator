# VEG Citation Schema

## Philosophy
Visual essays often lack space for full academic citations. We use a **Source Pack** model. The essay itself uses minimal markers (e.g., [S1]), and a separate comment/text block provides the full references.

## In-Text Markers
Use `[S#]` to denote a source index.
*   "The universe is expanding [S1]."

## Source Pack Format (JSON)

```json
{
  "sources": [
    {
      "id": "S1",
      "type": "book",
      "title": "The Fabric of Reality",
      "author": "David Deutsch",
      "year": 1997,
      "url": "optional"
    }
  ]
}
```

## Image Rules
*   **NEVER** put URLs inside the image pixels.
*   **NEVER** put full bibliographic strings inside the image pixels.
*   **OK**: "Source: D. Deutsch, 1997" (small footer).
