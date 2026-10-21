# ops harvest westb launch next

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_westb_launch_next_20260518T181225_result.json`
- **Structured JSON:** [`8b55a0aa70cb4df805cf.json`](../../sessions/8b/8b55a0aa70cb4df805cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都还在跑，GPU 全占满：

| Eval | GPU | 进度 | 当前 acc | 预估剩余 |
|------|-----|-------|----------|----------|
| CKA-only (grpo_cka_only_20_1p5b) | cuda:1 | 836/1319 (63%) | 0.3538 | ~55 min |
| Standard (grpo_standard_20_1p5b) | cuda:0 | 528/1319 (40%) | 0.2320 | ~2h |

两个 GPU 都满载（98%/95%），无法启动新任务。CKA-only 预计约 1 小时内完成，Standard 约 2 小时。需要等它们跑完后再收割结果、启动下一批。

---
