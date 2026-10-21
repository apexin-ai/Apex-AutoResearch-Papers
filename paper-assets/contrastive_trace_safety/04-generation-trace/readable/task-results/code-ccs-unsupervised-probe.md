# code ccs unsupervised probe

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ccs_unsupervised_probe_20260517T141539_result.json`
- **Structured JSON:** [`32c64996a606516fb52f.json`](../../sessions/32/32c64996a606516fb52f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results:

**R1-8B Comparison (primary model):**

| Method | Type | bal_acc | precision | FPR | lead |
|--------|------|---------|-----------|-----|------|
| LR probe | supervised | 0.817 | 0.693 | 0.097 | -2.0 |
| **CCS** | **unsupervised** | **0.777** | **0.565** | **0.191** | **+0.7** |
| RepE | unsupervised | 0.749 | 0.516 | 0.226 | +9.7 |

**All models CCS:**

| Model | bal_acc | precision | FPR | coverage | lead |
|-------|---------|-----------|-----|----------|------|
| r1-8b | 0.777 | 0.565 | 0.191 | 0.674 | +0.7 |
| qwq-32b | 0.731 | 0.555 | 0.214 | 0.684 | +2.0 |
| r1-32b | 0.703 | 0.507 | 0.410 | 0.900 | +5.2 |
| ot-7b | 0.692 | 0.319 | 0.344 | 0.809 | +20.5 |

**Key findings:**
- CCS is the best unsupervised method tested, beating RepE on R1-8B (bal_acc 0.777 vs 0.749, FPR 0.191 vs 0.226)
- Still significantly below supervised LR probe (bal_acc 0.817, FPR 0.097)
- All models needed polarity flip (probe consistently learned inverse mapping first)
- FPR remains high across all models (0.19-0.41), confirming the unsupervised gap
- OT-7B has high coverage/lead but low precision (0.319), indicating indiscriminate triggering

Outputs: script at `src/experiments/exp_r3_ccs_probe.py`, results at `artifacts/exp_r3_ccs_probe/results.json`.

---
