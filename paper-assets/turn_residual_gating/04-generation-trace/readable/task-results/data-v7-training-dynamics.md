# data v7 training dynamics

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_v7_training_dynamics_20260518T201309_result.json`
- **Structured JSON:** [`b6d4f8aa42747cbadda9.json`](../../sessions/b6/b6d4f8aa42747cbadda9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已生成。汇报如下：

## 数据收集结果

**行数统计：**
- 训练输出行 (Epoch)：124 条
- GATE 统计行：16 条 (gs 0-750, 每 50 gs 一条)
- GATE profile 行：8 条 (gs 0-700, 每 100 gs 一条)
- CSV 总行数：125 (含 header)

**训练进度：**
- 最后一条：micro_step 6150, global_step 768.8
- Gate mean 收敛至 ~0.96

**CSV 前 5 行：**
| micro_step | gs | L_NTP | L_GAR | mean_GAR |
|---|---|---|---|---|
| 0 | 0.0 | 2.0275 | 0.2342 | 0.0161 |
| 50 | 6.2 | 1.7218 | 0.2349 | 0.0153 |
| 100 | 12.5 | 1.3103 | 0.2337 | 0.0166 |
| 150 | 18.8 | 1.6785 | 0.2277 | 0.0228 |
| 200 | 25.0 | 1.4617 | 0.2348 | 0.0154 |

**CSV 后 5 行：**
| micro_step | gs | L_NTP | L_GAR | mean_GAR |
|---|---|---|---|---|
| 5950 | 743.8 | 0.9011 | 0.0002 | 0.4859 |
| 6000 | 750.0 | 0.8836 | 0.0061 | 0.4219 |
| 6050 | 756.2 | 0.7173 | 0.0009 | 0.4700 |
| 6100 | 762.5 | 1.3465 | 0.0000 | 0.5000 |
| 6150 | 768.8 | 0.7768 | 0.0002 | 0.4859 |

## 三阶段拐点

| 阶段 | 范围 (gs) | 范围 (micro) | mean_GAR |
|---|---|---|---|
| **Phase A** | 0 - 75 | 0 - 600 | ~0.015-0.033 平台 |
| **A→B 拐点** | **gs 75** | **micro 600** | 0.033 → 0.066 开始加速 |
| **Phase B** | 75 - 144 | 600 - 1150 | 0.033 → 0.434 加速上升 |
| **B→C 拐点** | **gs ~144** | **micro ~1150** | 跳至 0.43，此后收敛 |
| **Phase C** | 144+ | 1150+ | ~0.43-0.50 收敛波动 |

**文件路径：**
- CSV: `/root/turn_residual_gating/runs/v7_training_dynamics.csv`
- 原始 GATE 统计: `/root/turn_residual_gating/runs/v7_gate_stats.txt`
- 原始 GATE profile: `/root/turn_residual_gating/runs/v7_gate_profiles.txt`
- 原始训练输出: `/root/turn_residual_gating/runs/v7_training_output.txt`

---
