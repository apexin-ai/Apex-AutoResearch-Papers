# diagnostic training progress check 20260526

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_training_progress_check_20260526_20260526T174713_result.json`
- **Structured JSON:** [`ce834960ad4154578f92.json`](../../sessions/ce/ce834960ad4154578f92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| # | 实验 | 服务器 | Step | 进度 | 速度 | 预估完成 (UTC) |
|---|------|--------|------|------|------|----------------|
| 1 | spatial_bowl SDF s0 | 35807:0 | 26374/30000 | 88% | 4.64s/it | May 27 ~06:30 |
| 2 | obj_s0 λ=0.1 | 35807:1 | 18100/30000 | 60% | 4.62s/it | May 27 ~17:00 |
| 3 | obj_s1 λ=0.1 | 35807:2 | 17573/30000 | 59% | 4.63s/it | May 27 ~17:45 |
| 4 | spatial_bowl lora baseline | 35807:3 | 7825/30000 | 26% | 4.62s/it | May 28 ~06:15 |
| 5 | lora_baseline s2 | 45947:0 | 15497/30000 | 52% | 4.60s/it | May 27 ~20:15 |
| 6 | obj_s2 λ=0.1 | 45947:1 | 5847/30000 | 19% | 4.60s/it | May 28 ~08:40 |

**关键发现：**
- **spatial_bowl SDF 不需要 resume**，速度从 9s/it 降到 4.64s/it，~5h 内完成
- **λ=0.1 三个 seed**：s0/s1 进度接近（60%/59%），s2 因启动晚仅 19%
- **所有 GPU 100% 利用率**，无 OOM/NaN/loss spike
- 报告已写入 `artifacts/training_progress_20260527.md`

---
