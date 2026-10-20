# collect v5 final results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_v5-final-results_20260514T014957_result.json`
- **Structured JSON:** [`d18d3e4fca81bdb97796.json`](../../sessions/d1/d18d3e4fca81bdb97796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验仍在运行中，尚未完成：

| 实验 | GPU | 进度 | 启动时间 | 预计完成 |
|------|-----|------|----------|----------|
| s020 | GPU0 | 35/50 (70%) | 09:26 | ~10:00 UTC |
| s030 | GPU1 | 35/50 (70%) | 09:26 | ~10:00 UTC |
| s015 | GPU2 | 28/50 (56%) | 09:32 | ~10:05 UTC |
| s025 | GPU3 | 28/50 (56%) | 09:32 | ~10:05 UTC |

NaN skip 修复生效中（日志可见 `Skipped 1 NaN attention layers: [27]`）。

旧进程（38120, 38996, 38760）已清理。

**冗余下载进程**：有 3 个 modelscope + 1 个 huggingface_hub 进程在下载 Qwen2.5-7B，PIDs: 43532, 46175, 46558, 47323。这些是冗余的，要现在 kill 掉吗？

预计 ~15 分钟后全部完成，届时我再收集结果。

---
