# ops check all gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_gpu_status_20260520T092143_result.json`
- **Structured JSON:** [`b51ef8343cc27f6b107f.json`](../../sessions/b5/b51ef8343cc27f6b107f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## bjb1-40020 (2× RTX 4090)

| GPU | 实验 | PID | 状态 | 当前步数 | train_return |
|-----|------|-----|------|----------|-------------|
| 0 | exp_027_tcn_walker_s0_sigma02 (σ=0.2 s0) | 37873 | ✅ 运行中 (14% util) | **160,000** | 689.5 |
| 0+1 | exp_029a_tcn_walker_s1_sigma02 (σ=0.2 s1) | 50924 | ✅ 运行中 (17% util) | **28,000** | ~155 |
| — | exp_028_rave_walker_s0_ceil15 | 38382(已死) | ❌ **中断** — 无 EXIT_CODE，PID 不在 nvidia-smi | 136,000 | ~50 |

## bjb1-45299 (2× RTX PRO 6000 Blackwell)

| GPU | 实验 | PID | 状态 | 当前步数 | train_return |
|-----|------|-----|------|----------|-------------|
| — | exp_027_tcn_walker_s0 (σ=0.5 s0) | — | ✅ **已完成** (EXIT_CODE=0) | **220,000** | ~248 |
| 0+1 | exp_027_tcn_walker_s1 (σ=0.5 s1) | 888926 | ✅ 运行中 (32% util) | **112,000** | ~389 |
| — | exp_028_rave_walker_s0 | — | ❌ **被杀** (EXIT_CODE=129 / SIGHUP) | 112,000 | ~82 |

### 需要关注的问题

1. **bjb1-40020 exp_028 (RAVE ceil15)** — 进程静默死亡，日志最后停在 step 136000，无错误信息。PID 38382 已不存在。GPU 0 现在被 exp_027 和 exp_029a 共享。
2. **bjb1-45299 exp_028 (RAVE)** — EXIT_CODE=129 (SIGHUP)，在 step 112000 被终止。
3. **bjb1-45299 exp_027 s0 已完成** — 220K 步训练完毕，GPU 0 空闲（仅 526MiB 占用），可用于新任务。

---
