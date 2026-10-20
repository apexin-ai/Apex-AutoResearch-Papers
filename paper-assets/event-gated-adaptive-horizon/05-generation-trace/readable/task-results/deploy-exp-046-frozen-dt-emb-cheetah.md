# deploy exp 046 frozen dt emb cheetah

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_046_frozen_dt_emb_cheetah_20260522T104255_result.json`
- **Structured JSON:** [`6bd80bbddcab883d7b9d.json`](../../sessions/6b/6bd80bbddcab883d7b9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**exp_046_frozen_dt_emb_cheetah 已在 bjb1-40020 cuda:0 上启动：**

| 项目 | 值 |
|------|-----|
| PID | 281513 |
| GPU | cuda:0 (RTX 4090, 1097 MiB 已占用) |
| 日志 | `logdir/exp_046_frozen_dt_emb_cheetah/train.log` |

**初始日志确认正常：**
- 环境创建成功 (dmc_cheetah_run, action space 6维)
- Prefill 完成 (2500 steps, 4 episodes)
- 模型初始化完成 (model_opt 16.9M params, actor_opt 1.1M, value_opt 1.2M)
- 已到达 step 5000，开始首次 evaluation
- 无报错

---
