# fix oh cmdrep ablation retrain

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_oh-cmdrep-ablation-retrain_20260514T224513_result.json`
- **Structured JSON:** [`fa70dc11ae4baec0ce33.json`](../../sessions/fa/fa70dc11ae4baec0ce33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments completed and registry updated. Here's the final comparison:

## Results: cmdrep ablation with fixed OH data

### Old (buggy labels, stag=6.56%) vs New (fixed labels, stag=21.45%)

| Metric | Old Data | New Data |
|--------|----------|----------|
| 3-LF fine-tuned | 0.7512 | **0.9763** |
| 2-LF fine-tuned (conf≥2) | 0.9272 | **0.9113** |
| 2-LF fine-tuned (conf≥1) | — | **0.9238** |
| Delta (2LF - 3LF) | **+17.6pp** | **-5.3 to -6.5pp** |

### Full new results table

| Condition | Windows | Stag% | ZS F1 | FT F1 | Δ vs 3-LF FT |
|-----------|---------|-------|-------|-------|-------------|
| 3-LF (fixed) | 143,057 | 21.5% | 0.5186 | 0.9763 | — |
| 2-LF conf≥2 | 4,017 | 96.3% | 0.2381 | 0.9113 | -6.5pp |
| 2-LF conf≥1 | 72,554 | 58.6% | 0.4389 | 0.9238 | -5.3pp |

### Key findings
- The old +17.6pp improvement claim was **entirely an artifact of the label bug**
- With fixed labels, removing cmd_rep consistently **hurts** performance (-5 to -6.5pp)
- cmd_rep false positive rate dropped from 71% (old claim) to **2.3%** on the fixed data
- 3-LF labels now produce near-perfect probes (F1=0.9763), leaving little room for improvement

Both `oh-cmdrep-ablation` and `cross-agent-no-cmdrep` registry entries updated with conclusion=**negative**.

---
