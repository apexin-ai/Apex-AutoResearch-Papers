# code joint fit dead code fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_joint_fit_dead_code_fix_20260514T221237_result.json`
- **Structured JSON:** [`9133a23b584b8b4d22e3.json`](../../sessions/91/9133a23b584b8b4d22e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。方案 A，改动如下：

**joint_fit.py** (3 处):
- `concatenate_benchmarks()`: 实现了 `exclude_rules` 过滤——遍历规则，当数据集中存在匹配 `model` pattern 的模型时，将对应 `benchmark` 加入排除集合，循环中跳过这些 benchmark
- `run_joint_fit()`: 签名新增 `exclude_rules=None` 参数，透传给 `concatenate_benchmarks()`

**run_exp006.py** (2 处):
- 新增 `D018_EXCLUDE_RULES = [{"model": "3B", "benchmark": "gsm8k", "reason": "D018 LoRA damage"}]`
- `run_pipeline()` → `run_joint_fit()` 调用中传入 `exclude_rules=D018_EXCLUDE_RULES`

`python joint_fit.py --help` 验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "3B",
    "benchmark": "gsm8k",
    "reason": "D018 LoRA damage"
  }
}
```

</details>

---
