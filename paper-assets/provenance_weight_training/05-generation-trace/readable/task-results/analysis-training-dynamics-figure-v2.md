# analysis training dynamics figure v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics-figure-v2_20260518T204948_result.json`
- **Structured JSON:** [`00b860568dcf98f04d45.json`](../../sessions/00/00b860568dcf98f04d45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成，输出到 westd-41312 上：
- `/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_figure.pdf` (216K)
- `/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_figure.png` (193K)

**实际数据统计**（与 Director 预估有差异）：

| 指标 | 实际值 | Director 预估 |
|------|--------|--------------|
| b* median | 1.11 | 1.11 ✓ |
| b* p99 | 5.72 | 10.22 ✗ |
| α_eff ≥ τ=0.8 | 1.7% | 34.3% ✗ |
| ESS ≤ n_min+0.05 | 22.6% | 67.6% ✗ |

图中标注使用的是 CSV 实际计算值，不是 Director 的预估数字。

**图表内容**：
- **(a)** b* 分布直方图，标注 median=1.11, p99=5.72，右偏（mean=1.39）
- **(b)** α_eff（蓝，左轴）和 ESS（红，右轴）随 step 的 MA-100 曲线，浅色带为 10%-90% 分位范围，虚线标注 τ=0.8 cap 和 n_min=2 阈值

单栏宽度 3.5 inch，300 DPI，学术风格。Caption 需注明使用 ρ=0.6 数据（contamination_60_adaptive_seed456）。

---
