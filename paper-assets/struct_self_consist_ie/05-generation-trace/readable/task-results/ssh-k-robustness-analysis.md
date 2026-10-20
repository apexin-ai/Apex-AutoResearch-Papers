# ssh k robustness analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_k-robustness-analysis_20260520T111328_result.json`
- **Structured JSON:** [`37281d015b4b310cf977.json`](../../sessions/37/37281d015b4b310cf977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。所有产出保存在 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/k_robustness/`。

## 结果摘要

### 1. Seed 鲁棒性 (4 seeds: 42/123/456/789)

| Method | Mean F1 | Std | 
|--------|---------|-----|
| vc_weighted | **76.61** | 0.544 |
| lp_weighted | 76.21 | **0.524** (最稳) |
| uniform | 75.56 | 0.585 |
| greedy | 74.81 | 0.033 |
| sj_weighted | 74.19 | 0.615 |
| majority_vote | 72.08 | 1.410 (最不稳) |

### 2. N 鲁棒性 (子采样 N=2,4,6)
- **majority_vote** 对 N 最不敏感（N=2 时仍有 70.56%）
- uniform/lp/vc/sj 在 N=2 时都崩到 ~55.7%（theta=2/N=1.0 时要求 100% 一致）
- N≥4 后差距缩小

### 3. Dropout 韧性
- **uniform** 最抗 dropout（avg drop 仅 0.376pp）
- majority_vote 最差（avg drop 1.722pp，drop=3 时下降 2.9pp）

### 4. Entity Type 分析
- 8 种 entity types，`art` 和 `event` 的方法间差异最大（4.46% / 3.06% range）
- rare types 上所有方法 F1 都低 ~10pp（gap 10-12pp vs common）
- majority_vote 在 rare types 上表现最好（倾向高 recall）

### 5. 综合鲁棒性排名
- **uniform** 和 **lp_weighted** 并列第一（avg rank 2.3）
- uniform 胜在 dropout 韧性，lp_weighted 胜在 seed 稳定性
- vc_weighted 虽然绝对 F1 最高，但 N-sensitivity 和 dropout 排名靠后

---
