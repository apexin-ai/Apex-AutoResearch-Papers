# ops locate standard fair and fix humaneval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_locate_standard_fair_and_fix_humaneval_20260519T063646_result.json`
- **Structured JSON:** [`1f61da64814c0f4ff74d.json`](../../sessions/1f/1f61da64814c0f4ff74d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**崩溃原因**：路径错误。eval 用了 `grpo_standard_20_fair`，实际目录名是 `grpo_stage2_standard_20_fair`（两台服务器均无 `grpo_standard_20_fair`）。

**Checkpoint 位置**（均在 westd-29022）：
- Standard fair: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair/` (12.3GB)
- RASP fair: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair/` (12.3GB)

**已启动的 eval**（westd-29022）：
| Experiment | GPU | tmux session |
|---|---|---|
| `eval_humaneval_grpo_rasp_20_fair_2048` | cuda:3 | `eval_humaneval_rasp_fair` |
| `eval_humaneval_grpo_standard_20_fair_2048_v2` | cuda:2 | `eval_humaneval_standard_fair` |

**Registry 更新**：
- `eval_humaneval_grpo_standard_20_fair_2048` → DONE / failed（路径错误）
- 两个新 eval 已注册为 RUNNING

---
