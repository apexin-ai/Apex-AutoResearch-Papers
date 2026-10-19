# code eval pipeline

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_20260518T073439_result.json`
- **Structured JSON:** [`aee9209d068828225d76.json`](../../sessions/ae/aee9209d068828225d76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 正常输出，无语法错误。

文件已创建在 `artifacts/eval/eval_pipeline.py`。框架包含：

- `BenchmarkBase` 抽象基类（`load_data` / `run_inference` / `compute_metrics` / `evaluate` / `dry_run`）
- 4 个 benchmark 骨架类，每个方法标注 TODO 及预期数据格式
- `EvalPipeline` 统一管线（注册、批量运行、报告生成）
- `load_model_and_tokenizer` 工具函数
- 完整 CLI（`--model-path`、`--benchmarks`、`--output-dir`、`--device`、`--dry-run` 及各 benchmark 专属参数）

---
