# train oh cmdrep ablation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_oh-cmdrep-ablation_20260514T150300_result.json`
- **Structured JSON:** [`b50c83da74d0f097ba5b.json`](../../sessions/b5/b50c83da74d0f097ba5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed and registered. Here's the summary:

## OH cmd_rep Ablation Results

**Hypothesis confirmed**: Removing the command_repetition LF significantly improves cross-domain performance.

### Primary (conf>=1, 72,554 windows, 58.6% stagnation)

| Metric | 3-LF Baseline | No-cmd_rep | Delta |
|--------|--------------|------------|-------|
| Zero-shot macro_f1 | 0.5298 | **0.6071** | **+0.0773** |
| Fine-tune macro_f1 | 0.6880 | **0.9272** | **+0.2392** |
| Fine-tune f1_stag | — | 0.9379 | — |
| Fine-tune f1_prog | — | 0.9165 | — |

### Secondary (conf>=2, 4,017 windows, 96.3% stagnation)
- Zero-shot: 0.4631 (too skewed to be useful)
- Fine-tune: 0.9032 (high f1_stag=0.9917 but only 27 progress test samples)

### Key findings
- cmd_rep fired on 99.8% of OH windows, dominating the original 3-LF majority vote
- Removing it drops coverage from 143K to 72.5K windows but flips stag_ratio from 6.6% to 58.6% — much more balanced
- Zero-shot f1_stag jumped from 0.1513 to 0.5366 — the SWE-agent checkpoint can now detect OH stagnation
- Fine-tuned model achieves 0.9272 macro_f1 with balanced class performance (stag: 0.9379, prog: 0.9165)

---
