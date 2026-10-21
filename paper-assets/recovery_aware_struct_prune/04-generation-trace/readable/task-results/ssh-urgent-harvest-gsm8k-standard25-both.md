# ssh urgent harvest gsm8k standard25 both

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_harvest_gsm8k_standard25_both_20260521T121422_result.json`
- **Structured JSON:** [`174a214dfa9e3fa9ff2d.json`](../../sessions/17/174a214dfa9e3fa9ff2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在运行中，尚未完成。

---

## eval_gsm8k_grpo_standard_25 (westb-23072)

| 项目 | 状态 |
|------|------|
| 进程状态 | **ALIVE** (PID 75282) |
| 进度 | **1209/1319** (91.7%) |
| 最近快照 (1200/1319) | acc=**51.50%**, eos_rate=95.67%, avg_len=318 |
| 预估剩余 | ~30 min（周期性慢 spike ~100s/it） |
| Registry 更新 | 未需要 |
| Cron 删除 | 未需要 |

## eval_gsm8k_sft_standard_25 (westd-29022)

| 项目 | 状态 |
|------|------|
| 进程状态 | **ALIVE** (PID 335301) |
| 进度 | **946/1319** (71.7%) |
| 最近快照 (900/1319) | acc=**51.22%**, eos_rate=96.11%, avg_len=301 |
| 预估剩余 | ~1.5h |
| Registry 更新 | 未需要 |
| Cron 删除 | 未需要 |

两个都还在跑。westb 约 30 分钟内完成，westd 约 1.5 小时。需要我稍后再检查一次吗？

---
