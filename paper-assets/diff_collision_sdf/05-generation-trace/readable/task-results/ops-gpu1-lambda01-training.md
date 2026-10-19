# ops gpu1 lambda01 training

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1_lambda01_training_20260525T231052_result.json`
- **Structured JSON:** [`0f33c9291988931dd001.json`](../../sessions/0f/0f33c9291988931dd001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

**汇报：**

| 项目 | 值 |
|------|-----|
| PID | 271266（Python 进程） |
| GPU 1 显存 | 19055 MiB, 利用率 100% |
| 训练状态 | 正常，Step 4/30000，~2.65s/it |
| loss | ~0.16（action=0.15, sdf=0.12, ee=0.18） |
| lambda_sdf | 0.1 |
| 日志 | `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log` |

注意：原始命令中的 `--save_total_limit 3` 不是该脚本的合法参数，已去掉。

---
