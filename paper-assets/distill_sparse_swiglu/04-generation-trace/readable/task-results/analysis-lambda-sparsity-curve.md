# analysis lambda sparsity curve

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lambda_sparsity_curve_20260517T173720_result.json`
- **Structured JSON:** [`7907ed153ce76eedddcc.json`](../../sessions/79/7907ed153ce76eedddcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并保存。

**产出文件：**
- `/root/distill_sparse_swiglu/figures/lambda_sparsity_curve.pdf` (19KB, 矢量)
- `/root/distill_sparse_swiglu/figures/lambda_sparsity_curve.png` (164KB, 1755x1205px @300dpi)

**图表结构：** 两面板共享 X 轴（Training Step），上面板 λ（对数刻度），下面板 sparsity，三条曲线对应 s*=0.3/0.5/0.7，色盲友好配色。

**数据来源：**
- 30% target: `kl_sparsity30_s42_v3.log` (cap=5000, 101 data points, steps 1-1000)
- 50% target: `mvp_kl_norm_v2_s42.log` (cap=1000, 101 points)
- 70% target: `kl_sparsity70_s42_v2.log` (cap=1000, 101 points)

**关键观察：**

| Target | λ 初始 | λ 达到 cap 的 step | 最终 sparsity | 备注 |
|--------|--------|-------------------|---------------|------|
| 30% | 0.50 → 0.01 | ~260 (cap=5000) | 0.285 | 最有趣的动态：λ 先降后升 |
| 50% | 2.0 | ~10 (cap=1000) | 0.488 | λ 几乎立即饱和 |
| 70% | 2.0 | ~10 (cap=1000) | 0.688 | λ 几乎立即饱和 |

**Lagrangian 动态分析：**
- **30% target** 展示最完整的控制回路：自然 sparsity (0.406) > target，λ 先被抑制到 0.01；随着训练推进 sparsity 降到 target 以下，λ 快速指数上升到 cap 5000，形成 U 型曲线
- **50%/70% target** 因初始 sparsity (0.406) 远低于 target，λ 在前 10 步即饱和到 cap 1000，之后靠 KL loss 驱动 sparsity 上升
- 所有三个 target 的最终 sparsity 都略低于目标值（分别差 1.5pp/1.2pp/1.2pp），说明 Lagrangian 机制有效但在 cap 限制下存在系统性偏差

---
