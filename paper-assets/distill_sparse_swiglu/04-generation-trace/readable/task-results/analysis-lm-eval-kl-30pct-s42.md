# analysis lm eval kl 30pct s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lm_eval_kl_30pct_s42_20260516T024801_result.json`
- **Structured JSON:** [`3f8b1a1335c847eb82f4.json`](../../sessions/3f/3f8b1a1335c847eb82f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

---

## lm_eval_kl_30pct_s42 Results — **Conclusion: NEGATIVE**

### Metrics (KL distill, 30% sparsity)

| Task | Metric | KL 30% | Dense | Drop % | KL 50% | Δ vs 50% |
|------|--------|--------|-------|--------|--------|----------|
| ARC-c | acc_norm | 0.3737 | 0.5819 | **-35.8%** | 0.3771 | -0.003 |
| WinoGrande | acc | 0.6756 | 0.7814 | **-13.5%** | 0.6156 | +0.060 |
| MMLU | acc | 0.2874 | 0.6532 | **-56.0%** | 0.2591 | +0.028 |
| GSM8K | em_flex | 0.0781 | 0.5004 | **-84.4%** | 0.0121 | +0.066 |

Actual sparsity: 0.300 (on target). Per-layer range: 0.125 (layer 18) to 0.703 (layer 31).

### Analysis

- **WinoGrande** is the only task with acceptable retention (86.5% of dense). 30% meaningfully better than 50% (+6 pts).
- **ARC-c** nearly identical at 30% vs 50% — both ~36% drop from dense. Reducing sparsity from 50% → 30% did not help.
- **MMLU** at 0.2874 is near random chance (0.25). 56% drop from dense. Only marginally better than 50% KL (0.2591).
- **GSM8K** improved 6x over 50% (7.8% vs 1.2%), but still catastrophic — 84% drop from dense. Reasoning capability is destroyed.

### Verdict

30% sparsity with KL distillation still shows catastrophic degradation on knowledge (MMLU) and reasoning (GSM8K) tasks. The improvement over 50% is insufficient — GSM8K remains near-zero, MMLU remains near-random. Cannot claim "30% as recommended configuration."

---
