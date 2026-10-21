# analysis probe ablation A B

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_probe-ablation-A-B_20260519T202321_result.json`
- **Structured JSON:** [`7bac671b3d34d8cd5f11.json`](../../sessions/7b/7bac671b3d34d8cd5f11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

## 结果表格

| Probe 配置 | AUROC | ±std |
|---|---|---|
| **Multi-layer d_syc (7-dim, exp-008v3)** | **0.8349** | 0.0481 |
| Per-layer: Layer 19 | 0.8166 | 0.0454 |
| Per-layer: Layer 20 | 0.7934 | 0.0479 |
| Per-layer: Layer 24 | 0.7768 | 0.0670 |
| Per-layer: Layer 27 | 0.7923 | 0.0622 |
| Per-layer: Layer 32 | 0.7886 | 0.0649 |
| Per-layer: Layer 33 | 0.7870 | 0.0641 |
| Per-layer: Layer 35 | 0.7818 | 0.0686 |
| **Random-direction (7-dim, 5 seeds)** | **0.7265** | 0.0167 |

## 关键结论

1. **d_syc 方向是关键，不是 multi-layer combination。** Multi-layer（0.8349）相比最佳单层 layer 19（0.8166）仅提升 +0.018，但 d_syc vs random 方向差距达 **+0.108**。方向的质量贡献远大于层数组合的贡献。

2. **Layer 19 单独即可达到接近 multi-layer 的性能（0.8166 vs 0.8349）。** 多层拼接带来的增益很小，主要价值在 d_syc 方向本身。

3. **Random probe 并非 chance（0.5），而是 0.727。** 这说明 reward_layers 的 hidden states 本身包含一定的 condition 信息（valid_correction vs invalid_pressure 的分布差异），但 d_syc 方向精准放大了 sycophancy-relevant 的信号（+0.108 AUROC）。

结果已保存至 `/root/contrastive_entrain_calib/results/probe_ablation_AB/results.json`。

---
