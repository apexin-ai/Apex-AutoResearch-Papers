# ops submit next westb eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_next_westb_eval_20260524T074238_result.json`
- **Structured JSON:** [`bf3c561a2b733b7ec2d0.json`](../../sessions/bf/bf3c561a2b733b7ec2d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- **实验**: `eval_math500_grpo_rasp_alpha0p5_20_fixed`
- **服务器**: westb-23072, cuda:1
- **PID**: 364213
- **Checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20`（westb 本地存在）
- **状态**: RUNNING

注：cuda:0 上正在跑 `eval_math500_sft_random_20_fixed_v3`（PID 335348），两个 GPU 互不干扰。`sft_rasp_alpha3p0_20` 也在 westb 上，但优先级排第二所以未提交。`grpo_rasp_alpha4p0_20` 和 `grpo_alpha4_20` 不在 westb。

---
