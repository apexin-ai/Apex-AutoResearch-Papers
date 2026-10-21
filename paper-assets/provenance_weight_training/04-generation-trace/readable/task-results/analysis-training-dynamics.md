# analysis training dynamics

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics_20260516T083653_result.json`
- **Structured JSON:** [`a23e69e90b03d3ed1897.json`](../../sessions/a2/a23e69e90b03d3ed1897.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件在 `artifacts/dynamics/` 下：

| 文件 | 说明 |
|------|------|
| `training_dynamics_data.json` | 原始数据（120个 loss 点 + 62个 b*/alpha 窗口） |
| `fig_loss_curves.py/.pdf/.png` | 三方法 unweighted loss 对比 |
| `fig_bstar_trajectory.py/.pdf/.png` | adaptive b* 轨迹（中位数 + IQR） |
| `fig_alpha_eff_binding.py/.pdf/.png` | alpha_eff 约束触发率 |

**关键发现：**

- **Loss 曲线**：三方法的 unweighted loss 几乎重合（终态 ~2.09），adaptive 没有显著优劣势。曲线非常 noisy（batch size=4 导致方差大）。
- **b* 分布**：整个训练过程高度稳定。中位数 ~0.85，均值 ~1.35（右偏），P25 ~0.54，P75 ~1.50。没有随训练推进的系统性漂移。
- **alpha_eff binding rate**：全程稳定在 ~40%（均值 0.401），无趋势变化。约 40% 的 batch 中 alpha_eff 约束是 binding constraint（而非 ESS 下界）。

注意：step 500/1000/1500 是 eval 步（8481 条 b=0 的记录），已在提取时排除。

---
