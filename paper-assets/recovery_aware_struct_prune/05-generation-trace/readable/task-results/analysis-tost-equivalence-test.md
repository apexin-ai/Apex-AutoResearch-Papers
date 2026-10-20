# analysis tost equivalence test

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost_equivalence_test_20260524T174218_result.json`
- **Structured JSON:** [`b7c740d5294f0f946059.json`](../../sessions/b7/b7c740d5294f0f946059.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TOST 分析完成。结果写入 `artifacts/tost_analysis_results.json`。

**核心发现：**

| 比较 | Δ (pp) | ε=2pp p值 | 等价? |
|---|---|---|---|
| **CKA-only** | | | |
| SFT(63.91%) vs GRPO seed42(64.37%) | -0.45 | 0.008 | ✓ |
| SFT vs GRPO seed123(64.22%) | -0.30 | 0.005 | ✓ |
| SFT vs GRPO verify(64.06%) | -0.15 | 0.001 | ✓ |
| SFT vs GRPO seed456(64.59%) | -0.68 | 0.023 | ✓ |
| **Standard** | | | |
| SFT(59.21%) vs GRPO seed123(59.89%) | -0.68 | 0.020 | ✓ |
| SFT vs GRPO seed456(60.20%) | -0.99 | 0.069 | ✗ (borderline) |
| SFT vs GRPO fair_v2(59.44%) | -0.23 | 0.010 | ✓ |
| SFT vs GRPO ext300(59.29%) | -0.08 | 0.007 | ✓ |

- **ε=1pp**：所有对都不显著（N=1319 power 不足以检测 1pp 等价带）
- **ε=2pp**：7/8 对等价 (p<0.05)，仅 std_vs_seed456 borderline (p=0.069)
- **ε=3pp**：8/8 全部等价 (all p<0.002)
- 所有差异 <1pp，GRPO 一致略优但差异微不足道

---
