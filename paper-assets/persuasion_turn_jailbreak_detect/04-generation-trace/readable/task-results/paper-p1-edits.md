# paper p1 edits

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1_edits_20260522T073205_result.json`
- **Structured JSON:** [`a3b131af24020e220e10.json`](../../sessions/a3/a3b131af24020e220e10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No undefined references. All modifications are complete and verified. Here's the summary:

---

### Modifications completed

| # | Item | File | What changed |
|---|------|------|-------------|
| 4 | N2(d) DAPT bias | `conclusion.tex:19` | Added "classification DAPT increases WildChat FPR from 48.1% (vanilla) to 68.1%...confirming adaptation amplifies benign sensitivity" in Two-axis paragraph |
| 5 | Q2 Task-structure | `conclusion.tex:16` | Added at end of Regularization mechanism: "This advantage is condition-specific: classification DAPT outperforms MLM only under multi-turn synthetic evaluation; on single-turn human data (ToxicChat), MLM generalizes better" |
| 6 | W4 Cross-architecture | `experiments.tex:22,144,150,174,177` | Renamed "Cross-Encoder Validation" to "Cross-Architecture Observation"; added architecture confound acknowledgment; reframed RoBERTa-large as "DAPT may be unnecessary or mildly harmful for strong pretrained encoders" |
| 7 | W5 Mixed-LLM caveat | `experiments.tex:189` | Reframed: "ActorAttack remains challenging under mixed-LLM conditions (9-class F1=0.504±0.107...)" |
| 8 | W6 FITD disclaimer | `experiments.tex:63` | "FITD serves as a near-ceiling baseline where all variants achieve F1≥0.990, providing limited discriminative power" |
| 9 | Q3 Limitations | `conclusion.tex:30` | Added: "The 10-conversation benign adaptation result is validated only on WildChat (GPT-3.5 user conversations); whether it generalizes to other LLM assistants or enterprise chat systems is unevaluated" |
| 11 | VL1 Table font | `appendix.tex` | No change needed: Tables 7 & 8 already use `\small` (larger than `\footnotesize`) |

### Space compression (to maintain 8-page limit)
- Merged "Variance reversal" and "Encoder capacity" into single paragraph
- Compressed Regularization mechanism, Two-axis generalization, and Conclusion paragraphs
- Trimmed abstract by ~2 lines (removed verbose phrasings)
- No data or claims deleted; all original content preserved in compressed form

### Compilation verification
- Conclusion: page 8
- Limitations: page 9
- No LaTeX errors, no undefined references

---
