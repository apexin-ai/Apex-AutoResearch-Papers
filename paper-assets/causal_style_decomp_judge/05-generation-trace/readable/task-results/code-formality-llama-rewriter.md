# code formality llama rewriter

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_formality_llama_rewriter_20260524T065554_result.json`
- **Structured JSON:** [`7cef1da52f3c0e825a84.json`](../../sessions/7c/7cef1da52f3c0e825a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `formality_llama_rewriter` complete. Registry updated to DONE/success.

**Results summary:**

| Metric | Llama-70B rewriter | Baseline (Qwen3-32B rewriter) |
|---|---|---|
| BT P(formal) | **71.1%** [64.3%, 77.5%] | 66.5% |
| BT p-value | **0.0001** | — |
| GEE Style OR | **4.44** (p=1.3e-05) | 4.20 |
| GEE Orig OR | **5.75** | 4.70 |
| Likert ATE | 0.02 (p=0.69, n.s.) | — |
| Blindspot | **YES** | — |

The formality bias is rewriter-independent — switching from Qwen3-32B to Llama-70B as the counterfactual rewriter actually yields a *slightly stronger* bias (71.1% vs 66.5%, +4.6pp), with overlapping CIs confirming consistency. The blindspot pattern (pairwise detects, Likert misses) also reproduces.

---
