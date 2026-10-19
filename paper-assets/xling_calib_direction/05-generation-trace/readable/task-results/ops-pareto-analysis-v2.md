# ops pareto analysis v2

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pareto-analysis-v2_20260521T061545_result.json`
- **Structured JSON:** [`e4d6cb60dec3123745b5.json`](../../sessions/e4/e4d6cb60dec3123745b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。完整结果：

## Pareto Dominance 分析结果（zero_shot, ref=[0.5, 0.5]）

| Language | Hypervolume | Spearman ρ | p-value | Pareto Layers | Tradeoff? |
|----------|-------------|------------|---------|---------------|-----------|
| **ar** | 0.0370 | +0.857 | 0.0065 | [24, 27] | NO |
| **hi** | 0.0369 | +0.310 | 0.4556 | [20, 27] | NO |
| **ko** | 0.0360 | +0.714 | 0.0465 | [24, 27] | NO |
| **sw** | 0.0148 | +0.762 | 0.0280 | [27] | NO |
| **zh** | 0.0456 | +0.857 | 0.0065 | [24, 27] | NO |

**关键发现**：
- **所有 5 种语言均无 depth-transferability tradeoff**（Spearman ρ 全部为正），即更深层 EN probe 质量更高的同时，跨语言 transfer 也更好（或至少不变差）。
- ar/zh/ko 的正相关达到统计显著（p < 0.05），sw 边缘显著（p=0.028），hi 不显著（p=0.456）。
- **Pareto 最优层集中在深层**：layer 24 和 27 主导，hi 额外包含 layer 20。sw 仅 layer 27 为 Pareto 最优（最小 HV=0.0148，transfer 能力最弱）。
- zh 的 HV 最大（0.0456），说明中文 transfer 在 EN probe 质量-transfer 性能空间中覆盖面积最大。

输出文件已写入 `/root/xling_calib_direction/results/pareto/`（`pareto_detail.csv`, `pareto_summary.csv`, `pareto_results.json`）。

---
