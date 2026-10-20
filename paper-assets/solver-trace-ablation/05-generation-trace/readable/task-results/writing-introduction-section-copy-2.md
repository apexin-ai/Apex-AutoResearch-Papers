# writing introduction section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_introduction-section_20260514T185603_result.json`
- **Structured JSON:** [`4b0c1839e1c15bfe71ab.json`](../../sessions/4b/4b0c1839e1c15bfe71ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File looks good. ~1028 words (after stripping LaTeX markup), within the ~1200 budget. All edits applied cleanly.

**Changes made to the existing draft:**
1. Added `\citep{demillo1978}` — mutation testing inspiration for STA (line 19)
2. Replaced `\S\ref{sec:diagnostic}` with `Figure~\ref{fig:isr-collapse}` on the ISR collapse trajectory line (line 25) — previews Fig 2 in intro as requested
3. Converted `\begin{enumerate}` contributions list into flowing paragraph with "First... Second... Third... Fourth..." (lines 49–53)

```json
{
  "section": "introduction",
  "word_count": "~1030 (LaTeX-stripped estimate)",
  "citations_needed": [
    "satlm", "logic-lm", "linc", "deepseekmath",
    "mellgren-prolog-grpo", "logic-rl",
    "skalse-reward-hacking", "reward-hacking-survey",
    "demillo1978",
    "manheim-goodhart-taxonomy", "karwowski-goodhart-rl",
    "gao-reward-overoptimization"
  ],
  "figures_needed": [
    "fig:sta-overview (Fig 1: STA protocol overview)",
    "fig:isr-collapse (Fig 2: ISR collapse trajectory)"
  ],
  "tables_needed": [],
  "notes": [
    "Line 44 uses proved-only ISR* (0.037, 0.015, 0.387) while experiments.tex table uses all-sample ISR (0.031, 0.008, 0.081) — consistent but notation should be harmonized",
    "fig:sta-overview label uses hyphen (existing convention); instructions used underscore — verify label matches actual figure definition",
    "No \\cite{proofwriter} in intro; dataset formally introduced in \\S experiments — acceptable",
    "\\cite{folio} not used; actual data is ProofWriter, not FOLIO"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "introduction",
    "word_count": "~1030 (LaTeX-stripped estimate)",
    "citations_needed": [
      "satlm",
      "logic-lm",
      "linc",
      "deepseekmath",
      "mellgren-prolog-grpo",
      "logic-rl",
      "skalse-reward-hacking",
      "reward-hacking-survey",
      "demillo1978",
      "manheim-goodhart-taxonomy",
      "karwowski-goodhart-rl",
      "gao-reward-overoptimization"
    ],
    "figures_needed": [
      "fig:sta-overview (Fig 1: STA protocol overview)",
      "fig:isr-collapse (Fig 2: ISR collapse trajectory)"
    ],
    "tables_needed": [],
    "notes": [
      "Line 44 uses proved-only ISR* (0.037, 0.015, 0.387) while experiments.tex table uses all-sample ISR (0.031, 0.008, 0.081) — consistent but notation should be harmonized",
      "fig:sta-overview label uses hyphen (existing convention); instructions used underscore — verify label matches actual figure definition",
      "No \\cite{proofwriter} in intro; dataset formally introduced in \\S experiments — acceptable",
      "\\cite{folio} not used; actual data is ProofWriter, not FOLIO"
    ]
  }
}
```

</details>

---
