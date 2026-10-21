# analysis no trace seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_no_trace_seed123_20260522T234037_result.json`
- **Structured JSON:** [`92648dc4d9dbba14fea9.json`](../../sessions/92/92648dc4d9dbba14fea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据拿到了。

## 结果汇总

- **训练状态**: 正常完成（EXIT_CODE=0，3 epochs / 444 steps，耗时 21 分钟）
- **accuracy**: 79.08%
- **fail_f1**: 68.44%
- **pass_f1**: 84.35%
- **fail_precision**: 60.00%
- **fail_recall**: 79.65%
- **pass_precision**: 90.68%
- **pass_recall**: 78.85%
- **majority_baseline**: 71.51%，lift: +7.56pp
- **n**: 1190 样本
- **95% CI**: accuracy [76.81%, 81.26%], fail_f1 [64.80%, 71.89%]
- **vs seed42**: accuracy **+3.95pp** (79.08% vs 75.13%), fail_f1 **+5.72pp** (68.44% vs 62.72%)
- **checkpoint_path**: `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed123/final`
- **log_path**: `~/runs/trace-verdict-study/no_trace_seed123.log`
- **W&B**: 未记录（日志中无 wandb 初始化痕迹）
- **conclusion 建议**: **success**
- **理由**: seed123 显著优于 seed42（accuracy +3.95pp, fail_f1 +5.72pp），说明 no_trace baseline 在 seed42 上的表现偏低，seed123 给出了更强的 baseline 数字。两个 seed 均显著高于 majority baseline（71.51%），训练正常收敛（final train_loss=0.178，eval_loss=0.637）。

---
