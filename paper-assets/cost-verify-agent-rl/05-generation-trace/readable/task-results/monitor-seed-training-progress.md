# monitor seed training progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_seed_training_progress_20260521T111837_result.json`
- **Structured JSON:** [`2dc90e2dfa923ee11a1b.json`](../../sessions/2d/2dc90e2dfa923ee11a1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `worker_outputs/seed_training_progress_20260521.md`。

**核心发现**：

| Seed | Step | Train Success | Val Success (step 5) | ETA |
|------|------|---------------|----------------------|-----|
| seed4 (bjb1) | 5/15 (33%) | 0.148 | 0.094 (step 0 only) | ~00:30 May 22 |
| seed5 (westd) | 9/15 (60%) | 0.438 | 0.063 | ~21:00 today |
| seed6 (westd) | 8/15 (53%) | 0.422 | **0.219** | ~21:30 today |

**需关注**：
- **seed4 训练成功率显著偏低**（0.13-0.15 vs 其他 seed 的 ~0.42），且速度最慢（~30min/step vs ~18-20min/step）
- **seed5 train-val gap 大**：train 0.44 但 val 只有 0.063
- **seed6 表现最佳**：val success 0.219 最高，response length 在下降（正面信号）
- westd GPU 内存接近满载（95-99%），bjb1 磁盘 79%，均暂无风险

---
