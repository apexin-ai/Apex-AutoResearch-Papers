# ssh check 8b multiseed results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_8b_multiseed_results_20260518T011619_result.json`
- **Structured JSON:** [`06f8aaf2fe7bb42bdd75.json`](../../sessions/06/06f8aaf2fe7bb42bdd75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**两个实验都还在运行，并未退出。** EXIT_CODE=1 的报告有误。

### seed=123 (cuda:0, PID 37184)
- **训练**: 完成。checkpoint 存在 (`predictor_kl_normalized.pt`, 145MB)
- **Eval**: 正在运行中 (09:05 启动，已跑 ~13 分钟)
  - WikiText-2 PPL = **8.9267** (已完成)
  - ARC-Challenge: 已完成 (进度条 100%)
  - Winogrande + MMLU: 正在跑 (日志停在 MMLU 子数据集加载)
  - GSM8K: 待跑
- **results.json**: 尚未生成

### seed=456 (cuda:1, PID 37480)
- **训练**: 完成。checkpoint 存在 (`predictor_kl_normalized.pt`, 145MB)
- **Eval**: 正在运行中 (09:05 启动，已跑 ~13 分钟)
  - WikiText-2 PPL = **8.9614** (已完成)
  - ARC-Challenge: 已完成 (进度条 100%)
  - Winogrande + MMLU: 正在跑
  - GSM8K: 待跑
- **results.json**: 尚未生成

### 其他
- **GPU 占用**: 各 49GB / 98GB，正常
- **无 tmux 残留**
- **Model-level sparsity**: 两个 seed 均为 0.300，符合目标
- **无 OOM / crash / traceback**

MMLU 有 57 个子数据集，每个都要网络重试后 fallback 到缓存，预计 eval 全部完成还需 ~20-30 分钟。

---
