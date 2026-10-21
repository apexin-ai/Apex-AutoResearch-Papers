# code mvp b oom fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-b-oom-fix_20260511T200459_result.json`
- **Structured JSON:** [`81aab194881ce4f77ff8.json`](../../sessions/81/81aab194881ce4f77ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

| 参数 | 原值 | 新值 |
|------|------|------|
| `--batch_size` (per_device_train_batch_size) | 8 | **2** |
| `--grad_accumulation` (gradient_accumulation_steps) | 4 | **16** |

Effective batch size 保持不变：2 × 16 = **32**。峰值显存从 ~9.4GB logits 降至 ~2.4GB，应在 32GB RTX 5090 可用范围内。

---
