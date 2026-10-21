# writing introduction

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_introduction_20260515T220623_result.json`
- **Structured JSON:** [`83263bf96045b727dda5.json`](../../sessions/83/83263bf96045b727dda5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/_project/paper/introduction.tex`。

```json
{
  "section": "Introduction",
  "word_count": 780,
  "citations_needed": [
    "cheng_2025_contamination_survey",
    "shumailov_2024_model_collapse",
    "dohmatob_2025_strong_collapse",
    "drayson_2025_detection_collapse",
    "he_2025_golden_ratio",
    "feng_2025_beyond_collapse",
    "wang_2026_survive_contamination"
  ],
  "figures_needed": [],
  "notes": [
    "No section header included — main.tex already defines \\section{Introduction}\\label{sec:intro}",
    "Uses custom macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)",
    "Cross-references: \\S\\ref{sec:method}, \\S\\ref{sec:results}, \\S\\ref{sec:experiments}, Proposition~\\ref{prop:monotone}",
    "Key numbers verified against registry: adaptive mean 17.651, grid-best mean 17.646, uniform mean 17.694, ESS-only mean 17.722",
    "ESS-only 3-seed mean (17.722) computed from registry — Results Table 1 currently shows seed42 only with dagger footnote; may need update",
    "Batch regime stats (49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding) from verified Q1 analysis",
    "Contribution bullets map to: C1→§3 method, C2→§5 results (adaptive vs grid + ESS-only), C3→§4 experiments (detector)"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "Introduction",
    "word_count": 780,
    "citations_needed": [
      "cheng_2025_contamination_survey",
      "shumailov_2024_model_collapse",
      "dohmatob_2025_strong_collapse",
      "drayson_2025_detection_collapse",
      "he_2025_golden_ratio",
      "feng_2025_beyond_collapse",
      "wang_2026_survive_contamination"
    ],
    "figures_needed": [],
    "notes": [
      "No section header included — main.tex already defines \\section{Introduction}\\label{sec:intro}",
      "Uses custom macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)",
      "Cross-references: \\S\\ref{sec:method}, \\S\\ref{sec:results}, \\S\\ref{sec:experiments}, Proposition~\\ref{prop:monotone}",
      "Key numbers verified against registry: adaptive mean 17.651, grid-best mean 17.646, uniform mean 17.694, ESS-only mean 17.722",
      "ESS-only 3-seed mean (17.722) computed from registry — Results Table 1 currently shows seed42 only with dagger footnote; may need update",
      "Batch regime stats (49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding) from verified Q1 analysis",
      "Contribution bullets map to: C1→§3 method, C2→§5 results (adaptive vs grid + ESS-only), C3→§4 experiments (detector)"
    ]
  }
}
```

</details>

---
