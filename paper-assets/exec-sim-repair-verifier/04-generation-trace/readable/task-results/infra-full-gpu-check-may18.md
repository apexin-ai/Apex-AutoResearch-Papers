# infra full gpu check may18

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-gpu-check-may18_20260518T133947_result.json`
- **Structured JSON:** [`89adebbb8bac090988a8.json`](../../sessions/89/89adebbb8bac090988a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张卡都在跑，无已完成任务。汇总：

| GPU | 任务 | 进度 | 关键指标 | GPU 利用率 | 显存 | 预估剩余 |
|-----|------|------|----------|-----------|------|----------|
| **0** | CLS v5 retrain | 3889/6315 steps (**61%**), epoch 2 进行中 | epoch 1 eval_loss=0.0886, checkpoint-2105 已保存 | 99% | 24.9/32.6 GB | ~6.5h (~10s/it) |
| **1** | CWM s42 epoch 3 eval (seq4096) | 6158/9784 samples (**63%**) | running_acc=**56.4%** | 56% | 17.7/32.6 GB | ~13h (~13s/sample) |
| **2** | CWM s42 epoch 2 eval (seq8192) | 3002/9784 samples (**31%**) | running_acc=**66.9%** | 56% | 17.9/32.6 GB | ~22h (~12s/sample) |
| **3** | CWM s123 eval (seq4096) | 5754/9784 samples (**59%**) | running_acc=**61.6%** | 51% | 17.7/32.6 GB | ~16h (~14s/sample) |

值得注意：**CWM s42 epoch 2 (seq8192) 的 running_acc 66.9% 大幅领先 epoch 3 (best, seq4096) 的 56.4%**。epoch 2 用了 8192 seq length vs epoch 3 的 4096，序列长度对 CWM 任务影响显著。s123 seed 的 61.6% 也高于 s42 epoch 3，但低于 s42 epoch 2。

---
