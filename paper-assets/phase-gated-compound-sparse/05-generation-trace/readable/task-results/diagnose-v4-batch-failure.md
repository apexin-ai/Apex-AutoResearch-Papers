# diagnose v4 batch failure

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4_batch_failure_20260513T232112_result.json`
- **Structured JSON:** [`d362ccda25118092ef1b.json`](../../sessions/d3/d362ccda25118092ef1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败根因**：`run_profiling.py` 的 argparse 中没有定义 `--masking_method` 参数。

4 个 v4 实验全部因相同原因失败：
```
run_profiling.py: error: unrecognized arguments: --masking_method importance
```
（v4-random 的是 `--masking_method random`）

当前 `run_profiling.py` 支持的参数：
- `--model_path` (required)
- `--data_path` (required)
- `--output_dir`
- `--max_new_tokens`
- `--kde_bandwidth`
- `--min_phase_length`
- `--sparsity_levels` ← **这个有**

`--masking_method` ← **这个没有**

**修复方案**：

1. **如果 masking_method 逻辑已在代码中实现但只是忘了加 argparse 参数** → 在 `parse_args()` 中添加 `--masking_method` 参数，并在 `run_profiling()` 中使用它。
2. **如果 masking_method 逻辑还没实现** → 需要在代码中实现 importance/random 两种 masking 策略后再添加参数。

需要我检查代码中是否已有 masking_method 相关逻辑，还是直接加上这个参数？

---
