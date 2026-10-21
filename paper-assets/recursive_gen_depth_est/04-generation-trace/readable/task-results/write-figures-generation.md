# write figures generation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_figures_generation_20260515T162403_result.json`
- **Structured JSON:** [`8b1519b3f4c67ee62663.json`](../../sessions/8b/8b1519b3f4c67ee62663.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张图全部完成，已注册 artifacts。

**生成结果汇总：**

| 图 | 文件 | PDF | PNG |
|---|---|---|---|
| Fig 1: AUC Decay | `fig_auc_decay` | 20KB | 143KB |
| Fig 2: Feature Trajectory | `fig_feature_trajectory` | 26KB | 187KB |
| Fig 3: Confusion Matrix | `fig_confusion_matrix` | 29KB | 144KB |
| Fig 4: Atlas Heatmap | `fig_atlas_heatmap` | 28KB | 107KB |

**关键数据来源：**
- Fig 1: 硬编码深度扩展实验 AUC 值，三模型均在 d4v5 跌破 τ=0.75
- Fig 2: 从 `features_all.jsonl`（20000 条 Pythia nucleus 样本）实时计算，含 SEM error bars
- Fig 3: 左 panel 在 20000 样本上训练 RF(n=200) 做 5-fold CV；右 panel 用 `cross_model_loo_detailed.json` holdout_pythia 混淆矩阵
- Fig 4: 从 `summary_9cell.json` 读取 RF 4-class accuracy（GPT-2 XL temp09 最高 85.3%，Pythia topk50 最低 68.7%）

所有文件位于远程 `gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/figures/`。

---
