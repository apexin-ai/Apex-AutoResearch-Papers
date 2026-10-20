# ops westd cuda1 check and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cuda1_check_and_launch_20260518T214600_result.json`
- **Structured JSON:** [`8abc5fe83e1a60d66a37.json`](../../sessions/8a/8abc5fe83e1a60d66a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_math500_grpo_standard_20_fair_v2 仍在运行中。**

状态：
- **进度**: 234/500 (47%)，已跑 ~3h16m
- **中间 accuracy**: 28.50% (200 samples 时)
- **GPU 1**: 98% 利用率, 19251MiB 显存, PID 22049
- **预计剩余**: ~3.5h（按当前 ~50s/it）

cuda:1 占用中，无法启动下一个 eval。其余 GPU 状态：
- cuda:0: 空闲 (0MiB)
- cuda:2: 占用 (17010MiB, 98%)
- cuda:3: 占用 (17541MiB, 96%)

需要等 v2 eval 完成后再启动 eval_math500_sft_standard_20_2048。预计完成时间约 UTC 09:00-09:30。

---
