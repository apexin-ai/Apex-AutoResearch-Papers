# ops eval s2 l005 best cuda3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_s2_l005_best_cuda3_20260525T164117_result.json`
- **Structured JSON:** [`100620f331b465d749b4.json`](../../sessions/10/100620f331b465d749b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程在跑（PID 483300, RSS ~8GB, 运行 47 秒），CPU 端加载模型中。模型加载到 GPU 通常需要 1-2 分钟，之后 cuda:3 显存会上涨。

汇总：

- **Checkpoint**: best/ step 10000, best_loss=0.008740
- **PID**: 483300，cuda:3
- **日志**: 模型初始化正常 — `Creating PI0Pytorch model and injecting LoRA...`
- **状态**: 模型 CPU 加载中（RSS 8GB），等加载完成后会转到 cuda:3

---
