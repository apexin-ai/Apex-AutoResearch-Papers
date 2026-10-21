# check n2 deberta status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_n2_deberta_status_20260515T121811_result.json`
- **Structured JSON:** [`12e8934f885fbf8b092a.json`](../../sessions/12/12e8934f885fbf8b092a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n2_deberta_finetune_001 训练状态

**状态：RUNNING**

| 项目 | 详情 |
|------|------|
| PID | 231453，启动于 20:12 UTC |
| 当前进度 | **Fold 1/5, Epoch 2/3, step 600/1000** |
| 总进度 | ~1,600 / 15,000 steps (~11%) |
| Epoch 1 结果 | train_loss=0.7749, val_acc=**0.5437** |
| Epoch 2 loss 趋势 | 0.52 → 0.37（在下降） |
| 训练配置 | batch=16, lr=2e-5, epochs=3, max_len=512, 5-fold CV |

**GPU 使用：**
- GPU 0: **98% 利用率**, 21.3GB/97.9GB VRAM, 73°C
- GPU 1: 空闲 (0%)

**预估剩余时间：** 已跑约 6 分钟完成 11%，预计还需 ~50 分钟。

**注意：** results.json 是之前一次失败运行的残留（1 epoch, 1 fold, 全零），当前运行会覆盖它。

Epoch 1 的 val_acc 54.4% 暂时远低于 RF baseline 78.2%，但 DeBERTa finetune 前期正常——loss 仍在快速下降，后续 epoch 和 fold 预计会有明显提升。

---
