# analysis bf16 ds imp vs rand

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16-ds-imp-vs-rand_20260514T071001_result.json`
- **Structured JSON:** [`04db8e868491920fa4d1.json`](../../sessions/04/04db8e868491920fa4d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果非常清晰。

## 结果摘要

### Per-Sparsity 对比

| Sparsity | Imp 梯度 (median) | Rand 梯度 (median) | Imp 单调性 | Rand 单调性 | Perm p | Wilcox p | imp>rand |
|----------|-------------------|-------------------|-----------|-----------|--------|----------|----------|
| **s015** | 0.3508 | 0.0110 | 50% | 10% | 0.0001 | 3.1e-05 | 36/49 |
| **s020** | 1.1363 | 0.0434 | 72% | 18% | 0.0001 | 8.0e-07 | 39/49 |
| **s025** | 4.0174 | 0.3032 | 82% | 25% | 0.0001 | 2.4e-08 | 42/49 |

**Pooled** (147 problems): Perm p=0.0001, Wilcox p=2.8e-15

### 关键发现

1. **Importance masking 梯度随 sparsity 强单调递增**：0.35 → 1.14 → 4.02 → 9.95 (s030)
2. **Random masking 梯度几乎平坦**：0.01 → 0.04 → 0.30（仅 s025 略有上升）
3. **Importance 单调性远高于 random**：50%→72%→82%→90% vs 10%→18%→25%
4. **所有 sparsity level 的 permutation test 和 Wilcoxon test 均高度显著**（p < 0.001）
5. 每个 sparsity level 中，>73% 的 problem 的 importance 梯度大于 random 梯度

结果已保存至 `/root/autodl-tmp/pacs/analysis_bf16_ds_comparison.json`。

---
