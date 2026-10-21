# eval home few shot qwen8b

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-few-shot-qwen8b_20260517T174103_result.json`
- **Structured JSON:** [`16849e9b4474438ea2ed.json`](../../sessions/16/16849e9b4474438ea2ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已确认，无需重跑。之前的 `few_shot_baseline.py` 今天已经在 func-level test set 上跑过，结果如下：

```json
{
  "model": "Qwen3-8B",
  "method": "3-shot",
  "test_set": "func-level CLS (data/test.jsonl)",
  "test_set_size": 1890,
  "label_dist": {"pass": 978, "fail": 912, "pass_rate": "51.7%"},
  "accuracy": 68.78,
  "pass_f1": 64.46,
  "fail_f1": 72.17,
  "unparseable_rate": 0.0,
  "confusion_matrix": {"tn": 765, "fp": 147, "fn": 443, "tp": 535},
  "shot_selection": {"seed": 42, "n_pass": 2, "n_fail": 1},
  "elapsed_seconds": 171.0
}
```

与之前报告的 68.78% 完全一致。对比全景：

| Model | Method | Accuracy |
|-------|--------|----------|
| DeepSeek-6.7B | zero-shot | 56.56% |
| DeepSeek-6.7B | 3-shot | 59.95% |
| Qwen3-8B | zero-shot | 64.4% |
| **Qwen3-8B** | **3-shot** | **68.78%** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "Qwen3-8B",
    "method": "3-shot",
    "test_set": "func-level CLS (data/test.jsonl)",
    "test_set_size": 1890,
    "label_dist": {
      "pass": 978,
      "fail": 912,
      "pass_rate": "51.7%"
    },
    "accuracy": 68.78,
    "pass_f1": 64.46,
    "fail_f1": 72.17,
    "unparseable_rate": 0.0,
    "confusion_matrix": {
      "tn": 765,
      "fp": 147,
      "fn": 443,
      "tp": 535
    },
    "shot_selection": {
      "seed": 42,
      "n_pass": 2,
      "n_fail": 1
    },
    "elapsed_seconds": 171.0
  }
}
```

</details>

---
