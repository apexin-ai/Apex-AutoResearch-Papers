# check exp028c latest status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_latest_status_20260516T025544_result.json`
- **Structured JSON:** [`75d5dcf9e450d4536fcc.json`](../../sessions/75/75d5dcf9e450d4536fcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp028c 训练状态报告

### 进程状态
- **存活**: PID 824675, 运行 5h18m
- **当前进度**: step 6/100 完成 (6%), step 7 训练中
- **GPU**: 0%, 1% util — 快照捕获到 compute 间隙, 各占 33.2/97.9 GB (34%)

### Step 5 Val 数据 (16 episodes) ✅ 已完成

| 指标 | Step 0 (baseline) | Step 5 | 变化 |
|------|-------------------|--------|------|
| **success** | 6.25% (1/16) | **6.25% (1/16)** | 持平 |
| **pass@1** | 6.25% | **6.25%** | 持平 |
| **action_is_valid** | 74.5% | **96.5%** | +22pp ↑↑ |
| action_is_effective | 95.0% | 100% | +5pp ↑ |
| num_actions | 44.9 | 49.4 | +4.5 |
| val-core reward mean | 0.119 | **0.518** | 4.4x ↑↑ |

### Train Metrics 趋势

| Step | success | pass@8 | action_is_valid | entropy | kl_loss | grad_norm |
|------|---------|--------|-----------------|---------|---------|-----------|
| 1 | 13.3% | 37.5% | 76.4% | 0.263 | 0.013 | 16.9 |
| 2 | 6.3% | 25.0% | 83.2% | 0.247 | 0.171 | 17.3 |
| 3 | 15.6% | 68.8% | 85.9% | 0.249 | 0.112 | 12.6 |
| 4 | 18.8% | 62.5% | 87.9% | 0.234 | 0.031 | 14.5 |
| 5 | 9.4% | 37.5% | 89.6% | 0.236 | **0.824** | 13.1 |

### 异常/注意事项
- **KL loss 在 step 5 飙升到 0.824**（前 4 步在 0.013–0.171），需要监控后续是否回落
- Val success 未提升（仍 6.25%），但 16-episode 方差大，需等更多 val 点
- **action_is_valid 持续稳步上升**（train: 76% → 90%, val: 74.5% → 96.5%），这是积极信号
- val-core reward 4.4x 提升表明 rollout 质量在改善

### 速度 & 预估完成时间
- 平均 ~51 min/step（含 val 的 step 约 60 min）
- 剩余 94 steps，约 **82 小时 ≈ 3.4 天**
- 预计完成: **~5月19日 16:00 UTC**
- Checkpoint: 仅 `global_step_5`（save_freq=5，下次 step 10）
- 下次 val eval: step 10

---
