# ops check 3 experiments status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-3-experiments-status_20260519T021343_result.json`
- **Structured JSON:** [`e48213461c2c452ce1d2.json`](../../sessions/e4/e48213461c2c452ce1d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| 实验 | 状态 | 当前 step | 目标 | 进度 | train_return | 预估剩余 |
|------|------|-----------|------|------|-------------|----------|
| exp_001_baseline_s3 | **running** (PID 774106) | 72K | 105K | 68.6% | 606.84 | ~1.1h |
| exp_023_cheetah_baseline_s3 | **running** (PID 768897) | 152K | 200K | 76.0% | 628.69 | ~1.4h |
| exp_023_cheetah_baseline_s4 | **running** (PID 774033) | 85K | 200K | 42.5% | — | ~3.2h |

**预估依据**：根据进程启动时间和当前 step 推算平均速率：
- exp_001: ~514 steps/min (启动于 07:54, 2h20m 跑到 72K)
- exp_023_s3: ~576 steps/min (启动于 05:50, 4h24m 跑到 152K)
- exp_023_s4: ~607 steps/min (启动于 07:54, fps=9.84, 与墙钟估计吻合)

exp_023_cheetah_baseline_s4 metrics 中 value_mean=196.92, imag_reward_mean=0.48。

---

### nvidia-smi 摘要 (RTX PRO 6000 Blackwell ×2, 97.9GB each)

| GPU | VRAM 使用 | 利用率 | 进程数 | 主要负载 |
|-----|----------|--------|--------|---------|
| cuda:0 | 5,213 MiB / 97,887 MiB (5.3%) | 21% | 2 | exp_023_s4 (4669MB) + exp_023_s3 溢出 (515MB) |
| cuda:1 | 8,851 MiB / 97,887 MiB (9.0%) | 75% | 2 | exp_023_s3 (4156MB) + exp_001_s3 (4671MB) |

另外注意：有一个 `exp_008a_cheetah_unexposed_s0` 的 tmux session 存在 (PID 748622, May18 启动)，但其 python 进程未出现在 nvidia-smi 中，可能已结束。

---
