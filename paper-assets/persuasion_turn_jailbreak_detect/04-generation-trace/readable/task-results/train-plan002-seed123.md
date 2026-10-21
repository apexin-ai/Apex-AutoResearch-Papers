# train plan002 seed123

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan002-seed123_20260518T001245_result.json`
- **Structured JSON:** [`b5f662e0aa777188cf30.json`](../../sessions/b5/b5f662e0aa777188cf30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_002 seed=123 全部 4 个阶段完成。**

### 结果汇总

**Stage 1: DeBERTa Multi-task Fine-tuning**
- Best epoch: 3 (seed=42 是 epoch 2)
- Val persuasion acc: 0.8302 (seed=42: 0.8285)
- Val intent acc: 1.0
- Val loss: 0.4515 (seed=42: 0.4759)

**Stage 2-3: GRU Classifiers**
- Treatment GRU: val_acc=1.0, loss=0.0
- Baseline GRU: val_acc=0.9865, best_loss=0.0324

**Stage 4: Early Detection Evaluation (test set, N=76)**

| K | Treatment F1 | Baseline F1 | TF-IDF F1 |
|---|---|---|---|
| 1 | 1.0000 | 0.9870 | 1.0000 |
| 2 | 1.0000 | 0.9867 | 1.0000 |
| 3 | 1.0000 | 1.0000 | 1.0000 |
| 5 | 1.0000 | 1.0000 | 1.0000 |
| full | 1.0000 | 1.0000 | 1.0000 |

与 seed=42 一致：Treatment 和 TF-IDF 在所有 K 值上完美，Baseline 在 K=1,2 时略低。结果稳定。

**产出文件：**
- `checkpoints/plan_002_seed123/deberta_multitask/best/` (model + training_metrics.json)
- `checkpoints/plan_002_seed123/gru/treatment/best.pt`
- `checkpoints/plan_002_seed123/gru/baseline/best.pt`
- `results/plan_002_seed123_eval.json`

---
