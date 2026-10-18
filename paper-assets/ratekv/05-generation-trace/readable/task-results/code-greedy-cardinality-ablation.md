# code greedy cardinality ablation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_greedy_cardinality_ablation_20260514T061005_result.json`
- **Structured JSON:** [`30ec0cbda08458f139f1.json`](../../sessions/30/30ec0cbda08458f139f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验完成 — 结果摘要

| 条件 | PPL | bit分布 (2/4/8/16) | 
|------|-----|---------------------|
| (a) Greedy unconstrained | **32.45** | 68/30/4/10 |
| (b) Greedy + max_2bit=8 | **11.23** | 8/100/4/0 |
| (c) MCKP constrained k=8 | **11.23** | 8/100/4/0 |

**Delta (b)-(c) = +0.0012** — 实质为零。

**关键发现**：Greedy+constraint 产出了与 MCKP **完全相同的 bit allocation**（2-bit=8, 4-bit=100, 8-bit=4）。PPL 差异仅 0.001，在评估噪声范围内。

**结论**：贡献完全来自 cardinality constraint，而非 MCKP solver 本身。在离散 bit-width {2,4,8,16} 上，greedy 已经是最优的——MCKP 相对 greedy 没有额外优势，性能提升 100% 归因于限制 2-bit head 数量。

---
