# diagnose gpu collision check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-collision-check_20260515T175132_result.json`
- **Structured JSON:** [`bbe3a989dd5ed82348aa.json`](../../sessions/bb/bbe3a989dd5ed82348aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，**无需 kill 操作**。结果如下：

## GPU 状态汇总

| GPU | 活跃进程 PID | 对应 exp_id | 状态 |
|-----|-------------|-------------|------|
| cuda:0 | 181094 (wrapper: 180877) | v4-taxei-fixed-inject10-s123 | 正常，106/1635 steps (~6%) |
| cuda:1 | 181223 (wrapper: 180956) | v4-random-fixed-inject10-s0 | 正常，105/1635 steps (~6%) |
| cuda:2 | 无 | — | 空闲（v4-training-dynamics-forward-v2 已完成，exit 0 @ 17:50:03Z） |
| cuda:3 | 无 | — | 空闲（v4-taxei-fixed-inject10-s0 已完成，exit 0 @ 17:51:16Z） |

## 冲突情况

第二批进程已自行失败退出，无需手动干预：
- `v4-random-inject10-seed0` (PID 181792) → **exit 1** @ 17:49:14Z（GPU 0 已被占用）
- `v4-taxei-inject10-seed123` (PID 181699) → **exit 1** @ 17:49:11Z（GPU 1 已被占用）

第一批（PID 更小）占住了 GPU，第二批尝试抢占失败后自动退出。当前 GPU 0/1 上只有第一批在正常训练，GPU 2/3 空闲可用。

---
