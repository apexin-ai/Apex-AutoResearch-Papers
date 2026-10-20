# code d018 exclusion signal homogeneity

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d018_exclusion_signal_homogeneity_20260514T204013_result.json`
- **Structured JSON:** [`332ad3d9ae48bbfa3668.json`](../../sessions/33/332ad3d9ae48bbfa3668.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

**问题 1 — D018 排除（死代码修复）**：
- `should_exclude_dose_response()` 原来定义了但从未被调用
- 现在在 benchmark 循环中（line 284-296）正式调用，对每个 benchmark 检查 D018 规则，匹配的模型从 responses/dosages/models_bench 中过滤掉
- 新增 `--exclude-models` 参数（line 555），支持逗号分隔的模式全局排除

**问题 2 — 信号同源性检查**：
- 新增 `check_scale_signals()` 函数（line 109），预检每个 scale 的信号文件覆盖
- 在 `run_pipeline()` 数据加载后、dry-run 前（line 178-202），当 `pool_scales + signals_dir` 同时指定时自动检查，无信号的 scale 被 ERROR 排除
- `load_exp002_signals()` 新增 `pool_mode` 参数（line 81），pool 模式下缺信号抛 RuntimeError 而非静默 fallback
- 新增 `--require-signals` 参数（line 559），强制所有 scale 有信号否则 abort

**向后兼容**：非 pool 模式、不带 `--signals-dir` 时行为不变。

---
