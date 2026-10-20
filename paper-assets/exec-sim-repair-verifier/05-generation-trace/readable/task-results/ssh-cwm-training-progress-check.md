# ssh cwm training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-training-progress-check_20260520T015540_result.json`
- **Structured JSON:** [`c9f4d528dc44d5011b5f.json`](../../sessions/c9/c9f4d528dc44d5011b5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态总览

| GPU | Temp | Power | VRAM | Util | 进程 PID |
|-----|------|-------|------|------|----------|
| 0 | 73°C | 508/575W | 21253/32607 MiB | 97% | 886278 |
| **1** | **41°C** | **112/575W** | **0/32607 MiB** | **100%** | **无进程** |
| 2 | 66°C | 431/575W | 16709/32607 MiB | 89% | 885624 |
| 3 | 75°C | 550/575W | 31259/32607 MiB | 98% | 886352 |

**GPU 1 仍然 hung**：100% utilization、0 MiB memory、无进程，与之前状态一致。

**RAM：52 GiB / 754 GiB (7%)** — 安全。

---

## 训练进度汇总

| exp_id | GPU | PID | step/total | progress | loss | speed | ETA | 备注 |
|--------|-----|-----|-----------|----------|------|-------|-----|------|
| deepseek-cwm-repo-s123-train | 2 | 885624 | 966/2865 | 33.7% | train=0.0448, eval=0.0425 | ~1.8 s/it | ~57 min + 2次eval ≈ **~1h** | 刚完成 epoch 1.0 eval，loss 从 2.57→0.045 收敛良好 |
| qwen3-8b-cwm-repo-s123-train-v4 | 0 | 886278 | 100/6633 | 1.5% | 18.50 (step 100) | ~12.2 s/it | **~22h** | 刚开始，loss 从 24.5→18.5 快速下降中 |
| qwen3-8b-cwm-repo-s456-train-v3 | 3 | 886352 | ~100/6633 训练 + 正在跑 val eval (331/9335) | ~1.5% | 尚未记录 | ~12 s/it (训练) | **~22h** | 训练约100步后触发首次 val eval，eval 进度 3.5% |

**关键观察**：
- 3 个训练进程全部存活，PID 与预期一致（deepseek 确认是重启后的 885624）
- deepseek 进展最快（33%），预计 ~1h 后完成；两个 qwen3-8b 刚起步（1.5%），需要约 22h
- deepseek loss 收敛健康：epoch 1 train_loss 0.045，eval_loss 0.043
- qwen3-8b s123 的 loss 仍在早期高位（18.5），正在快速下降中（使用了 class_weight 的加权 loss，数值较大是正常的）
- GPU 1 持续 hung，建议在当前 3 个训练完成后再处理

---
