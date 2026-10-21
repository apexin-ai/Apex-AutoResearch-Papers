# ops check olmo2 rerun progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-olmo2-rerun-progress_20260521T143111_result.json`
- **Structured JSON:** [`53df4b8dc4242b65611d.json`](../../sessions/53/53df4b8dc4242b65611d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_olmo2_s42_rerun 进度

**进程状态**: PID 531623 存活，已运行 5m25s，CUDA_VISIBLE_DEVICES=3

**当前任务**: d000 s42 MMLU — 5999/14042 (42.7%)，速度 ~15.5 it/s

**已完成结果**: 无（`olmo2_d000_s42_mmlu/` 目录为空，尚未写出结果）

**GPU 3**: 96% 利用率，16.7GB / 95.6GB 显存

**进度估算**:
| 任务 | 状态 |
|------|------|
| d000 MMLU | 42.7% 进行中 |
| d000 ARC | 待开始 |
| d005/d025/d050/d100 × 2 benchmarks | 待开始 |

总计 10 个 eval 任务（5 dosage × 2 benchmark），当前第 1 个进行中。

**剩余时间估算**: 当前 MMLU 剩余 ~9 min，后续 4 个 MMLU ~60 min，5 个 ARC ~20 min，加载开销 ~5 min → **总计约 1.5 小时**。

---
