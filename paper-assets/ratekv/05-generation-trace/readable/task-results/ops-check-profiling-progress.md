# ops check profiling progress

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_profiling_progress_20260515T104657_result.json`
- **Structured JSON:** [`cfaa036ff49432aeae86.json`](../../sessions/cf/cfaa036ff49432aeae86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 实验 1: Pythia-1.4B profiling — **已完成**
- 耗时 25.7min，产出文件已保存 (36KB)

### 实验 2: Qwen2.5-14B profiling — **进行中**
- 进度: **347/384** (90.4%)
- 当前: L43H2，elapsed 145.7min
- ETA: **~16min**
- GPU 1: 33477 MiB / 97887 MiB, 100% 利用率

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 97887 MiB | 0% (空闲) |
| 1 | 33477 / 97887 MiB | 100% (Qwen profiling) |

Qwen 实验预计约 16 分钟后完成。完成后再提取 concentration 指标。

---
