# status all 4 exp progress loop23

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_all-4-exp-progress-loop23_20260522T054959_result.json`
- **Structured JSON:** [`d99a19b57efa0cedcd4e.json`](../../sessions/d9/d99a19b57efa0cedcd4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

---

### 服务器 1: bjb1-45299 (2× RTX PRO 6000 Blackwell)

**GPU**: GPU0 21%, 4067/97887 MiB | GPU1 34%, 3017/97887 MiB

| 实验 | 状态 | Step | 进度 | 最新 eval_return | ve_ratio | FPS | 预估剩余 |
|------|------|------|------|-----------------|----------|-----|---------|
| **exp_040** wide_dual_critic_cheetah | **DEAD** (PID 36013 不存在) | 100K/210K | 47.6% | 149.9 (@95K) | 0.107 (@95K) | 9.3 | — |
| **exp_041** dual_critic_walker_s3 | **ALIVE** (3h12m) | 116K/210K | 55.2% | 491.2 (@115K) ★ peak 604.3 (@105K) | 0.283 (@115K) | 9.55 | ~2h45m |

---

### 服务器 2: bjb1-40020 (2× RTX 4090)

**GPU**: GPU0 13%, 3564/24564 MiB | GPU1 17%, 2523/24564 MiB

| 实验 | 状态 | Step | 进度 | 最新 eval_return | ve_ratio | FPS | 预估剩余 |
|------|------|------|------|-----------------|----------|-----|---------|
| **exp_042** frozen_dt_emb_walker | **ALIVE** (3h12m) | 92K/210K | 43.8% | 378.3 (@85K) ★ peak 453.5 (@75K) | 0.112 (@85K) | 7.66 | ~4h17m |
| **exp_043** 008f_walker_s1 | **ALIVE** (3h14m) | 96K/210K | 45.7% | 250.8 (@95K) ★ peak 332.7 (@75K) | 0.427 (@95K) | 7.91 | ~4h00m |

---

### 关键发现

1. **exp_040 已死**，停在 step 100K (47.6%)。GPU0 仍占 4GB 显存但无活跃进程。无法用 read_only 查 tmux，需要 ssh_execute 检查 `tmux ls` 或重启。

2. **exp_041 表现最好**：eval_return 在 105K 达到 604，当前 115K 回落到 491，ve_ratio 0.283。Walker 环境，dual critic，seed 3。

3. **exp_043 的 ve_ratio 最高 (0.427)**，但 eval_return (250.8) 明显低于 exp_042 (378.3)，说明 gate 开了但 policy 质量不如 frozen_dt_emb 变体。

4. **所有存活实验的 gate_dt 都锁死在 dt=2**（gate_dt_2_frac=1.0, entropy=0），gate 没有学到多样化的时间步长选择。

---
