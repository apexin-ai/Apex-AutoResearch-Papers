# check n2 training status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_n2_training_status_20260515T122935_result.json`
- **Structured JSON:** [`389e61c66fb2b8639d67.json`](../../sessions/38/389e61c66fb2b8639d67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### n2_deberta_finetune_001 — **Running** (cuda:0, PID 231448, 已运行 ~18h)

| 指标 | 值 |
|------|-----|
| GPU 显存 | 21,340 MiB |
| 当前进度 | **Fold 2/5, Epoch 2/3, Step 350/1000** |
| Fold 1 完成 | epoch 1: val_acc=0.5437, epoch 2: val_acc=0.5258, epoch 3: val_acc=0.5540 |
| Fold 1 test acc | **0.5540** |
| Fold 2 当前 | epoch 1 val_acc=0.5288, epoch 2 进行中 |

结果目录的 `results.json` 是之前失败运行的残留（全 0，elapsed=3.5s），会被当前运行覆盖。

---

### n2_roberta_finetune_001 — **Running** (cuda:1, PID 235750, 已运行 ~5.5h)

| 指标 | 值 |
|------|-----|
| GPU 显存 | 8,132 MiB |
| 当前进度 | **Fold 1/5, Epoch 3/3, Step 550/1000** |
| Fold 1 epoch 1 | val_acc=0.4830 |
| Fold 1 epoch 2 | val_acc=0.5780 |
| Fold 1 epoch 3 | 进行中 (loss 在 0.23~0.60 区间) |

结果目录为空，尚未产出。

---

### 整体评估

- 两个进程均正常运行，GPU 占用正常
- DeBERTa 用了 ~18h 完成 1.3/5 folds；RoBERTa 用了 ~5.5h 接近完成第 1 fold（显存仅 8GB，推理更快）
- DeBERTa fold 1 test_acc=0.5540，RoBERTa fold 1 val_acc 已达 0.5780（epoch 2），两者目前均远低于 RF baseline 78.2%
- 按当前速度估算：DeBERTa 大约还需 ~50h 完成全部 5 folds；RoBERTa 大约还需 ~22h
- **val_acc 在 0.48~0.58 区间徘徊，且 DeBERTa fold 1 三个 epoch 后 val_acc 几乎没提升（0.54→0.53→0.55），可能存在学习率或特征表示问题**

---
