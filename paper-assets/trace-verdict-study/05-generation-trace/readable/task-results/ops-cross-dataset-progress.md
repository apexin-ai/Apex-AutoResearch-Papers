# ops cross dataset progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cross_dataset_progress_20260522T060128_result.json`
- **Structured JSON:** [`161e9806754d0f59e65b.json`](../../sessions/16/161e9806754d0f59e65b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告：

## Cross-Dataset 训练进度

| # | 实验 | 状态 | Accuracy | pass_f1 | fail_f1 |
|---|------|------|----------|---------|---------|
| 1 | cross_he2mbpp_exception_only | **DONE** | **99.4%** | 0.996 | 0.991 |
| 2 | cross_he2mbpp_no_trace | **DONE** | **70.6%** | 0.807 | 0.376 |
| 3 | cross_mbpp2he_exception_only | **训练中** | — | — | — |
| 4 | cross_mbpp2he_no_trace | **未开始** | — | — | — |

### 实验 3 进度
- 训练步: 111/402 (28%)，~10.6s/step
- 预计训练剩余: ~51 min，加评估 ~10 min → **约 15:10 CST 完成**
- 实验 4 预计 ~17:30 CST 完成（整体 batch ~18:00 CST 前全部结束）

### HE→MBPP 结果分析
exception_only (99.4%) vs no_trace (70.6%)：差距 **28.8pp**，exception trace 在跨数据集泛化上碾压 no_trace baseline。no_trace 仅高于 majority baseline 1.5pp，fail_f1=0.376 说明几乎无法识别失败用例。

### cuda:1 状态
占用中（100% util, 87.8GB/97.9GB），跑 experiment 3。cuda:0 空闲（49.2GB 显存被占但 0% util）。

### 能否开始 Experiment 3（exception subcomponent ablation）？
**不能**，cuda:1 被 cross-dataset batch 占用，预计 ~18:00 CST 才释放。cuda:0 可用但有 49GB 显存被其他进程占用，需先确认该进程是否可以释放。

---
