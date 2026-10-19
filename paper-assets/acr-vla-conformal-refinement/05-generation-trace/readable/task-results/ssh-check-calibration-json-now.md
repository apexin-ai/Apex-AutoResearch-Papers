# ssh check calibration json now

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-calibration-json-now_20260520T051720_result.json`
- **Structured JSON:** [`5750e1a2ebb7b7b72771.json`](../../sessions/57/5750e1a2ebb7b7b72771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件存在（9.5MB，27626 steps）。关键摘要部分已完整读取，`per_step_data` 是逐步记录占了绝大部分体积。

## 结果

### go_nogo: **NO-GO**

### 3 个 ρ 值（Spearman）

| 相关性 | ρ | p-value |
|--------|---|---------|
| k1_corr_mag vs k10_var | **0.1523** | 6.37e-143 |
| k2_corr_mag vs k10_var | **0.1340** | 8.66e-111 |
| k1_corr_mag vs k2_l2 | **0.1319** | 1.76e-107 |

### 分布统计

| 指标 | mean | std | P25 | P50 | P75 | P90 |
|------|------|-----|-----|-----|-----|-----|
| k1_correction_magnitude | 0.1208 | 0.0105 | 0.1205 | 0.1205 | 0.1205 | 0.1205 |
| k2_correction_magnitude | 0.1207 | 0.0105 | 0.1205 | 0.1205 | 0.1205 | 0.1205 |
| k10_variance | 0.000481 | 0.000430 | 0.000174 | 0.000372 | 0.000652 | 0.000987 |
| k2_l2_distance | 0.1502 | 0.0800 | 0.0920 | 0.1343 | 0.1890 | 0.2540 |

### 配置

- benchmark: `object`, 10 episodes, seed 42
- CRM checkpoint: `crm_v3_norm/obs_only/crm_best.pt`
- max_correction_norm: 0.2
- total_steps: 27,626

**核心问题**：correction magnitude 几乎是常数（~0.1205），P25–P90 完全相同，说明 CRM 对所有输入输出近乎相同大小的修正向量。ρ 值虽统计显著（p ≈ 0）但效应极弱（0.13–0.15），CRM 信号无法有效区分不确定性高低。

---
