# submit westd 41718 2gpu immediate

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-41718-2gpu-immediate_20260518T081014_result.json`
- **Structured JSON:** [`d1e69770dc052fcc57b8.json`](../../sessions/d1/d1e69770dc052fcc57b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验状态：

| 实验 | GPU | 状态 | 结果 |
|------|-----|------|------|
| c4_ood_kl30_s42_v2 | cuda:0 | **已完成** | C4 PPL = **16.0401** (vs s123 ~16.03，一致) |
| kl50_s42_uniform_eval | cuda:1 | **运行中** | 15.9GB 已加载 |

实验 1 已出结果：C4 OOD PPL 16.04，与 s123 的 16.03 高度一致，cross-seed OOD 泛化假设成立。实验 2 在 cuda:1 上正常跑着。

---
