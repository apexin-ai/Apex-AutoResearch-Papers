# analysis loop only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loop_only_seed456_20260516T134041_result.json`
- **Structured JSON:** [`d92550aa455afba1fd86.json`](../../sessions/d9/d92550aa455afba1fd86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_results.json

```json
{
  "condition": "loop_only",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final",
  "metrics": {
    "accuracy": 0.8663865546218488,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.1512605042016807,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.9178743961352657,
    "pass_recall": 0.8930669800235017,
    "pass_f1": 0.905300774270399,
    "fail_precision": 0.7486187845303868,
    "fail_recall": 0.799410029498525,
    "fail_f1": 0.7731811697574893
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.8470378151260504,
    "accuracy_ci_upper": 0.8840336134453781,
    "majority_baseline_ci_lower": 0.6915966386554622,
    "majority_baseline_ci_upper": 0.738655462184874,
    "lift_ci_lower": 0.12268907563025211,
    "lift_ci_upper": 0.18067226890756305,
    "pass_precision_ci_lower": 0.9004681680331177,
    "pass_precision_ci_upper": 0.9353749943575383,
    "pass_recall_ci_lower": 0.8714256198347108,
    "pass_recall_ci_upper": 0.9140845811049194,
    "pass_f1_ci_lower": 0.8897009655310747,
    "pass_f1_ci_upper": 0.9187609585037989,
    "fail_precision_ci_lower": 0.7054011242647606,
    "fail_precision_ci_upper": 0.7930153268029049,
    "fail_recall_ci_lower": 0.7596410887858194,
    "fail_recall_ci_upper": 0.8395299145299144,
    "fail_f1_ci_lower": 0.7396449704142012,
    "fail_f1_ci_upper": 0.8047833058011855
  }
}
```

## Checkpoint 目录

| 文件 | 大小 |
|------|------|
| adapter_model.safetensors | 154 MB |
| tokenizer.json | 10.9 MB |
| vocab.json | 2.6 MB |
| merges.txt | 1.6 MB |
| predictions.jsonl | 77 KB |
| training_args.bin | 6.3 KB |
| README.md | 5.2 KB |
| chat_template.jinja | 2.5 KB |
| tokenizer_config.json | 4.6 KB |
| eval_results.json | 1.4 KB |
| adapter_config.json | 1.1 KB |
| added_tokens.json | 605 B |
| special_tokens_map.json | 499 B |

## 训练日志尾部（loss/accuracy）

训练已完成，评估推理过程中的 running accuracy 轨迹：

```
  [50/1190]  running accuracy: 0.9200
  [100/1190] running accuracy: 0.9600
  ...
  [1150/1190] running accuracy: 0.8617
```

最终评估结果：
- **Accuracy: 86.6%** (95% CI: [84.7%, 88.4%])
- Majority baseline: 71.5% (always predict 'pass')
- **Lift over majority: +15.1pp** (95% CI: [+12.3pp, +18.1pp])
- pass: P=0.92, R=0.89, F1=0.91
- fail: P=0.75, R=0.80, F1=0.77

## predictions.jsonl

**1190 行**（与测试样本数一致）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "condition": "loop_only",
    "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final",
    "metrics": {
      "accuracy": 0.8663865546218488,
      "majority_baseline": 0.7151260504201681,
      "lift": 0.1512605042016807,
      "majority_class": "pass",
      "n": 1190,
      "pass_precision": 0.9178743961352657,
      "pass_recall": 0.8930669800235017,
      "pass_f1": 0.905300774270399,
      "fail_precision": 0.7486187845303868,
      "fail_recall": 0.799410029498525,
      "fail_f1": 0.7731811697574893
    },
    "confidence_intervals": {
      "accuracy_ci_lower": 0.8470378151260504,
      "accuracy_ci_upper": 0.8840336134453781,
      "majority_baseline_ci_lower": 0.6915966386554622,
      "majority_baseline_ci_upper": 0.738655462184874,
      "lift_ci_lower": 0.12268907563025211,
      "lift_ci_upper": 0.18067226890756305,
      "pass_precision_ci_lower": 0.9004681680331177,
      "pass_precision_ci_upper": 0.9353749943575383,
      "pass_recall_ci_lower": 0.8714256198347108,
      "pass_recall_ci_upper": 0.9140845811049194,
      "pass_f1_ci_lower": 0.8897009655310747,
      "pass_f1_ci_upper": 0.9187609585037989,
      "fail_precision_ci_lower": 0.7054011242647606,
      "fail_precision_ci_upper": 0.7930153268029049,
      "fail_recall_ci_lower": 0.7596410887858194,
      "fail_recall_ci_upper": 0.8395299145299144,
      "fail_f1_ci_lower": 0.7396449704142012,
      "fail_f1_ci_upper": 0.8047833058011855
    }
  }
}
```

</details>

---
