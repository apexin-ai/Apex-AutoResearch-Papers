# ops westd status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_status_check_20260518T201002_result.json`
- **Structured JSON:** [`3ee5218193a4db1804b9.json`](../../sessions/3e/3ee5218193a4db1804b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | 进度 | GPU利用率 | 显存 |
|-----|------|------|-----------|------|
| cuda:0 | E2 Extended GRPO | **253/300** (84%) | 100% | 90.6/97.9 GB |
| cuda:1 | MATH-500 Standard v2 | **129/500** (26%), Acc@100=0.34 | 99% | 17.5/97.9 GB |
| cuda:2 | MATH-500 SFT CKA-only restart | **235/500** (47%), Acc@200=0.345 | 99% | 17.0/97.9 GB |
| cuda:3 | MATH-500 RASP GRPO fair | **184/500** (37%), Acc@150=0.293 | 92% | 17.5/97.9 GB |

4 张卡全部满载运行。E2 GRPO 预计约 1 小时内完成；3 个 MATH-500 评估还需 2-4 小时不等。

---
