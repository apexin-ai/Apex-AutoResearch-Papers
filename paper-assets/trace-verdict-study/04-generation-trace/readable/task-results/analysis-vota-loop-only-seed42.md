# analysis vota loop only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_loop_only_seed42_20260515T100559_result.json`
- **Structured JSON:** [`c74fb359dacce754f084.json`](../../sessions/c7/c74fb359dacce754f084.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。汇总如下：

```json
{
  "condition": "loop_only",
  "accuracy": 0.8563,
  "accuracy_ci": [0.8353, 0.8756],
  "majority_baseline": 0.7151,
  "lift_vs_majority": 0.1412,
  "lift_vs_majority_ci": [0.1109, 0.1714],
  "n": 1190,
  "pass_precision": 0.9239,
  "pass_recall": 0.8707,
  "pass_f1": 0.8966,
  "fail_precision": 0.7165,
  "fail_recall": 0.8201,
  "fail_f1": 0.7648,

  "lift_vs_notrace": 0.1050,
  "lift_vs_notrace_ci_lower": 0.0824,
  "lift_vs_notrace_ci_upper": 0.1286,
  "notrace_baseline_acc": 0.7513,

  "lift_vs_vota": -0.1378,
  "lift_vs_vota_ci_lower": -0.1571,
  "lift_vs_vota_ci_upper": -0.1185,
  "vota_baseline_acc": 0.9941,

  "lift_vs_full_trace": 0.0387,
  "lift_vs_full_trace_ci_lower": 0.0185,
  "lift_vs_full_trace_ci_upper": 0.0597,
  "full_trace_baseline_acc": 0.8176,

  "all_comparisons_significant": true,
  "bootstrap_resamples": 10000,

  "train_loss_final": 0.0718,
  "train_epochs": 3,
  "train_runtime_seconds": 7425.65,

  "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final",
  "log_path": "~/runs/trace-verdict-study/vota_loop_only_seed42.log",
  "checkpoint_complete": true
}
```

**关键发现：**

| 对比 | Δ accuracy | 95% CI | 显著? |
|------|-----------|--------|-------|
| loop_only vs no_trace | **+10.5pp** | [+8.2, +12.9] | Yes |
| loop_only vs full_trace | **+3.9pp** | [+1.8, +6.0] | Yes |
| loop_only vs vota | **-13.8pp** | [-15.7, -11.8] | Yes |

- **loop_only (85.6%)** 显著高于 no_trace (75.1%) 和 full_trace (81.8%)，说明循环结构信息本身有较强预测力。
- 但远低于完整 vota (99.4%)，说明 loop trace 单独只能覆盖部分信号，assertion errors 和 exception 信息贡献了剩余 ~14pp 的提升。
- fail 类的 recall (82.0%) 高于 precision (71.6%)，模型倾向于多预测 fail（保守倾向）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "condition": "loop_only",
    "accuracy": 0.8563,
    "accuracy_ci": [
      0.8353,
      0.8756
    ],
    "majority_baseline": 0.7151,
    "lift_vs_majority": 0.1412,
    "lift_vs_majority_ci": [
      0.1109,
      0.1714
    ],
    "n": 1190,
    "pass_precision": 0.9239,
    "pass_recall": 0.8707,
    "pass_f1": 0.8966,
    "fail_precision": 0.7165,
    "fail_recall": 0.8201,
    "fail_f1": 0.7648,
    "lift_vs_notrace": 0.105,
    "lift_vs_notrace_ci_lower": 0.0824,
    "lift_vs_notrace_ci_upper": 0.1286,
    "notrace_baseline_acc": 0.7513,
    "lift_vs_vota": -0.1378,
    "lift_vs_vota_ci_lower": -0.1571,
    "lift_vs_vota_ci_upper": -0.1185,
    "vota_baseline_acc": 0.9941,
    "lift_vs_full_trace": 0.0387,
    "lift_vs_full_trace_ci_lower": 0.0185,
    "lift_vs_full_trace_ci_upper": 0.0597,
    "full_trace_baseline_acc": 0.8176,
    "all_comparisons_significant": true,
    "bootstrap_resamples": 10000,
    "train_loss_final": 0.0718,
    "train_epochs": 3,
    "train_runtime_seconds": 7425.65,
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final",
    "log_path": "~/runs/trace-verdict-study/vota_loop_only_seed42.log",
    "checkpoint_complete": true
  }
}
```

</details>

---
