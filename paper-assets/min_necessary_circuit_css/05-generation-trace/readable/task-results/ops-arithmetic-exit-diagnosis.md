# ops arithmetic exit diagnosis

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_arithmetic-exit-diagnosis_20260513T035439_result.json`
- **Structured JSON:** [`81f45642794057da5f77.json`](../../sessions/81/81f45642794057da5f77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清除或未以此 ID 创建）。所有更新完成。

---

## 结果汇总

**判定：实验代码正常完成所有 4 个 Phase（A→D），status=DONE，conclusion=negative。**

### 关键 Metrics

| 指标 | 值 |
|------|-----|
| Off-diagonal % | **92.9%** [91.0%, 94.5%] |
| Gate verdict | **PASS_MAIN** (off-diagonal ≥ 10%) |
| CSS 分布 | 1/3: 36, 2/3: 65, 3/3: 17 |
| CIRCUS tiers | core: 915, contingent: 6284, noise: 25292 |
| 3-way Jaccard | 0.144 |
| EAP-IG × Edge-Pruning Jaccard | 0.695 |

### Faithfulness（CPR / CMD）

| Circuit | Edges | CPR | CMD |
|---------|-------|-----|-----|
| **circus_core** | 915 | **+0.927** | 0.302 |
| stable_core | 65 | -0.097 | 4.566 |
| eap_ig | 100 | -0.142 | 4.753 |
| edge_pruning | 100 | -0.177 | 4.900 |
| acdc | 17 | -0.197 | 4.983 |
| css_1.00 | 17 | -0.197 | 4.983 |
| css_0.67 | 82 | -0.201 | 4.999 |
| css_0.33 | 118 | -0.208 | 5.027 |

### 核心发现

- Off-diagonal 92.9% 很高 → CIRCUS-core 中绝大多数边只被 1 个方法选中（方法间分歧大）
- **circus_core（915 edges）** 是唯一有正 CPR 的电路，但它包含了全部 3 个方法的并集，规模大
- 所有小电路（CSS、individual methods、stable_core）CPR 均为负 → zero ablation 下完全不 faithful
- css_1.00 = acdc（17 edges）完全相同 → ACDC isinf binarization 退化问题确认
- conclusion=negative：CSS 融合未带来 faithfulness 改善

### Registry 更新

- status: DONE
- conclusion: negative
- checkpoint_path: `/root/min_necessary_circuit_css/arithmetic_results.json`
- log_path: `/tmp/arithmetic.log`
- metrics: 已写入全部指标
- cron: 无需清除（不存在）

---
