# code fix tau vector selection

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_tau_vector_selection_20260514T134416_result.json`
- **Structured JSON:** [`6c583f8b3017b89fa8b5.json`](../../sessions/6c/6c583f8b3017b89fa8b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## Diff 摘要

### exp006/run_irt_calibration.py
- `load_exposure_scores(exposure_file, benchmarks_data, model_id=None)` — 新增 `model_id` 参数；嵌套格式时若无 model_id 则 raise `ValueError`（不再默默取 `next(iter(...))`）
- CLI 新增 `--tau-model-id`、`--tau-source {exposure,oracle,aggregated}`
- 调用处传递 `model_id=args.tau_model_id`

### exp006/run_irt_stan.py
- 同样的 `load_exposure_scores` 改动
- `run_real_data` 签名增加 `model_id` 参数
- CLI 新增相同的两个参数，main() 调用处传递

### exp003/rrf_aggregation.py
- `generate_exposure_json` 返回 `(exposure, aggregated)` 元组
- 新增跨模型聚合逻辑：对每个 benchmark 的所有 model exposure 逐 item 求 mean
- main() 额外输出 `exposure_aggregated.json`（扁平格式 `{bench: [floats]}`）

## 验证结果

| 测试场景 | 结果 |
|----------|------|
| `--tau-model-id Qwen2.5-0.5B_d100_s42` 从嵌套格式提取 | PASS (mean=0.90) |
| 扁平格式直接读取（向后兼容） | PASS (mean=0.50) |
| 嵌套格式不指定 model_id → ValueError | PASS |
| 无效 model_id → ValueError 列出可用 ID | PASS |
| 无 exposure file → 全 1 回退 | PASS |
| 聚合 τ 输出格式 | PASS (3 benchmarks) |
| 聚合 τ 作为 exp-006 扁平输入 | PASS（跨管线兼容） |

注意：d100 的 gsm8k 和 arc_challenge signal 文件缺失（stderr 有 warning），所以聚合只基于 d000 和 d005 两个模型的数据。这是数据问题，不影响代码正确性。

---
