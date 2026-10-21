# diagnose plan 001 flat nli scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_001_flat_nli_scoring_20260515T151804_result.json`
- **Structured JSON:** [`fcdaec1aaec95a960ff9.json`](../../sessions/fc/fcdaec1aaec95a960ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diagnose_plan_001.md`。

**根因**：启动命令有两个错误——模块路径 `freige.training.rsft_score_filter` 不存在（正确路径是 `training.rsft_score_filter`），且缺少 `--input_dir` 和 `--output_path` 必选参数。进程启动即 `ModuleNotFoundError` 崩溃，无日志文件被创建。

**好消息**：评分任务已通过分 shard 方式完成（s0-s3 共 2719 条训练数据），无需重跑，合并 4 个 `rsft_train.jsonl` 即可使用。

---
