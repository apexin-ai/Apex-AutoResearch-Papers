# code alpha sft sweep westd gpu1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha-sft-sweep-westd-gpu1_20260515T135109_result.json`
- **Structured JSON:** [`b97574c161bc14b435ff.json`](../../sessions/b9/b97574c161bc14b435ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交 α=1.0 SFT 到 westd-11672 cuda:1。

- **exp_id**: `sft-alpha-1p0`
- **日志**: `~/runs/recovery_aware_struct_prune/sft-alpha-1p0.log`
- **预计耗时**: ~30 分钟

剩余待执行（按优先级）：
1. α=0.0 eval（SFT 已完成）
2. α=2.0 SFT → eval
3. α=0.5 SFT → eval
4. α=1.0 eval（等当前 SFT 完成后）

---
