# ops verify cuda2 and p0 step60

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-cuda2-and-p0-step60_20260514T212901_result.json`
- **Structured JSON:** [`1946dfa591e7871cda22.json`](../../sessions/19/1946dfa591e7871cda22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中实际只有 step 5-40 的 metric 条目（8条，每5步），step 45+ 的指标尚未刷新到日志文件（Python stdout 缓冲）。当前进度 step 59/200。

## cuda:2 状态
- PID 100549 (nohup): **KILLED** — 已有标准 tmux 监控版本
- PID 100555 (100549 的子进程): 随父进程终止，已释放 9710 MiB
- PID 101831 (submit_training_job): **ALIVE** — 保留
- PID 101842 (101831 的子进程): **ALIVE** — 9060 MiB
- 结论: cuda:2 现在只有一个 eval 进程

## P0 (lr5e6_r1) Step 5-40 指标

| Step | f1_reward | ced_reward | format | reward_mean | frac_zero_std | KL |
|------|-----------|------------|--------|-------------|---------------|-----|
| 5 | 0.0185 | 0.0114 | 0.057 | 0.087 | 0.2 | **2.4e9** |
| 10 | 0.0 | 0.0 | 0.068 | 0.068 | 0.1 | 0.002 |
| 15 | 0.0109 | 0.0036 | 0.141 | 0.155 | 0.2 | 0.002 |
| 20 | *(truncated)* | | | | | |
| 25 | 0.0 | 0.0 | 0.176 | 0.176 | 0.2 | 0.004 |
| 30 | 0.0023 | 0.0015 | 0.128 | 0.131 | 0.1 | **7.0e13** |
| 35 | 0.0101 | 0.0154 | 0.168 | 0.193 | 0.1 | 0.157 |
| 40 | **0.0381** | **0.0786** | 0.201 | **0.318** | 0.3 | 0.006 |

当前 step: **59/200** (~30%)
Step 45-55 指标: **不可用**（metric dict 仍在 Python stdout 缓冲中，未刷新到日志文件。无 wandb。）

**趋势判断**: 上升。step 40 是目前最优（reward 0.318, f1 0.038, ced 0.079），步步新高。两次 KL spike（step 5 和 30）均快速恢复。f1 和 ced 在 step 35-40 出现加速增长信号。但 step 45-55 数据缺失，无法确认趋势是否延续。

---
