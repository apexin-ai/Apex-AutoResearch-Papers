# monitor progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_20260515T050110_result.json`
- **Structured JSON:** [`6f44bcdb0c42b384af8c.json`](../../sessions/6f/6f44bcdb0c42b384af8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n=500 Profiling 实验进度汇总

### Qwen2.5-7B-Instruct (Screen: c2_qw_gpu2, c2_qw_gpu3)

| Condition | 完成数 | 状态 |
|-----------|--------|------|
| imp_s015 | 500/500 | 完成 |
| rand_s015 | 500/500 | 完成 |
| imp_s020 | 500/500 | 完成 |
| rand_s020 | 500/500 | 完成 |
| imp_s025 | 500/500 | 完成 |
| rand_s025 | 500/500 | 完成 |
| imp_s030 | **454/500** | 运行中 |
| rand_s030 | **452/500** | 运行中 |

### DeepSeek-R1-Distill-Qwen-7B (Screen: c2_n500_gpu0, c2_n500_gpu1)

| Condition | 完成数 | 状态 |
|-----------|--------|------|
| imp_s015 | 500/500 | 完成 |
| rand_s015 | 500/500 | 完成 |
| imp_s020 | 500/500 | 完成 |
| rand_s020 | 500/500 | 完成 |
| imp_s025 | 500/500 | 完成 |
| rand_s025 | 500/500 | 完成 |
| imp_s030 | **203/500** | 运行中 |
| rand_s030 | **248/500** | 运行中 |

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 77% | 26.9/97.9 GB |
| 1 | 96% | 30.6/97.9 GB |
| 2 | 68% | 34.1/97.9 GB |
| 3 | 77% | 34.7/97.9 GB |

4 个 GPU 全部活跃，4 个 s030 进程正在并行跑。Qwen 预计约 30-40 分钟完成（~1 min/problem），DeepSeek 预计约 2-3 小时完成。

---
