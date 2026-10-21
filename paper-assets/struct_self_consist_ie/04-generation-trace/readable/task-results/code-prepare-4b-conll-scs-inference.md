# code prepare 4b conll scs inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_4b_conll_scs_inference_20260515T190528_result.json`
- **Structured JSON:** [`af2f41a3bc4607b513a3.json`](../../sessions/af/af2f41a3bc4607b513a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Task complete.

**Summary — Qwen3-4B CoNLL SCS Inference:**

- **Greedy F1 = 0.925** (higher than 8B's 0.907 — 4B benefits more from LoRA on this dataset)
- **SJ > FK > LP ordering holds**: rho 0.405 > 0.396 > 0.319 (structural consistency signals generalize across scale)
- **Structural beats surface**: SJ outperforms LP by +0.84pp rho
- **LP AUROC = 0.769 (full) / 0.815 (conditional)** — LP is a useful signal but weaker than structural
- **Verdict: MARGINAL** — oracle headroom is only 1.57pp because the 4B model already achieves 92.5% F1 on CoNLL, leaving minimal room for selection to help

Cross-scale takeaway: the SJ>FK>LP hierarchy is robust to model scale (4B vs 8B), but the 4B model has weaker SJ correlation (0.405 vs 0.450), possibly because higher base accuracy means less variance in sample quality for SCS to discriminate. Note the 8B comparison used N=16 vs N=8 here, so the rho gap may partly reflect sample count.

---
