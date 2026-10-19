# ops status check both servers

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_both_servers_20260522T051632_result.json`
- **Structured JSON:** [`c68add9b8605a4fc864f.json`](../../sessions/c6/c68add9b8605a4fc864f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. bjb1-17606 — v4b (ScienceWorld)

| 项目 | 值 |
|------|-----|
| 进程 386364 | **运行中** (Ss+, 已运行 1h07m) |
| 当前进度 | **Step 1/15 (7%)**, ~18:44/step, ETA ~4h22m |
| val success | 0.0 |
| val score | 2.63, final_score 4.84 |
| val reward/mean@32 | **0.484** |
| val response_length | 600.25 |
| action_is_valid | 0.522, action_is_effective 0.969 |
| GPU | cuda:0 46.4/97.9 GB, cuda:1 47.3/97.9 GB, 0% util (step 间歇) |

### 2. westd-47453 — exp029 seed 2048 (Alfworld)

| 项目 | 值 |
|------|-----|
| 进程 79754 | **已结束**, EXIT_CODE=0, 完成于 05:15:50 UTC |
| 训练 | **5/5 steps 完成**, 总耗时 ~3.2h |
| Checkpoint | `global_step_5/` — 6 个 .pt 文件 (model+optim+extra × 2 ranks) |

**Metrics 退化严重：**

| Metric | Step 0 | Step 5 (final) |
|--------|--------|----------------|
| val success | 0.031 | **0.0** |
| val pass@1 | 0.031 | **0.0** |
| val reward/mean@32 | 0.3125 | **0.0** |
| val response_length | 9807 | **10934** |
| train response_length | — | **15790** |

训练完全 collapse——val reward 从 0.31 降到 0.0，response length 膨胀，最终 step 所有 reward 指标归零。W&B teardown 有 BrokenPipeError 但不影响 checkpoint 保存。

### 3. GPU 使用

| 服务器 | GPU | 显存占用 | 利用率 |
|--------|-----|----------|--------|
| bjb1-17606 | cuda:0 | 46.4/97.9 GB | 0% (step 间) |
| bjb1-17606 | cuda:1 | 47.3/97.9 GB | 0% (step 间) |
| westd-47453 | cuda:0-3 | 0-3 MiB / 97.9 GB | **空闲** |

westd-47453 四张卡完全空闲，可用于下一个实验。seed 2048 结果表明该 seed 下训练 collapsed，需判断是否重跑或调整超参。

---
