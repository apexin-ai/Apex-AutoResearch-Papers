# urgent westd27271 fill gpu1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd27271_fill_gpu1_20260525T040148_result.json`
- **Structured JSON:** [`08a57974115816314cb1.json`](../../sessions/08/08a57974115816314cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在跑：

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| GPU0 | 90% | 16016 MiB | Object baseline（你之前提交的） |
| GPU1 | 70% | 15980 MiB | Random k=0.9 Object seed42（刚提交） |

Random Object 已在推理中：模型从 `/root/autodl-tmp/openvla-libero-object` 加载，256→230 vision tokens (k=0.9)，10 tasks × 50 episodes = 500 total。tmux 会话 `random_object`，日志 `/tmp/eval_random_object_seed42.log`，输出 `eval_results/openvla_random_prune_k09_object_seed42_v2.json`。

---
