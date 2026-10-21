# ssh cuda1 eval batch 20260515

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cuda1_eval_batch_20260515_20260515T151333_result.json`
- **Structured JSON:** [`d4aa1a6f59e836ee1b71.json`](../../sessions/d4/d4aa1a6f59e836ee1b71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 10 次 eval 完成（总耗时 ~23 分钟）。汇总如下：

---

## 汇总

### 1. VOTA 重跑结果
- **Accuracy: 99.41%** (0.994118) — 符合预期，旧值 99.16% 已更新
- **predictions.jsonl: 1190 行** ✓

### 2. Staleness 检查
| Condition | Registry | 实测 | Match | predictions.jsonl |
|-----------|----------|------|-------|-------------------|
| no_trace | 75.13% | 75.13% | ✓ | 已生成 (1190行) |
| full_trace | 81.76% | 81.76% | ✓ | 已生成 (1190行) |
| exception_only | 99.83% | 99.83% | ✓ | 已生成 (1190行) |

所有 accuracy 与 registry 一致，无 staleness 问题。4 个条件的 predictions.jsonl 均已生成。

### 3. Epoch Accuracy 表格 (eval_qwen_epochs.sh)

| Condition | Epoch 1 (ckpt-148) | Epoch 2 (ckpt-296) | Final |
|-----------|--------------------|--------------------|-------|
| **vota** | 99.33% | 99.41% | 99.41% |
| **no_trace** | 74.29% | 76.30% | 75.13% |
| **full_trace** | 83.03% | 76.30% | 81.76% |

注意：
- **vota** 单调递增，epoch 2 ≈ final
- **no_trace** epoch 2 (76.30%) > final (75.13%)，说明 epoch 3 有轻微过拟合
- **full_trace** epoch 1 (83.03%) > epoch 2 (76.30%)，且 final (81.76%) 介于两者之间。epoch 2 出现明显下降后 final 恢复，可能 checkpoint-296 对应的不是 epoch 2 而是另一个 step，或存在训练不稳定

---
