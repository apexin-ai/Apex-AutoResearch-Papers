# eval tau 06 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau_06_seed42_20260515T134959_result.json`
- **Structured JSON:** [`82eee0d562a15c801f13.json`](../../sessions/82/82eee0d562a15c801f13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

---

## tau_06_seed42 Eval 结果

| 配置 | PPL | Δ vs τ=0.8 | Δ vs uniform |
|------|-----|-----------|-------------|
| **τ=0.6 (本次)** | **17.681** | **+0.031 ↑** | **-0.009 ↓** |
| τ=0.8 (adaptive_fix) | 17.650 | baseline | -0.040 |
| uniform | 17.690 | +0.040 | baseline |

### 训练指标
- total_steps: 6103, train_loss(last100): 2.3053, unweighted_loss: 2.0058
- training_hours: 3.76

### b 分布（τ=0.6 的权重调节参数）
- mean=0.590, median=0.375, std=1.069
- 分布：zero=15.6%, (0,0.5)=47.1%, [0.5,1)=23.8%, [1,2)=9.0%, ≥2=4.4%
- alpha_eff 在大多数 step 被 clamp 到 τ=0.6（比 τ=0.8 更激进）

### 结论

**τ=0.6 略微恶化 PPL（+0.031 vs τ=0.8）**。更激进的降权（更低的 α_eff 下限）并未带来额外收益，反而有轻微质量损失。τ=0.6 的 PPL 与 uniform 基本持平（17.681 vs 17.690），说明过度降权抵消了 adaptive weighting 的优势。

这支持 τ=0.8 是更优的阈值选择：足够激进地降权可疑数据，但不至于过度。τ 的 sensitivity 在 [0.6, 0.8] 范围内表现平坦但 0.8 更优，为 Claim 3（τ 作为 robust hyperparameter）提供了边界证据。

---
