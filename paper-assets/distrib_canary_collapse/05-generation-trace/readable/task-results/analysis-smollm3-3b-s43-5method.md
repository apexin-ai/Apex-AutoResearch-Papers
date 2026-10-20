# analysis smollm3 3b s43 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smollm3_3b_s43_5method_20260520T185223_result.json`
- **Structured JSON:** [`a66f73765c62730aa1dd.json`](../../sessions/a6/a66f73765c62730aa1dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## SmolLM3-3B s43 5-Method Results (11 gens, α=1.0)

| | s43 | s42 |
|---|---|---|
| **PermG FDR forward** | 3/8 (ECE only) | 3/8 (ECE only) |
| **K≥3 robust** | 6/8 | 3/8 |
| TY Granger | 6/8 (d_max=0) | 0/8 (d_max=2) |
| DiffXCorr FDR | 8/8 | 6/8 |

**关键发现：**
- **PermG 跨 seed 完美复制** — 两个 seed 均为 3/8，全部来自 ECE 通道
- K≥3 差异由 TY d_max 不稳定驱动（s43 ADF 判定 I(0)，s42 判定 I(2)），符合 C003 警告
- **token_entropy U-shape 两 seed 均确认** — s43 min at gen 3 (0.90), s42 min at gen 2 (0.94)；distinct_1 单调递减，解耦解释了 PermG 对 entropy 通道失效
- ECE→distinct_{1,2,3} 是 3B 模型唯一 PermG-robust 的 canary-downstream 组合

报告已保存：`artifacts/smollm3_3b_s43_analysis.md`

---
