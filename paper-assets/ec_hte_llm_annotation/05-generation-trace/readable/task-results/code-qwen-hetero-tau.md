# code qwen hetero tau

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-hetero-tau_20260522T000224_result.json`
- **Structured JSON:** [`fc994adb0b5d87705449.json`](../../sessions/fc/fc994adb0b5d87705449.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs verified:

- **CSV**: 4801 lines (4800 data + 1 header) -- matches expected 50 seeds x 3 budgets x 4 methods x 8 cells = 4800
- **Analysis report**: written with full cross-model comparison

**Key results**:

| Budget | Qwen EC-HTE wins bias? | Llama EC-HTE wins bias? |
|--------|----------------------|----------------------|
| 200 | YES (+0.0093) | YES (+0.0117) |
| 500 | YES (+0.0141) | YES (+0.0215) |
| 1000 | YES (+0.0162) | YES (+0.0156) |

**EC-HTE's bias advantage is consistent across both models** -- it wins on |Bias| at all 3 budget levels for both Qwen and Llama.

Both models show the same bias-variance tradeoff: EC-HTE wins bias but loses RMSE (0/3 budgets for both), because per-subgroup correction adds variance at small expert budgets. The RMSE gap narrows with more experts (Qwen at n=1000: ΔRMSE = -0.0079).

Interestingly, Llama shows slightly larger average EC-HTE improvement (Δ|Bias| = +0.0163) despite smaller CM heterogeneity (Δ_FPR=0.219 vs Qwen's 0.241). This may be because Qwen's True_short subgroup has FPR=0.000, making its mixing matrix nearly singular and limiting correction effectiveness in that cell.

---
