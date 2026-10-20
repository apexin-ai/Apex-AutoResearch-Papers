# ssh westd collect d100 metrics

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-collect-d100-metrics_20260519T102321_result.json`
- **Structured JSON:** [`674214fb607e76ba5a45.json`](../../sessions/67/674214fb607e76ba5a45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从日志末尾的 summary 行提取到所有数据：

```json
{
  "gemma2_d100": {
    "train_loss": 1.258,
    "mean_token_accuracy": 0.7233,
    "entropy": 1.158,
    "train_runtime_sec": 11110,
    "done_sentinel": true
  },
  "olmo2_d100": {
    "train_loss": 0.9957,
    "mean_token_accuracy": 0.7459,
    "entropy": 1.122,
    "train_runtime_sec": 8584,
    "done_sentinel": true
  }
}
```

两个训练都已完成（epoch=1，.done sentinel 存在）。日志中没有 eval_loss/eval_accuracy，只有训练 metrics。OLMo-2 loss 明显更低（0.996 vs 1.258），token accuracy 也略高（0.746 vs 0.723），训练速度快约 23%（2h23m vs 3h05m）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gemma2_d100": {
      "train_loss": 1.258,
      "mean_token_accuracy": 0.7233,
      "entropy": 1.158,
      "train_runtime_sec": 11110,
      "done_sentinel": true
    },
    "olmo2_d100": {
      "train_loss": 0.9957,
      "mean_token_accuracy": 0.7459,
      "entropy": 1.122,
      "train_runtime_sec": 8584,
      "done_sentinel": true
    }
  }
}
```

</details>

---
