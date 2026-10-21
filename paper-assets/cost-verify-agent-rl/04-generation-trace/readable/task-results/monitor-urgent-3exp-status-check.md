# monitor urgent 3exp status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_urgent-3exp-status-check_20260518T052222_result.json`
- **Structured JSON:** [`56f761b277d6cbd6a8a2.json`](../../sessions/56/56f761b277d6cbd6a8a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已齐。汇报如下：

---

## factorial_h2_episodeadv_seed1

**当前 step: 9/15**（progress bar 显示 60%，step 8-9 metrics 尚未 flush 到日志）

**Step 10 val: 未到**（当前正在执行 step 10，预计 ~1-2 小时后出 val）

**Val results:**
| step | val success (AlfworldOOD) | action_is_valid |
|------|--------------------------|-----------------|
| 0 (initial) | 2.24% | 0.378 |
| 5 | 5.97% | 0.576 |

**Train metrics (per step):**
| step | success | pass@8 | action_is_valid | kl_loss | entropy |
|------|---------|--------|-----------------|---------|---------|
| 1 | 20.3% | 68.8% | 0.856 | 0.238 | 0.359 |
| 2 | 6.25% | 31.3% | 0.840 | 0.208 | 0.569 |
| 3 | 5.47% | 31.3% | 0.795 | — | 0.617* |
| 4 | 3.13% | 18.8% | 0.837 | 0.638 | 0.617 |
| 5 | 15.6% | 62.5% | 0.799 | 0.735 | 0.699 |
| 6 | **25.8%** | **81.3%** | 0.815 | 0.789 | 0.719 |
| 7 | 17.2% | 43.8% | 0.772 | **1.774** | 0.621 |
| 8-9 | *not logged yet* | | | | |

**注意**: KL loss 从 step 6→7 暴涨（0.789→1.774），action_is_valid 在下降。Train success 波动大（step 6 峰值 25.8%，step 7 回落到 17.2%）。

---

## exp029_episode_level_seed2

**进程状态: ALIVE** (PID 509, elapsed 12:06)

**当前 step: 0/15**（刚完成 initial validation，训练尚未开始第一步）

**Initial val (val_before_train):**
- success: 12.5%
- action_is_valid: 0.783
- pass@1: 12.5%

---

## gsweep_g080_h5_seed1

**当前 step: 3/15**（progress bar 显示 20%，但 step 2-3 metrics 尚未 flush）

**已知 metrics:**
- Step 1: success = **0.0%**, pass@8 = 0.0%, action_is_valid = 0.803, kl_loss = 0.044

**警告**: step 1 success = 0%，pass@8 也是 0%，与其他实验形成鲜明对比。gamma=0.80 + h5 配置在初始阶段完全无正样本。

---
