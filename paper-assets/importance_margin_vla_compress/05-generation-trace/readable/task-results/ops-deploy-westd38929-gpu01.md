# ops deploy westd38929 gpu01

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-westd38929-gpu01_20260524T071034_result.json`
- **Structured JSON:** [`1b669cbe627da81d275a.json`](../../sessions/1b/1b669cbe627da81d275a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部在跑，部署完成。

| GPU | 实验 | 显存 | 状态 |
|-----|------|------|------|
| 0 | eval_xvla_l2norm_k03_long_seed42 | 5080 MiB | Task 0 运行中 |
| 1 | eval_xvla_random_k03_long_seed42 | 4858 MiB | Task 0 运行中 |
| 2 | eval_xvla_l2norm_k05_long_seed42_v4 | 4830 MiB | 已有进程 |
| 3 | eval_xvla_l2norm_k03_goal_seed42 | 4856 MiB | 已有进程 |

两个新实验均已进入 Task 0 评估阶段，registry 已更新为 RUNNING。L2norm k=0.3 Long 填补表格空白，Random k=0.3 Long 提供配对对比数据。

---
