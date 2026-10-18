# analysis rf 21feature augmented

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rf_21feature_augmented_20260518T195603_result.json`
- **Structured JSON:** [`4911ac3921f0b1e76f5f.json`](../../sessions/49/4911ac3921f0b1e76f5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验全部完成。结果已保存到 `augmented_feature_results.json`。

## 结果汇总

### Exp A: 20-feature (19 + Min-K% K20) — 全量 20k, 9 cells

| | 4-class acc | d1-d3 bal acc |
|---|---|---|
| 19-feature | 0.7842 | 0.7160 |
| 20-feature (+mink) | 0.7890 | 0.7220 |
| **delta** | **+0.0048** | **+0.0060** |

Min-K% 在 8/9 cells 上带来正增益，唯一例外是 gpt2xl_topk50 (-0.0022)。最大增益在 olmo_temp09 (+0.0158 acc, +0.0213 bal)。

### Exp B: 21-feature (19 + Min-K% + DetectGPT) — 800 样本子集

**4-class (6 cells, gpt2xl + olmo):**

| | 4-class acc |
|---|---|
| 19-feature | 0.7721 |
| 20-feature | 0.7765 |
| 21-feature | 0.7788 |
| **delta 21 vs 19** | **+0.0067** |

DetectGPT 在 20-feat 基础上额外贡献约 +0.002 的增量，很微弱。

**3-class (2 pythia cells, d1-d3 only, 600 samples):** 21-feat 反而略低于 19-feat (-0.006)，样本太小导致不稳定。

### Exp C: Feature Importance (21-feat RF)

| 特征 | 排名 | Importance |
|---|---|---|
| **mink_k20** | **#3** | 0.0952 |
| **detectgpt** | **#17** | 0.0255 |

Min-K% 排名第3，说明它携带了 19 原始特征未完全覆盖的信息。DetectGPT 排名第17/21，贡献极低，这与其几乎不提升准确率一致。

### 结论
- Min-K% score 是有价值的补充特征（rank #3, +0.48% acc），值得加入。
- DetectGPT perturbation discrepancy 对 RF 几乎无帮助（rank #17, 额外 +0.2% on subset），且只有 200 samples/depth，实用性有限。

---
