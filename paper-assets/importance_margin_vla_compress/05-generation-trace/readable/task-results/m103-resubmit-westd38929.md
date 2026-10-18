# m103 resubmit westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_resubmit_westd38929_20260525T012452_result.json`
- **Structured JSON:** [`a204072055ae27cc9890.json`](../../sessions/a2/a204072055ae27cc9890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部验证通过，模型路径正确：

| GPU | 实验 | 加载模型 | 状态 |
|-----|------|---------|------|
| 0 | Random k=0.9 Goal | `openvla-7b-finetuned-libero-goal` | 已开始 Task 1/10, 256→230 tokens |
| 1 | Random k=0.9 Spatial | `openvla-7b-finetuned-libero-spatial` | 已开始 Task 1/10, 256→230 tokens |
| 2 | Attn k=0.85 Goal | `openvla-7b-finetuned-libero-goal` | 已开始 Task 1/10, 256→217 tokens |
| 3 | Attn k=0.85 Spatial | `openvla-7b-finetuned-libero-spatial` | 已开始 Task 1/10, 256→217 tokens |

所有实验均加载了正确的 suite-specific 微调模型，没有使用错误的 object/OFT 模型。

---
