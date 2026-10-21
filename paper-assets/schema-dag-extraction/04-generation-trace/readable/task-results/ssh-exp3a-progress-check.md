# ssh exp3a progress check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp3a-progress-check_20260515T032930_result.json`
- **Structured JSON:** [`346a4493cac0e65adbc2.json`](../../sessions/34/346a4493cac0e65adbc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp003a 进度报告

**状态**: 运行中 (PID 209542, 已运行 ~36 分钟)

**当前位置**: exp1 阶段，**55/94 batches 已完成** (58.5%)，正在处理第 56 个 batch

- 首个 batch 完成: 10:56:08
- 最后完成 batch: 11:29:43 (`count_1_random_54`)
- 平均每 batch: ~36.6 秒

**ETA 预估**:
| 阶段 | 剩余 batches | 预估耗时 |
|------|-------------|---------|
| exp1 | 39 | ~24 min |
| exp2 | 54 | ~33 min |
| **合计** | **93** | **~57 min** |

预计完成时间: **约 12:28** (UTC+8)

**GPU**: 94221 / 97887 MiB (96.3% VRAM), 利用率 14%。VRAM 高占用正常（Qwen3-32B-FP8）；GPU util 偏低是因为 vLLM 在 batch 间隙有 CPU 调度开销，处理中峰值会高很多。

**输出文件**: 尚未生成 `predictions_exp1_v2*.json`，exp1 完成后才会写出。

---
