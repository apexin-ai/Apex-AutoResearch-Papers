# deploy w38 s44 attn085 random07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_w38-s44-attn085-random07_20260527T214524_result.json`
- **Structured JSON:** [`de5d4336c3e7bf4aa285.json`](../../sessions/de/de5d4336c3e7bf4aa285.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动：

| 实验 | tmux session | PID | GPU |
|------|-------------|-----|-----|
| Attn k=0.85 seed44 | `eval_pi05_attn_k085_long_seed44_strict_w38` | **672324** | cuda:0 |
| Random k=0.7 seed44 | `eval_pi05_random_k07_long_seed44_strict_w38` | **672401** | cuda:1 |

注意：GPU 2 上还有一个已在运行的 l2norm k=0.5 实验 (PID 557458)。三个实验互不冲突。

---
