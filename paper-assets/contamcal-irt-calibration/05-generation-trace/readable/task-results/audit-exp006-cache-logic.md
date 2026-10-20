# audit exp006 cache logic

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp006_cache_logic_20260514T150314_result.json`
- **Structured JSON:** [`60c3ba7c967ef77e960a.json`](../../sessions/60/60c3ba7c967ef77e960a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. 缓存逻辑类型：**无**

四个文件全部审查完毕，**没有任何缓存/跳过逻辑**：

| 文件 | 输出目录处理 | 缓存检查 |
|------|-------------|---------|
| `run_exp006.py` | `bench_dir.mkdir(parents=True, exist_ok=True)` 然后直接写文件 | 无 |
| `run_irt_calibration.py` | 同上 | 无 |
| `run_irt_stan.py` | 同上 | 无 |
| `joint_fit.py` | 同上 | 无 |

代码对每个 benchmark 的处理流程是：创建目录 → 跑 IRT → 跑 baselines → 跑 evaluation → 写 JSON 结果文件（覆盖写入）。没有 `if exists: skip` 逻辑。

注意：CLI 的 `--skip-stan` 是跳过 Stan-based baselines（B2/B3），不是跳过已完成的 benchmark。

### 2. 残留目录和文件

```
/root/autodl-tmp/exp006/results_05B/
/root/autodl-tmp/exp006/results_05B/mmlu/    ← 空目录（0 文件）
```

整个 `results_05B/` 下无任何文件。

### 3. 是否需要清理

**不需要。** 空目录无害——代码会 `mkdir(exist_ok=True)`（对已存在目录无操作），然后直接覆盖写入结果文件。重跑不受影响。

---
