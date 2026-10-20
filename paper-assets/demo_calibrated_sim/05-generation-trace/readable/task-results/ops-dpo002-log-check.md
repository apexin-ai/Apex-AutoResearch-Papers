# ops dpo002 log check

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_dpo002-log-check_20260512T185746_result.json`
- **Structured JSON:** [`6c85fa2f9194ccf1cd77.json`](../../sessions/6c/6c85fa2f9194ccf1cd77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## dpo-002 结果报告

**训练结果：成功完成** — 3 epochs，无 error/crash。

**关键 metrics：**
| 指标 | 值 |
|------|-----|
| final_loss | 0.6614 |
| train_runtime | 1:26:02 (5162.8s) |
| epochs | 3.0 |
| samples/sec | 0.908 |
| 最后一步 rewards/accuracy | 0.667 |
| 最后一步 rewards/margin | 0.026 |

**Checkpoints：** checkpoint-782, checkpoint-1173, final_adapter

**值得注意：** loss 从未显著下降（始终在 0.63-0.68 波动），rewards/margin 极小（~0.03-0.13），rewards/accuracy 在 0.5-1.0 间震荡。训练本身跑完了，但 DPO 学习效果有限——符合预期（v2 数据仍存在 TRL tokenizer mismatch 问题）。

**Registry：** status=DONE, conclusion=success ✓
**Cron：** 已删除 ✓

---
