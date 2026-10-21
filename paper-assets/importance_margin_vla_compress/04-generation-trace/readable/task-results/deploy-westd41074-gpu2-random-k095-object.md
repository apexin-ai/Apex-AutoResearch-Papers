# deploy westd41074 gpu2 random k095 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074-gpu2-random-k095-object_20260526T213050_result.json`
- **Structured JSON:** [`559dcdc9904b78dfedb3.json`](../../sessions/55/559dcdc9904b78dfedb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**部署完成，实验已在运行：**

| 项目 | 值 |
|------|-----|
| tmux session | `eval_random_k095_object` |
| PID | 934369（python 进程） |
| GPU | GPU 2，15961 MiB 显存占用 |
| 状态 | 正在执行 Task 1/10，256→243 vision tokens (k=0.95) |
| 总量 | 10 tasks × 50 episodes = 500 total |

注意：任务描述中给的模型路径 `/root/autodl-tmp/openvla-7b-finetuned-libero-object` 不存在，已修正为实际路径 `/root/autodl-tmp/openvla-libero-object`。同时 `python` 命令在该服务器上不可用，需要通过 conda activate base 激活环境。

---
