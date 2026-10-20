# exp qwen math sft cka only

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_math_sft_cka_only_20260520T063552_result.json`
- **Structured JSON:** [`a101bced8e400ce734ea.json`](../../sessions/a1/a101bced8e400ce734ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 训练已启动。

**汇总：**

| 项目 | 结果 |
|------|------|
| **CKA-only post-prune eval (N=200)** | GSM8K Accuracy = **1.00%** (2/200), eos_rate=6.5%, avg_len=958 |
| **CKA-only SFT** | RUNNING on westb-23072 cuda:0, 1870 steps (7473 samples × 2 epochs / batch 8), ~1.1s/step, 预计约 35 分钟 |
| **修复** | `sft_recovery.py` 第 68 行断言增加 `<\|im_end\|>` 兼容 Qwen ChatML 模板 |
| **registry** | `sft_qwen_math_cka_only_20` → RUNNING |
| **log** | `~/runs/recovery_aware_struct_prune/sft_qwen_math_cka_only_20.log` |
| **output_dir** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20` |

另外注意：GPU 1 上有一个 standard SFT 进程（PID 997507, `pruned_standard_20_qwen_math`），来源不是本次操作。

---
