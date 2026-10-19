# ops westd 41718 fill gpus

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-41718-fill-gpus_20260518T065036_result.json`
- **Structured JSON:** [`0226b2b086882bb0e124.json`](../../sessions/02/0226b2b086882bb0e124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两卡已满：

| GPU | 实验 | 内容 |
|-----|------|------|
| cuda:0 | `downstream_ext_kl50_uniform_s42` | KL 50% uniform → HellaSwag, PIQA, BoolQ |
| cuda:1 | `downstream_ext_kl30_uniform_s123` | KL 30% uniform s123 → HellaSwag, PIQA, BoolQ (多 seed 补充) |

两个实验各占 ~41.7GB，tmux session 正常运行。填补的数据空白：50% sparsity 缺扩展下游任务结果，30% sparsity 缺 s123 seed 的扩展任务多 seed 方差数据。

---
