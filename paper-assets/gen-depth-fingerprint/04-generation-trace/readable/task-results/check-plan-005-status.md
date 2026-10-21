# check plan 005 status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan-005-status_20260515T033716_result.json`
- **Structured JSON:** [`2d9bec5b20d2761879aa.json`](../../sessions/2d/2d9bec5b20d2761879aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan-005 三个子实验状态报告

**全部正常运行中。** 已运行约 8 分 47 秒。

| 实验 | PID | GPU | 进度 | 输出行数 | 速度 |
|------|-----|-----|------|---------|------|
| plan-005-cont | 164658 | cuda:1 (6.2/32GB, 63%) | 62/995 (6.2%) | 306 lines | ~9.2s/it |
| plan-005-elab | 164737 | cuda:2 (6.2/32GB, 66%) | 59/995 (5.9%) | 293 lines | ~9.2s/it |
| plan-005-rewrite | 164881 | cuda:3 (6.2/32GB, 67%) | 59/995 (5.9%) | 293 lines | ~9.4s/it |

**输出文件位置：**
- `/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl`
- `/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl`
- `/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl`

**日志位置：** `~/runs/gen-depth-fingerprint/plan-005-{cont,elab,rewrite}.log`

按当前速度 (~9s/seed)，每个实验约需 995×9s ≈ 2.5 小时完成，预计还剩 ~2.3 小时。

---
