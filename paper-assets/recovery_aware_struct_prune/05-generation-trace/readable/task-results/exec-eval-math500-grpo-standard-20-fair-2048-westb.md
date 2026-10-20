# exec eval math500 grpo standard 20 fair 2048 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_eval_math500_grpo_standard_20_fair_2048_westb_20260521T223452_result.json`
- **Structured JSON:** [`decda37fb9e61baa008c.json`](../../sessions/de/decda37fb9e61baa008c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**启动确认**：

| 项目 | 值 |
|------|------|
| **exp_id** | `eval_math500_grpo_standard_20_fair_2048` |
| **服务器** | westd-29022（备选，因 westb 磁盘不足） |
| **GPU** | cuda:0（与 gsm8k eval 共享，98GB 卡充裕） |
| **Python PID** | 427456 |
| **模型路径** | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair` |
| **输出** | `/root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048.json` |
| **日志** | `/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048.log` |
| **状态** | RUNNING，500 题 MATH-500 已开始推理 |

**westb 未使用原因**：数据盘仅剩 14GB，装不下 12GB checkpoint。westd-29022 cuda:0 有 85GB 空余 VRAM，checkpoint 已在本地。

**备注**：westd 上已有旧结果 `math500_grpo_standard_20_fair_v2.json`（May 19, 145K），本次为独立重跑，输出路径不同。

---
