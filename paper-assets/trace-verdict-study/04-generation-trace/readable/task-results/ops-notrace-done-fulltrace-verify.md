# ops notrace done fulltrace verify

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_notrace-done-fulltrace-verify_20260514T223731_result.json`
- **Structured JSON:** [`c738c054183e75c222b3.json`](../../sessions/c7/c738c054183e75c222b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## no_trace_seed42_v4 最终结果
- PID 835084: **已退出** (DONE)
- accuracy: **75.13%**
- majority_baseline: 71.51%
- lift: **+3.61%**
- pass_f1: 0.8134, fail_f1: 0.6272
- pass_precision: 0.8776, pass_recall: 0.7579
- fail_precision: 0.5473, fail_recall: 0.7345
- n: 1190
- checkpoint_path: `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/`
- train_loss: 0.1800, eval_loss: 0.6454
- train_runtime: 1274.7s (21m14s), 444/444 steps

&lt;details>&lt;summary>完整 eval_results.json&lt;/summary>

```json
{
  "condition": "no_trace",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final",
  "metrics": {
    "accuracy": 0.7512605042016807,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.03613445378151259,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.8775510204081632,
    "pass_recall": 0.7579318448883666,
    "pass_f1": 0.8133669609079445,
    "fail_precision": 0.5472527472527473,
    "fail_recall": 0.7345132743362832,
    "fail_f1": 0.6272040302267003
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.7277310924369748,
    "accuracy_ci_upper": 0.7747899159663866,
    "lift_ci_lower": 0.004201680672268893,
    "lift_ci_upper": 0.07058823529411762,
    "pass_f1_ci_lower": 0.7928025838972547,
    "pass_f1_ci_upper": 0.8325087319589699,
    "fail_f1_ci_lower": 0.5902680712254419,
    "fail_f1_ci_upper": 0.6650001556662515
  }
}
```
&lt;/details>

## full_trace_seed42_v2 启动确认
- PID 837515: **存活** (bash wrapper), 子进程 PID 837520 (python) 在 cuda:0
- cuda:0 显存占用: **32,252 MiB** / 97,887 MiB (GPU-Util 100%)
- 训练已开始: step 54/444 (12%), ~15:36 elapsed, ETA ~1h54m
- 速度: ~17.4s/step

## vota_seed42_v4 进度
- cuda:1 有两个 python 进程 (PID 836281: 41,182 MiB, PID 838082: 15,584 MiB)
- vota 日志显示正在 tokenizing eval dataset，即将开始训练（或刚完成 tokenize 准备 training）
- 日志末尾: `Starting training...` → step 54/444 (12%), ~15:36 elapsed

注意：vota 日志的尾部内容与 full_trace 非常相似（都在 step 54 左右），两个任务均在正常训练中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "condition": "no_trace",
    "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final",
    "metrics": {
      "accuracy": 0.7512605042016807,
      "majority_baseline": 0.7151260504201681,
      "lift": 0.03613445378151259,
      "majority_class": "pass",
      "n": 1190,
      "pass_precision": 0.8775510204081632,
      "pass_recall": 0.7579318448883666,
      "pass_f1": 0.8133669609079445,
      "fail_precision": 0.5472527472527473,
      "fail_recall": 0.7345132743362832,
      "fail_f1": 0.6272040302267003
    },
    "confidence_intervals": {
      "accuracy_ci_lower": 0.7277310924369748,
      "accuracy_ci_upper": 0.7747899159663866,
      "lift_ci_lower": 0.004201680672268893,
      "lift_ci_upper": 0.07058823529411762,
      "pass_f1_ci_lower": 0.7928025838972547,
      "pass_f1_ci_upper": 0.8325087319589699,
      "fail_f1_ci_lower": 0.5902680712254419,
      "fail_f1_ci_upper": 0.6650001556662515
    }
  }
}
```

</details>

---
