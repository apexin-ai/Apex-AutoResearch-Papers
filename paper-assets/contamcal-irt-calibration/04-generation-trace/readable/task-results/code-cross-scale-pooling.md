# code cross scale pooling

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_scale_pooling_20260514T195101_result.json`
- **Structured JSON:** [`3c402ca458e50201cbea.json`](../../sessions/3c/3c402ca458e50201cbea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 修改的文件

1. **`run_irt_calibration.py`** — 新增 `load_pooled_eval_results()` 函数（line 201），对每个 scale 调用 `load_eval_results`，合并 models 列表和 response matrix

2. **`run_exp006.py`** — 
   - 新增 `--pool-scales` 参数（nargs='+'）
   - `run_pipeline()` 中当 `--pool-scales` 存在时调用 `load_pooled_eval_results`
   - D024 delta exposure 改为 per-scale baseline 减除
   - dry-run 输出显示 per-scale 模型数
   - joint_fit 调用传递 `pool_scales`

3. **`joint_fit.py`** — `run_joint_fit()` 新增 `pool_scales` 参数，当传入时用 `load_pooled_eval_results` 替代 `load_eval_results`

### Dry-run 结果

```
--pool-scales 0.5B 1.5B 3B --benchmark gsm8k --aligned-only
```
- 0.5B: 4 models (d000, d005, d025, d100)
- 1.5B: 3 models (d000, d005, d100)
- 3B: 3 models (d000, d005, d100)
- **Total: 10 models** × 1319 items

向后兼容：不传 `--pool-scales` 时行为与之前完全一致。

---
