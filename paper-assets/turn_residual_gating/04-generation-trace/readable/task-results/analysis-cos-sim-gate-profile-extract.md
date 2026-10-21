# analysis cos sim gate profile extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cos_sim_gate_profile_extract_20260520T024156_result.json`
- **Structured JSON:** [`dd9c0969012e44d46279.json`](../../sessions/dd/dd9c0969012e44d46279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

### Task 1: v7 per-step cos_sim
**v7 仅有 3 个 epoch-level 数据点，无 per-step 粒度。**

v7 训练时未开启 PCGrad，不记录 per-step cos_sim。cos_sim 数据来自 post-hoc 梯度冲突分析（`runs/analysis/gradient_conflict/epoch_{0,1,2}.json`），每个 epoch 在 checkpoint 上用 10 个样本计算：
- epoch 0: cos_sim = -0.089, conflict_fraction = 78.6%
- epoch 1: cos_sim = -0.054, conflict_fraction = 71.4%
- epoch 2: cos_sim = -0.042, conflict_fraction = 67.9%

无需新建文件，已有 `artifacts/cos_sim_trajectory/v7_cos_sim.json` 覆盖此数据。

### Task 2: v9 gate profile
已提取并保存：
- **`artifacts/gate_profile_v9.json`** — v9 PCGrad 28层 turn1 vs turn21 gate 值
- **`artifacts/gate_profile_v7.json`** — v7 对比数据

关键发现：

| 指标 | v7 | v9 PCGrad |
|------|-----|-----------|
| Mean turn1 gate | 0.881 | 0.877 |
| Mean turn21 gate | 0.946 | 0.945 |
| Mean diff | -0.065 | -0.068 |
| Max diff layer | L23 (-0.210) | **L15 (-0.332)** |
| Min gate (turn1) | L14 (0.747) | **L15 (0.625)** |

v9 PCGrad 的最大特点：**L15 出现极端动态范围** — turn1 gate 仅 0.625（远低于 v7 任何层），turn21 升到 0.957，diff = -0.332。这表明 PCGrad 允许特定层学到更大的 turn-dependent 调控幅度，而非 v7 那样所有层趋同。v9 也有 2 个 positive-diff 层（L13, L20），v7 只有 1 个（L19）。

---
