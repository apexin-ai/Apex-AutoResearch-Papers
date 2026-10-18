# diagnose idle gpus batch 20260526

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_idle_gpus_batch_20260526_20260526T144549_result.json`
- **Structured JSON:** [`d86fb424d75a8c102e6c.json`](../../sessions/d8/d86fb424d75a8c102e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-27271 已经在跑 Task 1/10，pruning 256→128 tokens (k=0.5)。

## 汇总

### 诊断结果

| GPU | 状态 | 说明 |
|-----|------|------|
| westd-27271:cuda:1 | **确认空闲** → 已填充 | 之前的 eval 完成，GPU 释放 |
| cqa1-33015:cuda:1 | **误报** — 在跑 | PID 416018, 10111 MiB, 跑 l2norm k085 long v3 |
| cqa1-33015:cuda:2 | **确认空闲** → 已填充 | attn k05 long v2 进程消失，无日志 |
| westd-41074:cuda:1 | **误报** — 全部在跑 | 4卡全忙 (55-71% util, ~16GB each) |

### 提交的实验

| exp_id | server:gpu | 命令 | 验证 |
|--------|-----------|------|------|
| eval_openvla_random_k05_goal_seed42_v2 | westd-27271:cuda:1 | random_prune k=0.5 Goal | 59% util, 15964 MiB, Task 1/10 已开始 |
| eval_pi05_attention_k05_long_seed42_v3 | cqa1-33015:cuda:2 | attention k=0.5 Long | 模型加载中，log 正常输出 |

**注意**: Random k=0.5 Goal 之前已有一次完成的结果 (SR=52.2%)，本次为验证性重跑。

---
