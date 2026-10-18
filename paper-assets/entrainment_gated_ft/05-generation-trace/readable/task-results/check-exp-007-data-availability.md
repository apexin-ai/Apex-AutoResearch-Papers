# check exp 007 data availability

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-007-data-availability_20260519T170212_result.json`
- **Structured JSON:** [`7e8871ffb8314215469b.json`](../../sessions/7e/7e8871ffb8314215469b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。结论：

**exp-007 不能直接启动**，缺少 lm-eval `--log_samples` 格式的 per-example JSONL 数据：

- **340M**: 全部 16 个模型都需要跑（零 logsamples 数据）。模型权重全部就位。
- **1.3B**: 已有 5 个模型的 logsamples（GDN h3/h6/h24, RetNet pure, Transformer），还缺 11 个模型。模型权重全部就位。
- 现有的 `analysis/lambada_per_example.csv` 只覆盖 4 个 340M 模型，且是自定义格式非 lm-eval 输出。
- 预估补跑时间约 2-3 小时（单 GPU 串行）。

报告已写入 `artifacts/exp007_data_check.md`。

---
