# deploy westd38929 gpu0 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu0-gpu3_20260523T205318_result.json`
- **Structured JSON:** [`559be969a1502e524340.json`](../../sessions/55/559be969a1502e524340.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行。

**部署结果汇总：**

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| eval_xvla_random_k05_goal_seed43 | GPU 0 | 844866 | `eval_xvla_random_k05_goal_seed43` | 运行中 (14/50 ep) |
| eval_xvla_random_k05_object_seed43 | GPU 3 | 844403 | `eval_xvla_random_k05_object_seed43` | 运行中 (15/50 ep) |

**注意**：Object seed43 实验之前已在 cqa1-33015 上完成（SR=71%），registry 状态为 DONE，无法回退到 RUNNING。当前在 westd-38929 上重跑，日志会写入 `logs/eval_xvla_random_k05_object_seed43.log`。

---
