# deploy cqa1 cuda2 goal random k03

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_cuda2_goal_random_k03_20260522T190959_result.json`
- **Structured JSON:** [`0b45808c72b5bf615500.json`](../../sessions/0b/0b45808c72b5bf615500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 已上载模型（9507 MiB），评估已启动：

- 模型 4143.4M 参数
- Pruning: random, keep **76/256** tokens/image (k=0.3)
- Suite: libero_goal, 10 tasks

## 总结

**收割完成的实验：**
| 实验 | SR |
|------|-----|
| Goal Random k=0.7 | **80.6%** |
| Goal Random k=0.5 | **74.4%** |

**已部署：**
- `eval_pi05_random_k03_goal_seed42` — GPU 2, 9.5GB VRAM, 正在运行
- tmux session: `eval_pi05_random_k03_goal_seed42`
- 日志: `logs/eval_pi05_random_k03_goal_seed42.log`
- 预计 ~2h 完成（10 tasks × 50 episodes）

---
