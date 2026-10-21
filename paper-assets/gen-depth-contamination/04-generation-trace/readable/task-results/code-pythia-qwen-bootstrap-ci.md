# code pythia qwen bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pythia_qwen_bootstrap_ci_20260522T212208_result.json`
- **Structured JSON:** [`9d4c986668eabaa18957.json`](../../sessions/9d/9d4c986668eabaa18957.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇报如下：

---

## Pythia Qwen-scored (scorer: Qwen2.5-1.5B)

**所有 depth pair AUC:**

| Pair | AUC | Fold values |
|------|-----|-------------|
| 0v1 | 0.9722 | [0.9763, 0.9711, 0.9726, 0.9665, 0.9742] |
| 1v2 | 0.6074 | [0.5926, 0.6082, 0.6199, 0.6063, 0.6098] |
| 2v3 | 0.5440 | [0.5528, 0.5379, 0.5479, 0.5566, 0.5249] |
| 3v4 | 0.5051 | [0.4959, 0.4889, 0.5130, 0.5072, 0.5207] |
| 4v5 | 0.5079 | [0.5079, 0.5160, 0.5182, 0.5004, 0.4969] |

**K\* = 2** (max depth with AUC > 0.60)

**Bootstrap CI (1v2), 10000 iterations, doc-level, seed=42:**

| Metric | Value |
|--------|-------|
| Point AUC (OOF) | 0.6072 |
| Boot mean ± std | 0.6073 ± 0.0050 |
| **95% CI** | **[0.5975, 0.6172]** |
| **99.5% CI (Bonferroni, α=0.005)** | **[0.5934, 0.6210]** |
| Permutation p-value | 0.0001 |
| 95% CI lower > θ=0.60 | **False** (0.5975) |
| 99.5% CI lower > θ=0.60 | **False** (0.5934) |

**判定：BORDERLINE** — 点估计 0.6074 > 0.60，但 95% CI 下界 0.5975 未越过 0.60 阈值。与自评分版本行为一致（之前 borderline_bootstrap_ci.json 中 exp-021 的 CI 也是 [0.5979, 0.6166]，verdict=BORDERLINE）。

---

## OLMo Qwen-scored (scorer: Qwen2.5-1.5B)

**所有 depth pair AUC:**

| Pair | AUC | Fold values |
|------|-----|-------------|
| 0v1 | 0.9861 | [0.9880, 0.9859, 0.9853, 0.9835, 0.9875] |
| 1v2 | 0.5001 | [0.5263, 0.4991, 0.4932, 0.4750, 0.5068] |
| 2v3 | 0.4972 | [0.5128, 0.4742, 0.5035, 0.4949, 0.5007] |
| 3v4 | 0.5034 | [0.5159, 0.4978, 0.5070, 0.4969, 0.4993] |
| 4v5 | 0.4971 | [0.4943, 0.4999, 0.4999, 0.5023, 0.4892] |

**K\* = 1** (仅 0v1 > 0.60，1v2 已降至随机水平 0.5001)

---

**关键发现：** Pythia Qwen-scored 的 1v2 AUC (0.6074) 与自评分版 (0.6073) 几乎完全一致，bootstrap CI 和 verdict 也匹配。OLMo Qwen-scored 的 1v2 直接降到 0.50，K\*=1，说明 OLMo 合成数据在 depth≥2 后完全不可区分。

---
