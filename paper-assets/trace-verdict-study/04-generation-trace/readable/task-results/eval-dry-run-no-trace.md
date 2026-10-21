# eval dry run no trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dry-run-no-trace_20260514T195021_result.json`
- **Structured JSON:** [`b83012ccef481199d90e.json`](../../sessions/b8/b83012ccef481199d90e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估脚本 dry-run 完成，无报错，输出格式正确。

## 评估结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | 75.1% (95% CI: [72.8%, 77.5%]) |
| **Majority baseline** | 71.5% (always predict 'pass') |
| **Lift over majority** | +3.6pp (95% CI: [+0.4pp, +7.1pp]) |

**Per-class metrics:**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 0.88 | 0.76 | 0.81 |
| fail | 0.55 | 0.73 | 0.63 |

Bootstrap: 1000 resamples

## eval_results.json 内容

```json
{
  "condition": "no_trace",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final",
  "metrics": {
    "accuracy": 0.7513,
    "majority_baseline": 0.7151,
    "lift": 0.0361,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134,
    "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272
  },
  "confidence_intervals": { ... }  // 所有指标的 95% bootstrap CI
}
```

## 汇报

- **脚本无 bug**，端到端顺利完成
- **输出格式正确**：accuracy + CI、majority baseline、lift + CI、per-class P/R/F1、bootstrap 1000 resamples 全部齐全
- **运行耗时**：约 2 分钟（含模型加载 + 1190 条推理 + bootstrap）
- **使用 GPU 1**（GPU 0 显存不够），占用 ~15.6GB 显存
- **唯一 warning**：`torch_dtype` deprecated（transformers 新版改用 `dtype`），不影响结果
- **no_trace 的 lift 仅 +3.6pp**，CI 下界接近 0，说明不看 trace 时模型略优于 majority baseline 但提升有限——符合预期，trace 条件的对比值得期待

---
