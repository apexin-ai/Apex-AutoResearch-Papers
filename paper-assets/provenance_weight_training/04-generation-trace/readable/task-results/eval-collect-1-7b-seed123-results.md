# eval collect 1 7b seed123 results

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_1_7b_seed123_results_20260520T163831_result.json`
- **Structured JSON:** [`f048075316a572461d3d.json`](../../sessions/f0/f048075316a572461d3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval entries are in PREPARING state and can't jump to DONE — not critical since the main experiment entries have all metrics. Here's the complete results table:

| Metric | uniform seed123 | adaptive seed123 | Δ (adaptive − uniform) |
|--------|----------------|-----------------|------------------------|
| **eval_ppl_openwebtext** | 13.292 | 13.291 | −0.001 |
| **eval_ppl_wikipedia** | 10.942 | 10.952 | +0.010 |
| **downstream_arc_easy_acc_norm** | 0.7260 | 0.7138 | −0.0122 |
| **downstream_arc_challenge_acc_norm** | 0.4317 | 0.4386 | +0.0069 |
| **downstream_hellaswag_acc_norm** | 0.6118 | 0.6147 | +0.0029 |
| **downstream_piqa_acc_norm** | 0.7454 | 0.7459 | +0.0005 |
| **downstream_winogrande_acc** | 0.6133 | 0.6298 | +0.0165 |
| **downstream_mean** | 0.6256 | 0.6286 | **+0.0030** |

seed123 与 seed42 趋势一致：OOD PPL 几乎相同（差异 <0.01），downstream mean adaptive 略优 (+0.30pp vs seed42 的 −0.05pp)。两个 seed 综合看 1.7B scale 下 adaptive 和 uniform 差异极小。

---
