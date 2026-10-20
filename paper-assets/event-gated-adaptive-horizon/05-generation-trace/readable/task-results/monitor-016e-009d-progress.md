# monitor 016e 009d progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_016e-009d-progress_20260515T221750_result.json`
- **Structured JSON:** [`829dbf859c8907199c1b.json`](../../sessions/82/829dbf859c8907199c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

report.md 是自动生成的，无法直接写入。以下是状态汇总：

---

### exp_016e_sgs_walker_s1 (cuda:1, PID 527392)
- **运行中** — uptime 2h41m, CPU 1223%
- **Step: 12,000 / 105,000**
- GPU 1: 23% util, 3278 MiB / 97887 MiB
- **5K eval 已通过，无死锁** — eval_return = 35.48（之前所有版本在此处死锁，现在已修复）
- train_return 在 12K 升至 ~83（8K 时为 ~37）
- gate_dt 仍固定在 2.0（100% dt=2_frac），尚未分化
- **尚未到 15K eval**，按当前速度预计 ~1h 内到达

### exp_009d_baseline_walker_s0 (cuda:0, PID 149708)
- **运行中** — uptime 9h53m, CPU 934%
- **Step: 228,000 / 500,000**（45.6%）
- GPU 0: 4165 MiB / 97887 MiB
- **最新 eval_return @ 218K: 638.19**（新高，稳步上升: 559→591→638）
- train_return @ 228K: ~654
- fps: 7.36
- 228K eval 正在进行中（已写入 eval 起始标记）

### 关键判断
1. **016e 死锁修复确认成功** — 5K eval 两次通过（Logger.video() no-op patch 有效）
2. 009d baseline 表现健康，eval_return 持续攀升，预计还需 ~10h 完成 500K steps

---
