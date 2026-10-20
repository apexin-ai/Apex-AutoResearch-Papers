# ops extract r22 raw data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_r22_raw_data_20260520T164246_result.json`
- **Structured JSON:** [`0a27851051a64652812a.json`](../../sessions/0a/0a27851051a64652812a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已提取并写入 `artifacts/round22_raw_data_extraction.md`。

---

## 摘要

### T4: Permutation test p-values
- **所有 boundary pair 的 perm_p 均为 0.0001** (= 0/10000 permutations 超过观测值), 包括 exp016, exp018, exp019, exp024, exp025, exp027, exp_gemma2b, 和全部 crossscorer configs
- 例外: retrain-chain 的 permutation_test.json 用不同编码, 其中 exp_008 3v4 p=0.304, exp_olmo 2v3 p=0.998 (这些是 K* 之后的第一个下降对, 不是 boundary pair)
- **exp_gemma2b** 的 3v4 (p=0.2919) 和 4v5 (p=0.3418) 不显著, 符合预期 (K*=1)

### T3: PELT changepoint
- 37 configs 完整列表已提取。18/37 (48.6%) K*_OBD = K*_PELT; 19/37 不一致
- PELT 系统性偏保守 (K*_PELT ≤ K*_OBD), 差值主要为 1

### T2: Fold-level AUC
- 所有 configs 的 1v2 和 2v3 五折 AUC 均已提取 (从 pairwise_auc.json 和 bootstrap_ci.json)
- 数据可直接用于 Youden's J optimal θ 计算

### T6: Generator identity AUC
- **不存在独立的 generator identity classification AUC 指标**
- multi_source 实验仅测量加入 generator label 后 depth classifier 的 AUC 增量
- 增量极小: 平均 Δ(1v2) ≈ +0.01; K* 在所有 domain/config 中未因此改变

---
