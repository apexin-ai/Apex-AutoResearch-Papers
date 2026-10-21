# analysis act activation drift

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_act-activation-drift_20260520T234652_result.json`
- **Structured JSON:** [`026207469d880f9f059a.json`](../../sessions/02/026207469d880f9f059a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已生成。结果摘要：

### exp-004 ACT Activation Drift 结果

| 指标 | ckpt-4000 (dip) | ckpt-5000 (recovery) | Δ |
|---|---|---|---|
| proj_user AUROC | 0.3189 | 0.3203 | **+0.0014** |
| proj_asst AUROC | 0.3337 | 0.3467 | **+0.0130** |
| proj_user mean_diff | -2.525 | -2.423 | +0.103 |
| proj_asst mean_diff | -0.410 | -0.304 | +0.106 |

### ACT vs GRPO 对比

| | ACT (exp-004) | GRPO (exp-003) |
|---|---|---|
| proj_user AUROC shift | **+0.0014** (恢复) | **-0.0073** (继续退化) |
| proj_asst AUROC shift | **+0.0130** (恢复) | **-0.0038** (继续退化) |
| AUROC 恢复? | **Yes** | **No** |

### 关键发现

1. **ACT 的 d_syc 方向投影 AUROC 在 dip→recovery 过程中轻微恢复**（+0.0014 user, +0.0130 asst），而 GRPO 持续下降（-0.0073, -0.0038）。这与 SYCONScore 的行为一致。

2. **ACT 的 AUROC 绝对值远高于 GRPO**（0.32-0.35 vs 0.16-0.23），说明 ACT 训练后模型在 L19 对 valid/invalid 的表征分离度比 GRPO 更强。

3. **Drift 幅度较小**：Wasserstein 距离仅 0.15-0.22，说明 ACT 的 ckpt-4000→5000 之间激活变化平缓，不像 GRPO 那样发生剧烈表征漂移。

产出文件：
- `projection_stats.json` — 完整统计
- `comparison_with_grpo.json` — ACT vs GRPO 对比
- `projection_histogram.png` — 4-panel 可视化
- `raw_projections.json` — 原始投影数据

---
