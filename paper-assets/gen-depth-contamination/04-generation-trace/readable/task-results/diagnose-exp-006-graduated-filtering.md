# diagnose exp 006 graduated filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_graduated_filtering_20260514T210628_result.json`
- **Structured JSON:** [`0a6e07d28f4e8fceca77.json`](../../sessions/0a/0a6e07d28f4e8fceca77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

## 诊断结果

**中断点**: `[33/50] graduated_a0.7_s456` — 训练进度 5%（139/2814 steps）时被 timeout 杀掉。该目录只有 `filter_config.json`，无 adapter 和 eval 结果。

**完成情况**: 32/50 runs 已完成（+ base_model eval），每个都有完整的 `final_adapter/` 和 `eval_results.json`。

**缺失的 18 个 runs**:

| 策略 | 缺失的 seeds |
|------|-------------|
| graduated_a0.7 | s456 (partial), s789, s1024 |
| graduated_a0.9 | s42, s123, s456, s789, s1024 |
| surprisal | s42, s123, s456, s789, s1024 |
| dsir | s42, s123, s456, s789, s1024 |

**恢复方案**: 脚本有内置 skip 逻辑（检查 `eval_results.json` 是否存在），直接重新运行同一脚本即可，32 个已完成的 runs 会自动跳过。graduated_a0.7_s456 无 eval_results.json，会从头重跑。

```json
{
  "root_cause": "timeout_hours 不足：50 runs × ~45min ≈ 37.5h，但 timeout 限制不够覆盖全部",
  "error_type": "resource",
  "completed_runs": 32,
  "total_runs": 50,
  "missing_runs": [
    "graduated_a0.7_s456", "graduated_a0.7_s789", "graduated_a0.7_s1024",
    "graduated_a0.9_s42", "graduated_a0.9_s123", "graduated_a0.9_s456",
    "graduated_a0.9_s789", "graduated_a0.9_s1024",
    "surprisal_s42", "surprisal_s123", "surprisal_s456",
    "surprisal_s789", "surprisal_s1024",
    "dsir_s42", "dsir_s123", "dsir_s456", "dsir_s789", "dsir_s1024"
  ],
  "estimated_resume_hours": 13.5,
  "partial_results_valid": true,
  "fix_steps": [
    "直接重新运行 bash scripts/run_exp006.sh（内置 skip 逻辑会跳过已完成的 32 runs）",
    "设置 timeout ≥ 15h 以覆盖剩余 18 runs（18 × 45min ≈ 13.5h + buffer）"
  ],
  "can_auto_fix": true
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "timeout_hours 不足：50 runs × ~45min ≈ 37.5h，但 timeout 限制不够覆盖全部",
    "error_type": "resource",
    "completed_runs": 32,
    "total_runs": 50,
    "missing_runs": [
      "graduated_a0.7_s456",
      "graduated_a0.7_s789",
      "graduated_a0.7_s1024",
      "graduated_a0.9_s42",
      "graduated_a0.9_s123",
      "graduated_a0.9_s456",
      "graduated_a0.9_s789",
      "graduated_a0.9_s1024",
      "surprisal_s42",
      "surprisal_s123",
      "surprisal_s456",
      "surprisal_s789",
      "surprisal_s1024",
      "dsir_s42",
      "dsir_s123",
      "dsir_s456",
      "dsir_s789",
      "dsir_s1024"
    ],
    "estimated_resume_hours": 13.5,
    "partial_results_valid": true,
    "fix_steps": [
      "直接重新运行 bash scripts/run_exp006.sh（内置 skip 逻辑会跳过已完成的 32 runs）",
      "设置 timeout ≥ 15h 以覆盖剩余 18 runs（18 × 45min ≈ 13.5h + buffer）"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
