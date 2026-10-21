# ssh gpu status check all

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_all_20260521T023951_result.json`
- **Structured JSON:** [`392c181430bcb35a2dc9.json`](../../sessions/39/392c181430bcb35a2dc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### westd-29022（4× RTX PRO 6000, 96GB each）
- **GPU**: 全部空闲，0% 利用率，0MB 显存占用
- **SFT CKA-only 25%**: **已完成** ✓
  - 训练 2 epoch，总用时 1644s（~27min）
  - 最终 loss=0.6508，mean_token_accuracy=0.8285
  - 模型已保存，日志最后一行：`SFT recovery complete.`
  - 进程 307651 已退出

### westb-23072（2× RTX PRO 6000, 96GB each）
- **GPU 0**: 100% 利用率，30853MiB 占用（PID 59509）
- **GPU 1**: 90% 利用率，12315MiB 占用（PID 59668）
- **MATH-500 eval**（PID 59502）: **运行中**，已跑 34min，进度 7/500（1.4%）。每题 ~227s，极慢，预计还需 ~31h
- **HumanEval eval**（PID 59663）: **运行中**，已跑 33min，进度 158/164（96%）。每题 ~11.5s，预计 ~1min 内完成

### 关注点
MATH-500 速度异常慢（227s/题 vs HumanEval 11s/题），可能是生成长度没设上限或 batch_size=1 问题。

---
