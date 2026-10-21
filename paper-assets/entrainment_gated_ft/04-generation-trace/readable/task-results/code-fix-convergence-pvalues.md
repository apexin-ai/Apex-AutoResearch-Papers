# code fix convergence pvalues

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_convergence_pvalues_20260519T053517_result.json`
- **Structured JSON:** [`724cf1a2d231238a0433.json`](../../sessions/72/724cf1a2d231238a0433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**p 值修复**：1.3B lambada rho=-1.0 的 p 值从渐近的 ~1.4e-24 修正为精确排列检验的 **0.0167**（5!=120 种排列）。这是唯一 p<0.05 的组合。

**非单调模式**：
- 340M: lambada (min at attn=4), hellaswag (min at attn=0), winogrande (min at attn=1) 均有反弹
- 1.3B: hellaswag (min at attn=1), arc_challenge (min at attn=2) 有反弹；lambada/arc_easy/mmlu 单调收敛

CSV 已更新，包含 `min_std_attn`, `min_std`, `reduction_pct`, `rebound_pct` 列。PDF/PNG 图表已重新生成。

---
