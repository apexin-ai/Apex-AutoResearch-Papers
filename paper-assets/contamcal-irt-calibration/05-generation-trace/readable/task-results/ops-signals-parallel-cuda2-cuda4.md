# ops signals parallel cuda2 cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-parallel-cuda2-cuda4_20260515T194205_result.json`
- **Structured JSON:** [`4b954b8b1ba06d16eccd.json`](../../sessions/4b/4b954b8b1ba06d16eccd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已经被别人启动了。当前 3B signals 的完整调度状况：

| GPU | PID | 命令 | 启动时间 | 当前处理 |
|-----|-----|------|----------|----------|
| cuda:3 | 617201 | `run_batch.py --model-size 3B --gpu 0` (全部 dosage) | 02:57 | d000/mmlu |
| cuda:4 | 622557 | `run_batch.py --model-size 3B --gpu 0 --only d100` | 03:41 | d100/mmlu |
| cuda:2 | 622855 | `run_batch.py --model-size 3B --gpu 0 --only d005 d025` | 03:41 | d005/mmlu |

**3B signals 完成状态（12 个 combo）：**

| Dosage | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| d000 | **运行中** (cuda:3) | ✓ | ✓ |
| d005 | **运行中** (cuda:2) | 待做 | ✓ |
| d025 | 待做 (cuda:2 排队) | ✓ | ✓ |
| d100 | **运行中** (cuda:4) | 待做 | 待做 |

**潜在冲突**：cuda:3 的 batch 没有 `--only` 限定，处理完 d000 后会继续跑 d005/d025/d100。如果 cuda:2/cuda:4 还没完成对应 combo（没生成 `signals_merged_*.json`），cuda:3 会尝试对同一 output-dir 并行写入，造成数据竞争。

**建议**：不再重复提交。可以监控当前三个 batch 的进度，必要时在 cuda:3 的 d000 完成后 kill 它（因为 d005/d025/d100 已分别由 cuda:2 和 cuda:4 覆盖）。需要我 kill cuda:3 的 batch 吗？

---
