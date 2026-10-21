# analyze codellama13b vota seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_vota_seed42_20260516T182221_result.json`
- **Structured JSON:** [`85f2c02c5b5bb07a0165.json`](../../sessions/85/85f2c02c5b5bb07a0165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验 `codellama13b_vota_seed42` 结果

### 1. eval_results.json（完整内容）

```json
{
  "condition": "vota",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final",
  "metrics": {
    "accuracy": 0.9857142857142858,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.2705882352941177,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.9882903981264637,
    "pass_recall": 0.9917743830787309,
    "pass_f1": 0.9900293255131964,
    "fail_precision": 0.9791666666666666,
    "fail_recall": 0.9705014749262537,
    "fail_f1": 0.9748148148148148
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.9789915966386554,
    "accuracy_ci_upper": 0.9915966386554622,
    "majority_baseline_ci_lower": 0.6915966386554622,
    "majority_baseline_ci_upper": 0.738655462184874,
    "lift_ci_lower": 0.246218487394958,
    "lift_ci_upper": 0.2958193277310925,
    "pass_precision_ci_lower": 0.9812195526097762,
    "pass_precision_ci_upper": 0.9943965499821503,
    "pass_recall_ci_lower": 0.9848656824355311,
    "pass_recall_ci_upper": 0.9975792011719942,
    "pass_f1_ci_lower": 0.985107141334265,
    "pass_f1_ci_upper": 0.994286525974026,
    "fail_precision_ci_lower": 0.9620972801417131,
    "fail_precision_ci_upper": 0.9935095955000414,
    "fail_recall_ci_lower": 0.9522388059701492,
    "fail_recall_ci_upper": 0.9863545949698296,
    "fail_f1_ci_lower": 0.9622912381735911,
    "fail_f1_ci_upper": 0.9856749417625182
  }
}
```

### 2. 训练日志尾部（最后 80 行）

训练正常结束（`EXIT_CODE=0`）。日志显示评估阶段：

- 加载 LoRA adapter 从 `codellama13b_vota_seed42/final`
- 在 1190 个测试样本上推理，running accuracy 从 1.0000 逐步稳定到 0.9852
- 最终结果：

```
=== Evaluation Results (condition: vota) ===
Accuracy:           98.6% (95% CI: [97.9%, 99.2%])
Majority baseline:  71.5% (always predict 'pass')
Lift over majority: +27.1pp (95% CI: [+24.6pp, +29.6pp])

Per-class metrics:
  pass:  P=0.99  R=0.99  F1=0.99
  fail:  P=0.98  R=0.97  F1=0.97

Bootstrap: 1000 resamples
```

### 3. Checkpoint 目录内容

```
-rw-r--r-- root root      5264 May 17 02:14 README.md
-rw-r--r-- root root      1128 May 17 02:14 adapter_config.json
-rw-r--r-- root root 250422888 May 17 02:14 adapter_model.safetensors  (238MB)
-rw-r--r-- root root       813 May 17 02:14 chat_template.jinja
-rw-r--r-- root root      1417 May 17 02:19 eval_results.json
-rw-r--r-- root root     77430 May 17 02:19 predictions.jsonl
-rw-r--r-- root root       538 May 17 02:14 special_tokens_map.json
-rw-r--r-- root root   3620731 May 17 02:14 tokenizer.json
-rw-r--r-- root root    500058 May 17 02:14 tokenizer.model
-rw-r--r-- root root      1869 May 17 02:14 tokenizer_config.json
-rw-r--r-- root root      6481 May 17 02:14 training_args.bin
```

### 4. predictions.jsonl 前 5 条

```jsonl
{"id": 0, "label": "fail", "pred": "fail", "raw_pred": "fail"}
{"id": 1, "label": "pass", "pred": "pass", "raw_pred": "pass"}
{"id": 2, "label": "fail", "pred": "fail", "raw_pred": "fail"}
{"id": 3, "label": "fail", "pred": "fail", "raw_pred": "fail"}
{"id": 4, "label": "pass", "pred": "pass", "raw_pred": "pass"}
```

---
