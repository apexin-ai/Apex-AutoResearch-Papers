# analysis power artifact simulation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_power-artifact-simulation_20260522T102844_result.json`
- **Structured JSON:** [`f7f3c95429fa1710b224.json`](../../sessions/f7/f7f3c95429fa1710b224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有产出已注册。

## 结果摘要

| 模型 | γ (onset scaling) | R² | 含义 |
|------|-------------------|-----|------|
| **H0 (linear signal)** | 0.85 | 0.977 | 纯 power artifact 预测 |
| **H1 (step transition)** | 1.96 | 0.920 | 理论 phase transition 模型 |
| **Observed** | **2.08** | — | 实验观测值 |

**结论: `real_transition`** — H0 的 apparent onset 遵循 T^{−0.85}（来自 F-test √T power scaling + df 效应），与观测的 T^{−2.08} 差距 Δγ = 1.24。这是结构性差异：smooth signal 模型无论怎么调参，其 power-law exponent 都被 PermG 检验的统计功效 scaling 约束在 ~0.5–1.0 范围，无法达到 2.08。

观测到的 steep scaling 需要信号结构本身存在 phase transition，而非仅靠检测功效随 T 增长。

### 产出文件
- `artifacts/power_simulation/power_artifact_test.json` — 完整数据
- `artifacts/power_simulation/power_artifact_test.py` — 可复现脚本
- `artifacts/power_simulation/power_artifact_comparison.pdf/png` — 3-panel 对比图
- `artifacts/power_simulation/power_artifact_analysis.md` — 分析报告

---
