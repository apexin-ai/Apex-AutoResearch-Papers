# ops cqa1 gsm8k intermediate dosage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gsm8k-intermediate-dosage_20260519T222459_result.json`
- **Structured JSON:** [`95ad62fdaf15927fc700.json`](../../sessions/95/95ad62fdaf15927fc700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d005 eval 正在推进中（165 batches, ~10s/batch, 预计 ~28min）。bitsandbytes 警告如预期不影响运行。

**执行摘要：**

| 项目 | 状态 |
|------|------|
| d005/d025/d050 adapters | 全部存在，alpha=32 ✓ |
| evaluate.py md5 | 001a9bc2... 匹配 ✓ |
| GPU 0 | 已占用，d005 eval 进行中（~10s/batch × 165 batches） |
| 实验注册 | `gsm8k_qwen7b_s42_intermediate_cqa1` QUEUED → RUNNING |
| 预计完成 | ~90min（3 dosages × ~30min） |
| d000+d100 SCP | cqa1→westd 不通，需从 westd 反向拉取 |

---
