# ssh rsft gen progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-gen-progress-check_20260515T041544_result.json`
- **Structured JSON:** [`711286e670eb72cd7acc.json`](../../sessions/71/711286e670eb72cd7acc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT 生成进度 (2026-05-15 ~14:50)

| Shard | 进度 | 完成率 | 速率 | 剩余 |
|-------|------|--------|------|------|
| 0 | 577/682 | 84.6% | 3.7 docs/min | ~28 min |
| 1 | 623/681 | 91.5% | 4.0 docs/min | ~14 min |
| 2 | 621/681 | 91.2% | 4.0 docs/min | ~15 min |
| 3 | 548/657 | 83.4% | 3.75 docs/min | ~29 min |

**总体 87.7%，预计 ~15:20 全部完成。**

质量指标正常：format_ok 99.6-100%，diversity 7.4-7.8/8。Shard 1 truncation_rate=10.1% 略超阈值（日志建议 max_new_tokens=3072，当前 1024）。

GPU 3 利用率 99%（其余 58-65%）。4 个进程均正常运行。

rsft_trainer.py 的 max_steps 默认 -1（使用 num_train_epochs 控制），无需修复。

---
