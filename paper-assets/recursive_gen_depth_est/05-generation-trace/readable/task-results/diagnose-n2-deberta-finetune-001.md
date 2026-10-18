# diagnose n2 deberta finetune 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_n2_deberta_finetune_001_20260515T131545_result.json`
- **Structured JSON:** [`dd517f8376531688bf80.json`](../../sessions/dd/dd517f8376531688bf80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：非失败 — 实验已正常完成

EXIT_CODE=129 (SIGHUP) **不是训练中途崩溃**。日志显示 5/5 folds 全部跑完，结果已保存到 `results.json` 和 `fold_predictions.npz`。SIGHUP 发生在训练结束之后，最可能的原因是：启动训练的 SSH session/tmux 在脚本完成后断开，bash wrapper 收到 SIGHUP 信号，导致 exit code 被覆盖为 129。**训练本身成功完成。**

### 训练进度：全部完成

- 5 个 fold × 3 epochs × 1000 steps = 全部跑完
- 总耗时 3727 秒（~62 分钟）

### 结果摘要

| 指标 | 值 |
|------|-----|
| **Accuracy** | 0.5831 ± 0.0467 |
| **Per-class F1** | d0=0.947, d1=0.378, d2=0.247, d3=0.656 |
| **Pairwise AUC** | d0v1=0.981, d1v2=0.733, d2v3=0.755 |

### 产出文件

- `results/n2_deberta_finetune/results.json` (2.8KB)
- `results/n2_deberta_finetune/fold_predictions.npz` (1MB)

### 服务器状态

- GPU 0 空闲（0MiB），GPU 1 被另一进程(PID 243827)使用
- 磁盘充足：根分区 25% 使用，数据盘 40% 使用

### 重跑建议

不需要重跑 — 实验已完成。可直接使用 `results.json` 中的结果。注意 depth 1 和 depth 2 的分类表现较弱（F1 < 0.4），如果需要改进，可以考虑增加 epochs、调整类别权重、或使用更大的模型。

---
