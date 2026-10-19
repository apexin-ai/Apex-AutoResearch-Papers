# ops verify bjb1 exp029 alive

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-bjb1-exp029-alive_20260518T102238_result.json`
- **Structured JSON:** [`0520caa49baf2a3b1ed8.json`](../../sessions/05/0520caa49baf2a3b1ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

- **PID 24047: alive** — `python train.py --config-name _alfworld_exp029_episode_level_seed2`，启动于 17:40，运行约 43 分钟
- **GPU 0: 45989 MiB / 97887 MiB** — 100% util, 437W
- **GPU 1: 45989 MiB / 97887 MiB** — 100% util, 440W
- **当前阶段**: Ray 集群运行中，两张 GPU 均被 `actor_rollout_compute_log_prob` worker 占用（PID 27465/27466），正在执行 rollout + log_prob 计算，属于 GRPO 训练的数据采集/概率计算阶段。

---
