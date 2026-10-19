# infra hsweep status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_hsweep-status-check_20260517T112333_result.json`
- **Structured JSON:** [`3735b59add8b2e007c5d.json`](../../sessions/37/3735b59add8b2e007c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's the report:

---

## hsweep_h2_seed1 状态报告

### 1. 训练进度与 Metrics

**当前 step: 9**（W&B run `7o9bjszm`，PID 920380 运行 7h06m）
**Checkpoint: global_step_5**

| Step | train/success | pass@8 | manager_invalid_action |
|------|-------------|--------|----------------------|
| 1 | 18.75% | 43.75% | 2.7% |
| 2 | 14.84% | 50.0% | 2.0% |
| 3 | 18.75% | 62.5% | 2.8% |
| 4 | **5.47%** | 25.0% | **26.4%** |
| 5 | 1.56% | 6.25% | 36.9% |
| 6 | 3.13% | 25.0% | 47.1% |
| 7 | 4.69% | 18.75% | 50.2% |
| 8 | 1.56% | 12.5% | 54.2% |
| 9 | **0.0%** | **0.0%** | **64.1%** |

**Val (step 0):** success=0.0%, reward/mean@1600=0.0
**Val (step 5):** success=3.13%, manager_invalid_action=78.1%

### 2. GPU 状态
- cuda:0: 96% util, 25881/97887 MiB, 45°C
- cuda:1: 95% util, 25881/97887 MiB, 45°C
- 进程: PID 923806/923807 (`actor_rollout_update_actor`)

### 3. Watchdog 状态
- tmux session `hsweep_watchdog` **存在**（created 15:30:44）
- Pane **内容为空**（scrollback 已清空或脚本在等待状态，无输出）

### 4. auto_next 序列
**已确认为优化版**: `2:1 → 2:2 → 5:1 → 10:1 → 20:1 → full:1 → 2:3 → 5:2 → ...`
- h=2 seed2 会启用 `LOG_PER_SAMPLE_ADV=1` 记录 per-sample advantage

---

### ⚠️ 严重告警：训练已崩溃

Step 3→4 发生剧烈恶化，invalid action 从 2.8% 跳到 26.4%，此后持续恶化至 step 9 的 64.1%，success 率归零。这是典型的 **policy collapse**。训练仍在继续但已无意义——当前 step 9 生成的 response 全部失败，每 step 约 38 分钟的 GPU 时间在做无用功。

需要决策：是否终止当前 run 并分析 step 3→4 之间发生了什么（checkpoint 在 step 5，但 step 5 已经崩了），还是让它跑完看是否能自行恢复。

---
