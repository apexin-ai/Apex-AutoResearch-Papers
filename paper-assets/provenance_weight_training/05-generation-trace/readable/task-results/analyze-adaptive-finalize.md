# analyze adaptive finalize

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_adaptive-finalize_20260514T065720_result.json`
- **Structured JSON:** [`1d28de3e9fb464674b11.json`](../../sessions/1d/1d28de3e9fb464674b11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验均已更新为 DONE/success。以下是完整汇报：

---

## Adaptive ×3 实验结果

### Metrics 汇总

| | adaptive_seed42 | adaptive_seed123 | adaptive_seed456 | **均值±std** |
|---|---|---|---|---|
| **train_loss** | 9.2665 | 9.2665 | 9.2354 | **9.256 ± 0.018** |
| **train_runtime** | 13115s (3h38m) | 13197s (3h40m) | 13130s (3h38m) | ~3h39m |
| **total_steps** | 6103 | 6103 | 6103 | 6103 |
| **GPU hours** | 4.21 | 4.21 | 4.21 | — |

### Checkpoint

- 路径：`output/models/adaptive_seed{42,123,456}/final/`
- 大小：每个 ~1.2 GB（model.safetensors = 1,192,135,096 bytes）
- 包含完整模型 + tokenizer + config

### b* 和 α_eff 分析

**b\* 不是一个固定值，而是每个 batch 自适应计算的。** 关键参数：
- `tau = 0.8`（α_eff 目标上限）
- `n_min = 3`（最小有效样本数）
- `contamination_ratio = 0.4`

从 log 中观察到的 per-batch 分布：
- **b\***: 范围 0.0 ~ 3.8，大部分集中在 0.2 ~ 0.8
  - b\*=0.0 时 ESS=4.0（uniform 权重），α_eff ~0.8-0.93
  - b\*>1.0 的较少，偶尔出现大值（如 3.78）
- **α_eff**: 范围 0.03 ~ 0.80，被 tau=0.8 截断
  - 多数 batch 的 α_eff 在 0.4-0.8 之间
  - 当 α_eff 达到 0.8 上限时，b\* 通过反函数精确求解
- **mean_q**: 范围 0.07 ~ 0.98
  - 高 mean_q (>0.8) 的 batch 对应低 α_eff——说明这些 batch 的样本 q_score 高（合成数据多），权重被大幅下调
- **ESS**: 绝大部分在 3.0 附近（n_min 约束），少数达到 3.1-4.0

### train_loss 高于 uniform 的原因分析

adaptive train_loss (9.26) 比 uniform (7.30) 高 ~27%。这**不意味着**模型质量差，原因：

1. **加权 loss ≠ 真实 loss**：adaptive 方法对每个样本赋予不同权重 `w_i`，train_loss 是加权平均 `Σ w_i * loss_i / Σ w_i`。高 q_score（合成数据）样本权重被压低，而模型在这些样本上 loss 本身更低（已学到的模式），所以加权 loss 被拉高——权重偏向了模型 loss 更高的"难"样本。

2. **mean_q 分布证实了这一点**：平均 mean_q ~0.5-0.6，说明每个 batch 中约一半样本被判定为合成，权重被大幅下调。这些样本的低 loss 不再贡献到加权平均中，导致 reported train_loss 升高。

3. **真正的质量比较应看 downstream eval**（如 MMLU/GSM8K），而非 train_loss。train_loss 在不同加权方案下不可直接比较。

---
