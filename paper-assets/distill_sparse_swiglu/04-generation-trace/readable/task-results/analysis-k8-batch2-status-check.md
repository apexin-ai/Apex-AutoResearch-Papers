# analysis k8 batch2 status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k8_batch2_status_check_20260523T090316_result.json`
- **Structured JSON:** [`97ae8a6ecfb7a2023fb1.json`](../../sessions/97/97ae8a6ecfb7a2023fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE。

## 汇报

| 实验 | 状态 | avg_kl | avg_sparsity | final_kl (Step 1000) | 耗时 |
|------|------|--------|-------------|---------------------|------|
| perlayer_kl_k8_s123 | DONE (success) | 0.0997 | 0.286 | 0.0825 | ~36min |
| perlayer_kl_k8_s456 | DONE (success) | 0.0982 | 0.285 | 0.1079 | ~36min |

**GPU 状态**：cuda:0 和 cuda:1 均已空闲（0% 利用率，0 MiB 显存占用），可用于下一批任务。

---
