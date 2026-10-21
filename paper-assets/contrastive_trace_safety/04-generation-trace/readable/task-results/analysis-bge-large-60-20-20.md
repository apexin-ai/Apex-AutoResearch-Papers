# analysis bge large 60 20 20

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bge_large_60_20_20_20260518T202717_result.json`
- **Structured JSON:** [`603aed508c45d080bff5.json`](../../sessions/60/603aed508c45d080bff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Completed. Here's the summary:

## BGE-large 60/20/20 Results

**Status**: RERUN completed (QwQ corrected W=3→W=5, MiniLM added)
**Config**: 60/20/20 split, seed=42, LR(C=1.0, balanced), 10k bootstrap, two-sided p-values

### Per-model metrics

| Model | Modality | BA | Prec | FPR |
|-------|----------|-----|------|-----|
| **R1-8B** (W=15) | HS | .729 | .497 | .233 |
| | BGE | .646 | .436 | .221 |
| | MiniLM | .659 | .400 | .318 |
| **OT-7B** (W=3) | HS | .682 | .446 | .138 |
| | BGE | .575 | .263 | .243 |
| | MiniLM | .577 | .248 | .315 |
| **R1-32B** (W=1) | HS | .742 | .588 | .273 |
| | BGE | .633 | .475 | .351 |
| | MiniLM | .627 | .472 | .345 |
| **QwQ-32B** (W=5) | HS | .725 | .524 | .251 |
| | BGE | .635 | .442 | .267 |
| | MiniLM | .543 | .330 | .347 |

### Holm-Bonferroni (HS vs BGE, 12 tests): **3/12 reject**
- **OT-7B**: all 3 metrics PASS (p=0.0006, 0.0020, 0.0026)
- **R1-32B**: BA uncorrected p=0.013, but fails HB threshold
- **R1-8B, QwQ-32B**: no metrics pass HB

### Key observations
- HS advantage is **directionally positive across all 4 models** for all metrics (except R1-8B FPR: -1.2pp adverse)
- Only OT-7B survives full HB correction against BGE — consistent with paper's "encoder-conditional" framing
- BGE vs MiniLM: mostly NS (BGE slightly better on FPR, otherwise indistinguishable)
- QwQ W=5 results differ from old W=3: HS-BGE gaps narrowed and lost significance

**Artifacts**: `results.json` and `results_summary.txt` saved to `/root/autodl-tmp/contrastive_trace_safety/artifacts/bge_large_60_20_20/`

---
