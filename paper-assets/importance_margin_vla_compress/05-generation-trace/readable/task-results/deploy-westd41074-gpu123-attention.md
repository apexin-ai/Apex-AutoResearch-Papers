# deploy westd41074 gpu123 attention

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd41074-gpu123-attention_20260523T214642_result.json`
- **Structured JSON:** [`ba45cae3488a984eca62.json`](../../sessions/ba/ba45cae3488a984eca62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。4 张 GPU 均有进程运行，GPU 分配正确。

**部署汇总：**

| GPU | 实验 | PID | 显存 | tmux session |
|-----|------|-----|------|-------------|
| 0 | eval_pi05_attention_k05_goal_seed43 (已有) | 65843 | 10638 MiB | eval_pi05_attention_k05_goal_seed43 |
| 1 | eval_pi05_attention_k05_object_seed42 | 70037 | 10653 MiB | eval_pi05_attention_k05_object_seed42 |
| 2 | eval_pi05_attention_k05_spatial_seed42 | 70113 | 10720 MiB | eval_pi05_attention_k05_spatial_seed42 |
| 3 | eval_pi05_attention_k05_long_seed42 | 70252 | 10861 MiB | eval_pi05_attention_k05_long_seed42 |

3 个实验已部署、registry 已更新为 RUNNING，日志分别在 `/tmp/eval_pi05_attention_k05_{object,spatial,long}_seed42.log`。

---
