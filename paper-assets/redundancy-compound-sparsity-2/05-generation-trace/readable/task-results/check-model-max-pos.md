# check model max pos

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_model_max_pos_20260512T142918_result.json`
- **Structured JSON:** [`785d04e7fe793722afa4.json`](../../sessions/78/785d04e7fe793722afa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **max_position_embeddings** = 131072 (128K)
- **rope_theta** = 1000000.0
- **rope_scaling** = None

模型原生支持 128K 上下文，rope_theta=1M，无额外 rope_scaling。64K 实验完全在原生支持范围内，无需做任何 position embedding 扩展。

---
