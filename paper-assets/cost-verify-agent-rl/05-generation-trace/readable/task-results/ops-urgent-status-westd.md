# ops urgent status westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-westd_20260518T024343_result.json`
- **Structured JSON:** [`bd08c531ee223a9d3783.json`](../../sessions/bd/bd08c531ee223a9d3783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 状态（并非 0% 利用率）

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 52% | 45.0/97.9 GB | factorial generate_sequences |
| 1 | 54% | 45.0/97.9 GB | factorial generate_sequences |
| 2 | 100% | 24.7/97.9 GB | gsweep compute_log_prob |
| 3 | 96% | 24.7/97.9 GB | gsweep compute_log_prob |

---

### Factorial (h2_episode_adv) — 运行中

- **进度**: 47% (7/15 steps), 已运行 ~6h, ETA ~7h
- **Checkpoint**: `global_step_5`
- **KL**: 稳定 0.024–0.040，无异常

**Train success 趋势**:
| step | 1 | 2 | 3 | 4 | 5 |
|------|-------|-------|-------|-------|-------|
| success | 20.3% | 6.3% | 5.5% | 3.1% | 15.6% |

**Val (step 0, OOD)**: success=2.2%, reward_mean=0.08

**Step 5 val reward 指标** (对比 step 0 明显提升):
- best@64: 7.89 (was 4.33)
- best@128: 9.58 (was 6.5)
- critic/score/mean: 0.768 (was 0.08)

**评估**: 正在学习。Train success 有波动但 step 5 恢复到 15.6%，reward 指标持续上升。需等 step 10 val 确认。

---

### Gsweep g050 (h5) — 运行中但已崩溃

- **进度**: 80% (12/15 steps), 已运行 ~11.5h, ETA ~5h
- **Checkpoint**: `global_step_10`

**Train success 趋势**:
| step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|---|
| success | 0% | 1.6% | 0.8% | 0% | 2.3% | 0% | 0% | 0% | 0% | 0% |

**Val success**: step 0=9.4% → step 5=0% → step 10=0%

**KL 序列**: 0.019, 0.025, 0.018, 0.014, 0.010, 0.009, 0.009, **0.209** (step 8 爆炸), 0.018

**Step 10 val**: 所有 reward 指标 = 0.0, critic/score = 0.0, response_length 从 49 暴涨到 1412

**评估**: **完全崩溃**。从 step 1 起 train success 基本为 0，step 8 KL 爆到 0.209（20 倍正常值）。模型在浪费 GPU 时间。

---

### Watchdog 状态
- tmux session `gsweep_watchdog` 运行中
- 尚未启动 g080（等 g050 进程结束）

---

### 建议
gsweep g050 已完全崩溃，剩余 3 步 (~5h) 纯属浪费 GPU 2,3。是否要 kill 掉 g050 让 watchdog 提前启动 g080？

---
