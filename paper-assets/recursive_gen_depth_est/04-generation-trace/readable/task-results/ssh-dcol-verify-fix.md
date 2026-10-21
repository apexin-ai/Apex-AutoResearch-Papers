# ssh dcol verify fix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dcol_verify_fix_20260514T163519_result.json`
- **Structured JSON:** [`be39be2fb36d13723954.json`](../../sessions/be/be39be2fb36d13723954.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成。验证结果：

## 6 项验证清单

| # | 验证项 | 结果 | 详情 |
|---|--------|------|------|
| 1 | train/val/test 三组数据量 | **通过** | train=14000, val=3000, test=3000（总 20000，比例 70/15/15） |
| 2 | 训练只打印 train/val loss | **通过** | 每 epoch 输出 Train loss + Val loss，无 test loss |
| 3 | Early stopping 基于 val loss | **通过** | `Best model saved (val_loss=...)` 均基于 val_loss |
| 4 | 独立 Test Set Evaluation | **通过** | 训练后有 `Test Set Evaluation (held-out)` 区块 |
| 5 | Test acc ≠ Val acc | **通过** | Val acc=0.7607, Test acc=0.7513（差 0.94pp） |
| 6 | Loss 合理、逐 epoch 下降 | **通过** | 无 NaN/Inf，train loss 1.5601→1.2397→1.2008，val loss 1.1969→1.1085→1.0949 |

## 具体数字

**Split**: train 14000 / val 3000 / test 3000（各 depth 均 5000 样本，4 类均衡）

**Epoch 训练过程**:
| Epoch | Train Loss | Train Acc | Val Loss | Val Acc |
|-------|-----------|-----------|----------|---------|
| 1 | 1.5601 | 0.6493 | 1.1969 | 0.7410 |
| 2 | 1.2397 | 0.7233 | 1.1085 | 0.7577 |
| 3 | 1.2008 | 0.7317 | 1.0949 | 0.7607 |

**最终评估**: Val acc=0.7607, Test acc=0.7513 (4-class), Test 3-class acc=0.6698

3-way split 修复验证全部通过。

---
