# analysis exp016 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp016_bootstrap_ci_20260516T045403_result.json`
- **Structured JSON:** [`f9beb0c2a62a78cae146.json`](../../sessions/f9/f9beb0c2a62a78cae146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新，artifact 已注册。

---

## exp-016 Bootstrap CI 结果

### 关键结论：1v2 CI lower = 0.6168 > θ=0.60 → **PASS**

| Pair | AUC | 95% CI | Perm p |
|------|-----|--------|--------|
| 0v1 | 0.9870 | [0.9853, 0.9885] | <0.0001 |
| **1v2** | **0.6260** | **[0.6168, 0.6353]** | **<0.0001** |
| 2v3 | 0.5496 | [0.5397, 0.5600] | <0.0001 |
| 3v4 | 0.5293 | [0.5188, 0.5399] | <0.0001 |
| 4v5 | 0.5181 | [0.5075, 0.5288] | 0.0016 |

方法: GroupKFold(5) OOF + doc-level bootstrap (10K) + label permutation (10K)

### 分析

1. **1v2 CI lower=0.6168 稳健地高于 θ=0.60**，尽管 fold 0 的 1v2=0.5963 < 0.60，aggregate 层面无问题
2. **所有 5 个 pairs 统计显著** (p ≤ 0.0016)，4v5 的 p=0.0016 最大但仍远低于 0.05
3. **2v3 CI upper=0.56 < 0.60**，干净地确认 K*=2 边界

### 与 exp-017 (Instruct) 对比

| | Base (exp-016) | Instruct (exp-017) |
|--|---|---|
| 1v2 AUC | 0.626 | 0.6114 |
| 1v2 CI | [0.6168, 0.6353] | [0.6015, 0.6213] |

两个 CI 有重叠 [0.6168, 0.6213]，base 和 instruct 的 1v2 区分度无显著差异。K*=2 不是 instruct-tuning 的副产物。

---
