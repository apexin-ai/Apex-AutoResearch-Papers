# exp single feature p90ppl

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_single_feature_p90ppl_20260517T224525_result.json`
- **Structured JSON:** [`edb01700a12c69a44be0.json`](../../sessions/ed/edb01700a12c69a44be0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### Single-feature RF (p90_ppl only) — Leave-one-model-out CV

| Holdout | 4-class Acc | d0 recall | d1 recall | d2 recall | d3 recall |
|---------|------------|-----------|-----------|-----------|-----------|
| Pythia  | 0.5669     | 0.951     | 0.324     | 0.358     | 0.634     |
| OLMo    | 0.5917     | 0.910     | 0.688     | 0.368     | 0.401     |
| GPT-2 XL| 0.5894     | 0.958     | 0.696     | 0.357     | 0.346     |
| **Mean**| **0.5827** |           |           |           |           |

Std: 0.0112

仅用 p90_ppl 一个特征就达到 58.3% 的 4-class accuracy（随机基线 25%）。d0 recall 在所有 fold 上都很高（>91%），d2 一致最弱（~36%），d1 和 d3 的区分能力在不同 holdout 模型间波动较大。对比全 19 特征的 cross-model LOO（Pythia fold 62.4%），单特征损失约 4-6 个点。

---
