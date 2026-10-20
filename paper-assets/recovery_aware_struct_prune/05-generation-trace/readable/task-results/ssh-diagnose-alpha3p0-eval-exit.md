# ssh diagnose alpha3p0 eval exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_alpha3p0_eval_exit_20260522T144347_result.json`
- **Structured JSON:** [`9b75b2342140cb91e6ea.json`](../../sessions/9b/9b75b2342140cb91e6ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## α=3.0 GRPO Eval 结果

| 指标 | 值 |
|------|-----|
| **accuracy** | **63.45%** (837/1319) |
| stderr | ±1.33% |
| eos_rate | 98.64% (1301 natural / 18 truncated) |
| avg_response_length | 219.7 tokens |
| mode | greedy (T=0) |
| checkpoint | `grpo_rasp_alpha3p0_20_v2/checkpoint-100` |

进程已退出，eval 完整跑完（1319/1319）。上次 88% 进度时 acc=63.04%，最终收敛到 **63.45%**，变化不大。

---
