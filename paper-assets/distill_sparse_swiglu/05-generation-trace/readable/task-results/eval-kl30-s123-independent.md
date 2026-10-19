# eval kl30 s123 independent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl30_s123_independent_20260517T112444_result.json`
- **Structured JSON:** [`15ee3429cb7e877e724a.json`](../../sessions/15/15ee3429cb7e877e724a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s456 训练正在启动，参数确认：lambda_max=5000, target=0.3, seed=456。

---

## 汇报

**30% s123 eval 完整结果：**
| Metric | Value |
|---|---|
| WikiText-2 PPL | **8.9748** |
| ARC-c (25-shot acc_norm) | **0.4531** |
| WinoGrande (5-shot acc) | **0.6930** |
| MMLU (5-shot acc) | **0.3807** |
| GSM8K (8-shot exact_match) | **0.0758** |

**s456 训练已提交：**
- Job ID: `kl30_s456_train`
- PID: 36749
- GPU: cuda:1
- 参数：seed=456, lambda_max=5000, sparsity_target=0.3, 1000 steps
- 日志：`~/runs/distill_sparse_swiglu/kl30_s456_train.log`

**已完成操作：**
1. Kill 了 chain 脚本 (PIDs 31022, 31023)
2. 等待 s123 eval 完成并收集全部 downstream 结果
3. 独立提交 s456 训练到 cuda:1

---
