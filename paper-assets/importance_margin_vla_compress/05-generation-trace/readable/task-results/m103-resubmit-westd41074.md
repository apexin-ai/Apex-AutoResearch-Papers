# m103 resubmit westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_resubmit_westd41074_20260525T012507_result.json`
- **Structured JSON:** [`c1194343f73733fbe9a0.json`](../../sessions/c1/c1194343f73733fbe9a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部验证通过，模型路径正确：

| GPU | 实验 | 模型 | 状态 |
|-----|------|------|------|
| 0 | Attn k=0.9 Long | `openvla-7b-finetuned-libero-10` | 运行中，Task 1/10 |
| 1 | Attn k=0.85 Long | `openvla-7b-finetuned-libero-10` | 运行中，Task 1/10 |
| 2 | Random k=0.9 Long | `openvla-7b-finetuned-libero-10` | 运行中，Task 1/10 |
| 3 | L2norm k=0.9 Long | `openvla-7b-finetuned-libero-10` | 运行中，Task 1/10 |

所有实验的 `Loading OpenVLA from:` 均指向 `/root/autodl-tmp/models/openvla-7b-finetuned-libero-10`，unnorm_key=libero_10，确认无误。

---
