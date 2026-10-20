# analysis codellama13b exception only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_exception_only_seed123_20260516T215512_result.json`
- **Structured JSON:** [`b091a24861b76c17bd10.json`](../../sessions/b0/b091a24861b76c17bd10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**codellama13b_exception_only_seed123: accuracy = 100.0% (0 errors / 1190)**

完整 eval_results.json:
```json
{
  "condition": "exception_only",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123/final",
  "metrics": {
    "accuracy": 1.0,
    "majority_baseline": 0.7151,
    "lift": 0.2849,
    "n": 1190,
    "pass_precision": 1.0,
    "pass_recall": 1.0,
    "pass_f1": 1.0,
    "fail_precision": 1.0,
    "fail_recall": 1.0,
    "fail_f1": 1.0
  }
}
```

训练和评估正常完成（EXIT_CODE=0），推理全程 running accuracy 保持 1.0000。

**多种子对比（exception_only, CodeLlama-13B）：**
| Seed | Accuracy | Errors |
|------|----------|--------|
| 42 | 99.83% | 2/1190 |
| 123 | **100.0%** | 0/1190 |

seed123 比 seed42 还好，达到了完美分类。exception_only 条件在 CodeLlama-13B 上表现极其稳健。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "condition": "exception_only",
    "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed123/final",
    "metrics": {
      "accuracy": 1.0,
      "majority_baseline": 0.7151,
      "lift": 0.2849,
      "n": 1190,
      "pass_precision": 1.0,
      "pass_recall": 1.0,
      "pass_f1": 1.0,
      "fail_precision": 1.0,
      "fail_recall": 1.0,
      "fail_f1": 1.0
    }
  }
}
```

</details>

---
