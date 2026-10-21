# analysis 14d ablation bootstrap v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14d_ablation_bootstrap_v2_20260517T125200_result.json`
- **Structured JSON:** [`458ebf5056adf32f6803.json`](../../sessions/45/458ebf5056adf32f6803.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成（耗时 1173s ≈ 19.5 min）。以下是完整汇总：

## 14D vs 15D Feature Ablation 结果（去除 self_bleu）

| Model | K\*\_15D | K\*\_14D | K\* 变化? | 1v2 AUC\_15D [CI] | 1v2 AUC\_14D [CI] | Delta |
|-------|---------|---------|-----------|-------------------|-------------------|-------|
| Qwen-base | 2 | 2 | **不变** | 0.6288 [0.6197, 0.6379] | 0.6258 [0.6163, 0.6350] | -0.0031 |
| Pythia | 2 | 2 | **不变** | 0.8840 [0.8775, 0.8904] | 0.8830 [0.8764, 0.8894] | -0.0010 |
| LLaMA-8B | 2 | 2 | **不变** | 0.6075 [0.5979, 0.6171] | 0.6074 [0.5978, 0.6170] | -0.0001 |
| Mistral-7B | 1 | 1 | **不变** | 0.5902 [0.5801, 0.6001] | 0.5903 [0.5803, 0.6003] | +0.0002 |

## 结论

**去除 self_bleu 对 K\* 判定无任何影响。** 所有 4 个模型的 K\* 在 14D 和 15D 下完全一致。

AUC 差异（Delta）极小：
- 最大绝对 Delta 仅 0.0031（Qwen-base 1v2 pair），远小于 CI 宽度（~0.018）
- 所有 pair 的 14D CI 与 15D CI 高度重叠，差异无统计显著性

**对 Critical #3 的回应：** self_BLEU 特征的移除不改变任何模型的污染深度判定（K\*），且对分类器 AUC 的影响在统计噪声范围内（|Δ| < 0.008），说明我们的方法对该特征不存在过度依赖。

---
