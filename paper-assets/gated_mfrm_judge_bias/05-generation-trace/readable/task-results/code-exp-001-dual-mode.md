# code exp 001 dual mode

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_dual_mode_20260521T233811_result.json`
- **Structured JSON:** [`5d7996de033747ce2ede.json`](../../sessions/5d/5d7996de033747ce2ede.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改摘要：

### judge_interface.py (229→299 行, +70)
- **L16-30**: 新增 `POINTWISE_JUDGE_PROMPT` (MT-Bench 标准模板)
- **L53-58**: `_parse_verdict` 解析失败返回 `None` (原 `0.5`)
- **L61-68**: 新增 `_parse_pointwise_score` (提取 `[[N]]`, 范围 1-10)
- **L79-86**: 基类新增 `evaluate_pointwise` 抽象方法
- **L97-99**: 新增 `_build_pointwise_prompt` 辅助方法
- **L101-103**: `_make_result` 增加 `score is not None` 守卫 (BA 翻转时)
- **L105-107**: 新增 `_make_pointwise_result` 辅助方法
- **每个子类**: 提取 `_call()` 方法 + 新增 `evaluate_pointwise()`

### collect.py (186→316 行, +130)
- **L43-56**: `load_completed` 新增 `mode` 参数，pointwise key = `(item_id, model, judge)`
- **L70-79**: 新增 `evaluate_pointwise_with_retry`
- **L82-99**: `collect_judgments` 签名改为 `(benchmark, judge_configs, target_models, output_dir, reference_model, mode, ...)`
- **L101-108**: auto mode 解析逻辑
- **L127-175**: `_collect_pointwise` — pointwise 收集主循环，输出含 `status` 字段
- **L178-234**: `_collect_pairwise` — pairwise 收集 (target vs reference_model)
- **L237-270**: `main()` 适配新 config 结构 (多 benchmark + `--benchmark` 参数)

### config.yaml (23→64 行, +41)
- 顶层 `benchmark` / `model_pairs` → `benchmarks` (mt_bench + arena_hard 双轨)
- judges 扩充至 9 个 (新增 gpt-5.5, claude-opus-4.7, deepseek-v4-pro RPM 调整)
- target_models 扩充至 22 个模型

### data_loader.py (74→91 行, +17)
- **L73-82**: 新增 `load_mt_bench_responses(model_name)` 和 `load_arena_hard_responses(model_name)` 便捷函数
- docstring 更新反映双轨设计

---
