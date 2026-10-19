# diagnose extract exp029 step40 val

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_extract-exp029-step40-val_20260519T021307_result.json`
- **Structured JSON:** [`55ac682899916ad3e29e.json`](../../sessions/55/55ac682899916ad3e29e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_seed2 Step 40 结果

### Step 40 Val 指标

| 指标 | 值 |
|------|-----|
| success | 0.28125 (9/32) |
| pass@1 | 0.28125 |
| action_is_valid | 0.3629 |
| action_is_effective | 0.4163 |
| manager_invalid_action | 0.5838 |
| num_actions | 8.19 |
| reward/mean@32 | 2.8125 |
| best@8/mean | 9.25 |
| response_length | 2785.5 |

### Step 40 Train 指标

| 指标 | 值 |
|------|-----|
| train success | 0.0625 |
| train pass@8 | 0.25 |
| manager_invalid | 0.8013 |
| ppo_kl | 0.1735 |
| kl_loss | 0.1877 |
| grad_norm | 8.47 |
| entropy | 0.0438 |

### 完整 Val 历史

| Step | success | pass@1 | valid | mgr_invalid | num_actions | reward@32 |
|------|---------|--------|-------|-------------|-------------|-----------|
| 15 (init) | 0.250 | 0.250 | 0.678 | 0.008 | 40.1 | 2.50 |
| 20 | 0.125 | 0.125 | 0.439 | 0.343 | 27.8 | 1.25 |
| 25 | 0.156 | 0.156 | 0.410 | 0.510 | 17.3 | 1.56 |
| 30 | **0.3125** | **0.3125** | 0.477 | 0.467 | 13.0 | **3.125** |
| 35 | 0.281 | 0.281 | 0.357 | 0.591 | 8.0 | 2.81 |
| 40 | 0.281 | 0.281 | 0.363 | 0.584 | 8.2 | 2.81 |

### 训练状态

仍在继续（step 41 正在 generation 中）。tail 显示 anchor_obs 警告和 WorkerDict 初始化，训练未停止。

**关键观察**：val success 峰值在 step 30 (31.25%)，step 35/40 稳定在 28.125%。manager_invalid 从 init 的 0.8% 飙升到 ~58%，num_actions 从 40 压缩到 8，action_is_valid 从 67.8% 降至 36.3%。模型学会了缩短轨迹但代价是大量 invalid action。

---
