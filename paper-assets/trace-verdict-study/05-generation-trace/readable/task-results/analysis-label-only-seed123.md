# analysis label only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_label_only_seed123_20260516T085944_result.json`
- **Structured JSON:** [`4f922adceeda978f901a.json`](../../sessions/4f/4f922adceeda978f901a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_results.json

```json
{
  "condition": "full_trace",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final",
  "metrics": {
    "accuracy": 0.8705882352941177,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.15546218487394958,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.8626430801248699,
    "pass_recall": 0.9741480611045829,
    "pass_f1": 0.9150110375275937,
    "fail_precision": 0.9039301310043668,
    "fail_recall": 0.6106194690265486,
    "fail_f1": 0.7288732394366197
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.8529201680672268,
    "accuracy_ci_upper": 0.888235294117647,
    "majority_baseline_ci_lower": 0.6915966386554622,
    "majority_baseline_ci_upper": 0.738655462184874,
    "lift_ci_lower": 0.13277310924369745,
    "lift_ci_upper": 0.17983193277310916,
    "pass_precision_ci_lower": 0.8424747665162173,
    "pass_precision_ci_upper": 0.8824794701054377,
    "pass_recall_ci_lower": 0.9631316542189735,
    "pass_recall_ci_upper": 0.9839542916745057,
    "pass_f1_ci_lower": 0.9028577495953044,
    "pass_f1_ci_upper": 0.9270966492406679,
    "fail_precision_ci_lower": 0.8655421784098255,
    "fail_precision_ci_upper": 0.9396577690070628,
    "fail_recall_ci_lower": 0.5603969586003459,
    "fail_recall_ci_upper": 0.6609207682483544,
    "fail_f1_ci_lower": 0.6862358534788723,
    "fail_f1_ci_upper": 0.7684567891030516
  }
}
```

### **Accuracy: 87.1% (95% CI: [85.3%, 88.8%])**

Lift over majority baseline (+15.5pp)。fail recall 偏低 (0.61)，模型倾向预测 pass。

---

## 日志尾部 (最后 50 行)

```
Training complete. Model saved to /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final
Condition: full_trace
Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final
Test samples: 1190
Loading base model from /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct
Loading checkpoint shards: 100%|██████████| 4/4 [00:03<00:00,  1.26it/s]
Loading LoRA adapter from /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final
Running inference...
  [50/1190] running accuracy: 0.9800
  [100/1190] running accuracy: 0.9200
  ...
  [1150/1190] running accuracy: 0.8748

Computing metrics...

=== Evaluation Results (condition: full_trace) ===
Accuracy:           87.1% (95% CI: [85.3%, 88.8%])
Majority baseline:  71.5% (always predict 'pass')
Lift over majority: +15.5pp (95% CI: [+13.3pp, +18.0pp])

Per-class metrics:
  pass:  P=0.86  R=0.97  F1=0.92
  fail:  P=0.90  R=0.61  F1=0.73

Bootstrap: 1000 resamples
Predictions saved to .../final/predictions.jsonl
Results saved to .../final/eval_results.json
EXIT_CODE=0
```

训练和评估正常结束，退出码 0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "condition": "full_trace",
    "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final",
    "metrics": {
      "accuracy": 0.8705882352941177,
      "majority_baseline": 0.7151260504201681,
      "lift": 0.15546218487394958,
      "majority_class": "pass",
      "n": 1190,
      "pass_precision": 0.8626430801248699,
      "pass_recall": 0.9741480611045829,
      "pass_f1": 0.9150110375275937,
      "fail_precision": 0.9039301310043668,
      "fail_recall": 0.6106194690265486,
      "fail_f1": 0.7288732394366197
    },
    "confidence_intervals": {
      "accuracy_ci_lower": 0.8529201680672268,
      "accuracy_ci_upper": 0.888235294117647,
      "majority_baseline_ci_lower": 0.6915966386554622,
      "majority_baseline_ci_upper": 0.738655462184874,
      "lift_ci_lower": 0.13277310924369745,
      "lift_ci_upper": 0.17983193277310916,
      "pass_precision_ci_lower": 0.8424747665162173,
      "pass_precision_ci_upper": 0.8824794701054377,
      "pass_recall_ci_lower": 0.9631316542189735,
      "pass_recall_ci_upper": 0.9839542916745057,
      "pass_f1_ci_lower": 0.9028577495953044,
      "pass_f1_ci_upper": 0.9270966492406679,
      "fail_precision_ci_lower": 0.8655421784098255,
      "fail_precision_ci_upper": 0.9396577690070628,
      "fail_recall_ci_lower": 0.5603969586003459,
      "fail_recall_ci_upper": 0.6609207682483544,
      "fail_f1_ci_lower": 0.6862358534788723,
      "fail_f1_ci_upper": 0.7684567891030516
    }
  }
}
```

</details>

---
