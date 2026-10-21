# ops tmux cleanup loop17

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tmux-cleanup-loop17_20260516T175451_result.json`
- **Structured JSON:** [`1c80ffc8976da460c8f0.json`](../../sessions/1c/1c80ffc8976da460c8f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**已杀掉的 stale sessions：**
- `exp_001_eval_llama32_3B_d025_s42`
- `exp_002_signals_15B_instruct_arc`

**当前存活 sessions (5个)：**
| Session | 创建时间 |
|---------|---------|
| `eval_llama_d000_v3` | May 16 23:34 |
| `eval_llama_d005` | May 17 01:54 |
| `exp_001_eval_3B_d100_v2_para_aligned` | May 15 08:05 |
| `exp_001_sft_llama32_3B_d100_s42` | May 16 23:31 |
| `sig_15b_mmlu_v2` | May 16 23:49 |

注意：用户提到的 `exp_001_sft_llama32_3B_d005_s42` (cuda:0) 和 `exp_002_signals_15B_instruct_mmlu` (cuda:4) 未以这些名称出现在 tmux ls 中，可能对应 `eval_llama_d005` 和 `sig_15b_mmlu_v2`。

等待步骤 3 后的新任务提交指令。

---
