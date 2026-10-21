# diagnose plan 002 dryrun final

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-dryrun-final_20260514T050814_result.json`
- **Structured JSON:** [`a39b4be914e43db323d4.json`](../../sessions/a3/a39b4be914e43db323d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## dryrun-passed

训练完成，无 crash/OOM。EXIT_CODE=0。

**注意**：实际运行的日志在 `/tmp/dr4.log`（非 `plan002_dryrun.log`），且参数不同于原来的 run：
- 原 run：5880 samples, 1163 steps, 有 class weights + oversampling
- 当前 run：**1920 samples from 11 files, 383 steps, 无 class weights/oversampling**

### Train Metrics
| 指标 | 值 |
|------|------|
| train_loss | 0.6307 |
| train_runtime | 303.8s (5:03) |
| speed | 1.26 it/s |

### Eval Metrics
| 指标 | 值 |
|------|------|
| eval_loss | 0.4762 |
| eval_accuracy | **92.3%** |
| eval_f1_macro | **0.48** |
| eval_balanced_accuracy | **0.50** |

### Per-class
| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| deterministic | 0.923 | 1.000 | 0.96 |
| internal | **0.0** | **0.0** | **0.0** |

### Confusion Matrix
```
              pred_internal  pred_deterministic
true_internal      0              30
true_determ        0             360
```

### Per-task Accuracy
- **chemistry-mix: 0.000** (唯一含 internal 的 task，全部误判)
- 其余 10 个 task: 1.000

### Checkpoints
```
checkpoints/plan-002-dryrun/
├── checkpoint-383/
├── final_adapter/
└── eval_report.json
```

### 结论
**dryrun-passed**（训练流程正常完成），但模型学到了退化解——全部预测为 deterministic，internal 类完全漏判。balanced_accuracy=0.5 本质是随机猜。这个 run 没有启用 class weights 和 oversampling（原 run 有），可能是导致退化的原因。另外 GPU 上还有另一个进程 PID 789051 占用 28004 MiB。

---
