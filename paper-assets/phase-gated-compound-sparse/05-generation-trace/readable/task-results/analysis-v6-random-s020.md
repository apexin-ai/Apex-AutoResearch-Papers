# analysis v6 random s020

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6_random_s020_20260514T054901_result.json`
- **Structured JSON:** [`0cc32183dabd14ccda18.json`](../../sessions/0c/0cc32183dabd14ccda18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v6_random_s020 已完成，registry 更新为 DONE。

**结果摘要：**

| | random (v6_random_s020) | importance (v6_importance_s020) |
|---|---|---|
| II high mean | 0.856 | 0.494 |
| II mid mean | 1.258 | 4.954 |
| II low mean | 0.957 | 25.876 |
| 梯度 (low/high) | **1.12×** | **11.05×** |
| per_problem_ii_count | 50 | 50 |

Random masking 三个 phase 的 II 值在 0.86-1.26 之间，梯度接近 1×（平坦），与预期一致——随机剪枝不产生系统性的 phase 依赖交互。Importance masking 的 11× 梯度则表明 importance-based pruning 在 low-sparsity phase 引发显著更强的注意力交互。

JSON 中没有 bootstrap_gradient_paired/unpaired 字段（可能该版本分析脚本未计算），但 per_problem_ii 数据完整（50 问题），可直接用于 problem-level permutation test。

---
