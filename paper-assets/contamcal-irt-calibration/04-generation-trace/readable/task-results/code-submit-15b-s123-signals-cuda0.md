# code submit 15B s123 signals cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_submit-15B-s123-signals-cuda0_20260516T020626_result.json`
- **Structured JSON:** [`6eba09cd66b356e1949b.json`](../../sessions/6e/6eba09cd66b356e1949b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 张 GPU 均被占用：**

| GPU | 显存占用 | PID | 利用率 |
|-----|----------|-----|--------|
| 0 | 13583 MiB | 642763 (3B eval d100_a32_s123) | 66% |
| 1 | 8985 MiB | 676497 | 91% |
| 2 | 9509 MiB | 676140 | 52% |
| 3 | 8985 MiB | 655989 | 68% |
| 4 | 6659 MiB | 668217 | 62% |
| 5 | 7531 MiB | 663067 | 61% |

无空闲 GPU 可用。根据 C001/C002 约束，不能向有活跃进程的 GPU 提交任务。

**当前状况**：
- cuda:0 上的 3B eval 已跑 4.5h，评估 4 个 benchmark（mmlu/gsm8k/arc_challenge/humaneval），可能还需要一段时间才能完成
- 所有 checkpoints 和 base model 已确认存在

**建议**：等 cuda:0 的 eval 完成后再提交 1.5B s123 signals 批处理。需要我先准备好脚本（检查 `compute_signals.py --help` 并写好脚本内容），等 GPU 释放后立即提交？

---
