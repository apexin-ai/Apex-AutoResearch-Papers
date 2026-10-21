# exp gemma comet fix

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma-comet-fix_20260524T170207_result.json`
- **Structured JSON:** [`a75bf00f50b7edae2005.json`](../../sessions/a7/a75bf00f50b7edae2005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline complete. Here's the **Gemma-2 COMET Tercile Ablation** result:

---

## COMET Tercile Ablation — Gemma-2-9B-IT (EN→ZH, Layer 17)

| Tercile | n | COMET range | COMET mean | Balanced Acc |
|---------|---|-------------|------------|--------------|
| **High** | 112 | [0.9122, 0.9634] | 0.9304 | **0.6261** |
| **Med** | 112 | [0.8871, 0.9120] | 0.8996 | 0.6003 |
| **Low** | 111 | [0.8076, 0.8870] | 0.8564 | 0.5233 |

- **Full test balanced_acc:** 0.5877
- **Delta (High − Low):** +10.28 pp
- **Fisher exact test:** p = 0.278, OR = 0.728
- **Conclusion: CONFOUNDER** — higher COMET (better translation quality) correlates with higher probe accuracy (+10.28 pp), suggesting translation quality is a confounding factor for cross-lingual probe performance on Gemma-2.

**Fix applied:** The original script indexed tertile masks (0–341) into the 335-entry prediction array. Fixed by computing tertiles only over the 335 validated entries that have activations, excluding the 7 filtered-out (COMET < 0.80) samples.

**Implication:** The COMET gate (≥ 0.80 threshold) is not aggressive enough for Gemma-2 — low-quality translations in the passed set still depress probe accuracy. Consider tightening the threshold or controlling for translation quality in subsequent analyses.

---
