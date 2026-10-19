# train per layer analysis

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_per-layer-analysis_20260515T145957_result.json`
- **Structured JSON:** [`5a9d031b7b5bc7b9fe9e.json`](../../sessions/5a/5a9d031b7b5bc7b9fe9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 24 个分类器训练完成。结果汇总：

## Per-Layer 3-Class Accuracy (5-fold CV, 559 samples)

### PaliGemma 层 (mean pooling) — 平均 98.82%

| Layer | Mean Acc | Std |
|-------|---------|-----|
| paligemma_layer_6 | **99.64%** | ±0.44% |
| paligemma_layer_10 | 99.29% | ±0.87% |
| paligemma_layer_12 | 99.28% | ±0.36% |
| paligemma_layer_4 | 99.11% | ±0.80% |
| paligemma_layer_14 | 98.93% | ±1.31% |
| paligemma_layer_8 | 98.75% | ±0.72% |
| paligemma_layer_16 | 98.39% | ±1.19% |
| paligemma_layer_2 | 97.14% | ±1.90% |

### Expert 层 (mean pooling) — 平均 75.89%

| Layer | Mean Acc | Std |
|-------|---------|-----|
| expert_layer_14 | **81.40%** | ±3.29% |
| expert_layer_10 | 75.13% | ±1.99% |
| expert_layer_6 | 74.77% | ±2.89% |
| expert_layer_2 | 72.27% | ±2.08% |

### 关键发现

1. **PaliGemma >> Expert**：PaliGemma 平均 98.82% vs Expert 75.89%，扰动信号主要在视觉编码器中
2. **PaliGemma 最强层**：layer_6（99.64%），中间层信号最强；最弱 layer_2（97.14%），但仍然很高
3. **Expert 层趋势**：随深度递增（72→81%），晚期层 expert_14 最强
4. **first_last pooling 对 Expert 有显著提升**：expert_14 从 81.4% → 94.6%，expert_10 从 75.1% → 91.1%；但对 PaliGemma 无帮助（已接近饱和）
5. **所有 PaliGemma 层几乎饱和**（97-99.6%），区分度有限；Expert 层变异更大，层选择对 routing 更关键

---
