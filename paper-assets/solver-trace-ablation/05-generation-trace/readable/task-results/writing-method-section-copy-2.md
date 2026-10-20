# writing method section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-section_20260515T200124_result.json`
- **Structured JSON:** [`120a78f483b39ca14be3.json`](../../sessions/12/120a78f483b39ca14be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "section": "method",
  "word_count": 1200,
  "citations_needed": [
    "proofwriter — ProofWriter dataset",
    "mccune2010prover9 — Prover9 theorem prover",
    "deepseekmath — GRPO origin",
    "demillo1978 — mutation testing",
    "jia-harman-survey — mutation testing survey"
  ],
  "figures_needed": [
    "fig1_sta_overview — 3-panel: (a) NL→formal→solver pipeline, (b) STA ablation protocol, (c) ISR diagnostic vs reward Goodhart arrow"
  ],
  "tables_needed": [
    "tab:reward — 6 reward conditions (included inline)"
  ],
  "notes": "Key changes from previous version: (1) Taxonomy 7→8 modes: H7 split into H7a/H7b, H8 conjunction collapse added. (2) H7 statistics updated to D095 final: ISR 70.6% vs Random 13.7%, Fisher p=1.3e-39, OR=15.05. (3) Genuine formula changed to set exclusion proved−|H7∪H1∪H8| per C013. (4) Data source corrected from FOLIO to ProofWriter (file naming evidence: proofwriter_fol_*.jsonl). (5) Fig 1 placeholder added with 3-panel description. (6) ISR definition merged into §3.3 STA (was separate §3.4). Verify: is training data actually ProofWriter or FOLIO? File names suggest ProofWriter but existing tex cited FOLIO."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "method",
    "word_count": 1200,
    "citations_needed": [
      "proofwriter — ProofWriter dataset",
      "mccune2010prover9 — Prover9 theorem prover",
      "deepseekmath — GRPO origin",
      "demillo1978 — mutation testing",
      "jia-harman-survey — mutation testing survey"
    ],
    "figures_needed": [
      "fig1_sta_overview — 3-panel: (a) NL→formal→solver pipeline, (b) STA ablation protocol, (c) ISR diagnostic vs reward Goodhart arrow"
    ],
    "tables_needed": [
      "tab:reward — 6 reward conditions (included inline)"
    ],
    "notes": "Key changes from previous version: (1) Taxonomy 7→8 modes: H7 split into H7a/H7b, H8 conjunction collapse added. (2) H7 statistics updated to D095 final: ISR 70.6% vs Random 13.7%, Fisher p=1.3e-39, OR=15.05. (3) Genuine formula changed to set exclusion proved−|H7∪H1∪H8| per C013. (4) Data source corrected from FOLIO to ProofWriter (file naming evidence: proofwriter_fol_*.jsonl). (5) Fig 1 placeholder added with 3-panel description. (6) ISR definition merged into §3.3 STA (was separate §3.4). Verify: is training data actually ProofWriter or FOLIO? File names suggest ProofWriter but existing tex cited FOLIO."
  }
}
```

</details>

---
