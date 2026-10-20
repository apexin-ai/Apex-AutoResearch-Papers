# diagnose quadruped progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_quadruped-progress-check_20260529T080234_result.json`
- **Structured JSON:** [`87dd0d89b88ec47108e0.json`](../../sessions/87/87dd0d89b88ec47108e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_quadruped_baseline_s0_r2 状态：**

| 指标 | 值 |
|------|-----|
| 当前 step | **128,000 / 200,000** (64%) |
| 最新 eval_return | **61.3** (step 125K，较 step 115K 的 173.5 大幅下降) |
| 进程状态 | **存活** (PID 42268, tmux session `exp_quadruped_baseline_s0_r2`) |
| GPU 利用率 | CPU 占用 1209%（多线程），进程正常运行 |
| FPS | ~10.1 |
| CIVO 警报 | **已触发** (step 125K: ve_ratio=6.6, delta_ve=4.3, eval_decline=2/3) |

注意：step 125K 处 CIVO detector 报告了 value expansion 模式，eval_return 从 173.5 (115K) 跌到 61.3 (125K)。这是 baseline 实验（无干预），CIVO alert 仅记录不触发动作。

预计剩余时间：按 10 fps 计算，还剩 ~72K steps ≈ 2 小时。

---
