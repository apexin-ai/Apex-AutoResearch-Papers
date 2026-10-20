# writing method section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-section_20260514T185032_result.json`
- **Structured JSON:** [`b64c5c3f861f3cef41b9.json`](../../sessions/b6/b64c5c3f861f3cef41b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `paper/method.tex`. Report:

```json
{
  "section": "3 Method (5 subsections: Task Formulation, GRPO Training, Solver Trace Ablation, Reward Formulations, Reward Hacking Taxonomy)",
  "word_count": "~1100 (raw LaTeX incl. commands; prose ~1050)",
  "citations_needed": [
    "deepseekmath — GRPO (✅ in bib)",
    "demillo1978 — mutation testing origin (✅ in bib)",
    "jia-harman-survey — mutation testing survey (✅ in bib)",
    "prover9 — McCune 2005-2010 (❌ missing from references.bib)",
    "swiprolog — Wielemaker et al. (❌ missing from references.bib, mentioned by name only)"
  ],
  "figures_needed": [
    "fig1_sta_overview — STA protocol diagram (exists as figures/paper/fig1_sta_overview.pdf)"
  ],
  "tables_needed": [],
  "notes": [
    "Algorithm 1 (STA pseudocode) requires \\usepackage{algorithm} and \\usepackage{algorithmic} in preamble",
    "Hacking taxonomy enumerate uses enumitem [leftmargin=*, itemsep=2pt] — verify ACL template compatibility or fall back to plain enumerate",
    "ISR limitations paragraph included per D051 premise-count confound; forward-references §Results for controlled analysis",
    "7 hacking modes per Director correction (query-as-fact gaming = mode 7)",
    "H7 ISR-specificity stat (64.5% vs 0%) sourced from D057 3-seed data",
    "Prover9 and SWI-Prolog bib entries need to be added to references.bib before compilation"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "3 Method (5 subsections: Task Formulation, GRPO Training, Solver Trace Ablation, Reward Formulations, Reward Hacking Taxonomy)",
    "word_count": "~1100 (raw LaTeX incl. commands; prose ~1050)",
    "citations_needed": [
      "deepseekmath — GRPO (✅ in bib)",
      "demillo1978 — mutation testing origin (✅ in bib)",
      "jia-harman-survey — mutation testing survey (✅ in bib)",
      "prover9 — McCune 2005-2010 (❌ missing from references.bib)",
      "swiprolog — Wielemaker et al. (❌ missing from references.bib, mentioned by name only)"
    ],
    "figures_needed": [
      "fig1_sta_overview — STA protocol diagram (exists as figures/paper/fig1_sta_overview.pdf)"
    ],
    "tables_needed": [],
    "notes": [
      "Algorithm 1 (STA pseudocode) requires \\usepackage{algorithm} and \\usepackage{algorithmic} in preamble",
      "Hacking taxonomy enumerate uses enumitem [leftmargin=*, itemsep=2pt] — verify ACL template compatibility or fall back to plain enumerate",
      "ISR limitations paragraph included per D051 premise-count confound; forward-references §Results for controlled analysis",
      "7 hacking modes per Director correction (query-as-fact gaming = mode 7)",
      "H7 ISR-specificity stat (64.5% vs 0%) sourced from D057 3-seed data",
      "Prover9 and SWI-Prolog bib entries need to be added to references.bib before compilation"
    ]
  }
}
```

</details>

---
