# diag qwen15b full trace tail256 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen15b_full_trace_tail256_seed42_20260517T204326_result.json`
- **Structured JSON:** [`5c16947430cd3daed766.json`](../../sessions/5c/5c16947430cd3daed766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有失败**。诊断结果：

## 实际状态：训练和评估均已成功完成

**日志证据**（424行，零错误）：
- 训练：3 epochs / 444 steps，`train_loss=0.269`，耗时 8m39s
- 模型已保存：`/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail256_seed42/final/`（adapter + tokenizer + eval_results 全部就位）
- 评估结果：**Accuracy 72.6%** (CI: 70.0%–75.3%)，majority baseline 71.5%，lift +1.1pp

**grep 全日志无任何**：Error / Exception / Traceback / OOM / killed / crash。唯一匹配 "fail" 的行是评估指标里的 `fail: P=0.52 R=0.57 F1=0.54`。

## "无 W&B metrics" 的原因

日志中**完全没有 wandb 相关输出**——W&B 从未被初始化。不是 crash 导致没上报，而是这次运行根本没启用 W&B logging。可能训练命令缺少 `--report_to wandb` 或相关环境变量未设置。

## 环境状态
- **进程残留**：无 train.py 进程
- **GPU 1**：空闲（0MiB / 0%）
- **磁盘**：root overlay 80% (6.2G 剩余)，不是瓶颈

## 结论

这不是实验失败，而是**实验已成功但缺少 W&B tracking**。如果需要 W&B 记录，在训练命令中加 `--report_to wandb` 重跑，或直接使用已保存的 `eval_results.json` 提取结果。

---
