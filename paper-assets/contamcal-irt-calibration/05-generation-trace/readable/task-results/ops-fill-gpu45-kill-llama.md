# ops fill gpu45 kill llama

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_gpu45_kill_llama_20260517T062635_result.json`
- **Structured JSON:** [`4125d587a323d942e472.json`](../../sessions/41/4125d587a323d942e472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个 GPU 已经被占满了：

| GPU | PID | 任务 |
|-----|-----|------|
| 0 | 943337 | evaluate.py Qwen2.5-3B-Instruct (mmlu, arc, gsm8k) |
| 1 | 943406 | evaluate.py Qwen2.5-0.5B-Instruct (mmlu, arc, gsm8k) |
| 2 | 943479 | evaluate.py Qwen2.5-1.5B-Instruct (mmlu, arc, gsm8k) |
| 3 | 935048 | evaluate.py DeepSeek-R1-Distill-Qwen-1.5B (mmlu, arc, gsm8k) |
| 4 | 946440 | compute_signals s4 Qwen2.5-0.5B-Instruct/mmlu |
| 5 | 947036 | compute_signals s4 Qwen2.5-1.5B-Instruct/mmlu |

**cuda:4 和 cuda:5 已经在跑 signals 任务了**（s4_selfcritique for 0.5B/mmlu 和 1.5B/mmlu），正好是高优先级任务。zombie 进程 752362 已 kill -9。

当前状态：6 GPU 全部活跃，无需额外提交。cuda:4/5 上的 signals 任务符合 C007 优先级（0.5B/1.5B signals 优先）。

---
