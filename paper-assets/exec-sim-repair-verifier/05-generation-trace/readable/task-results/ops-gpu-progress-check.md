# ops gpu progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-progress-check_20260524T032820_result.json`
- **Structured JSON:** [`d8cc41be152c963baa78.json`](../../sessions/d8/d8cc41be152c963baa78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## CWM Eval 进度汇总 (May 24, ~11:30)

| GPU | 实验 | 进度 | Running Acc | 速率 | ETA |
|-----|------|------|-------------|------|-----|
| 0 | s456 ckpt300 reeval (seq2048) | **5016/9784 (51.3%)** | **65.9%** | ~8.3/min | ~21:05 |
| 1 | s42 ckpt300 reeval (seq2048) | **3552/9784 (36.3%)** | **68.9%** | ~8.9/min | ~23:10 |
| 2 | s123 ckpt300 reeval (seq2048) | **4856/9784 (49.6%)** | **64.3%** | ~8.3/min | ~21:25 |
| 3 | s42 ckpt6100 eval (seq8192) | **760/9784 (7.8%)** | **70.9%** | ~12/min | ~May 25 00:00 |

**空闲 GPU: 无**（4 张全满载，利用率 76%-90%）

### 补充信息

- **之前的 ckpt6100 seq4096 eval (PID 272025)**: 已完成，9784/9784，**accuracy = 69.50%** (6800/9784)
- s456 和 s123 的 reeval 有 resumed 样本（分别 1306 和 1162 条来自之前的 partial run），s42 ckpt300 是全新 eval（resumed=0），所以 s42 进度更慢但速率其实接近
- GPU 3 的 seq8192 eval PID 为 328069（batch_size=4, max_new_tokens=512），每 batch ~20s，单样本速率反而比 seq2048 的 eval 更快

---
