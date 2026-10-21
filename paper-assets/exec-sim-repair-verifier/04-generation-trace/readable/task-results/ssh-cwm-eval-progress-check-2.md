# ssh cwm eval progress check 2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-eval-progress-check-2_20260524T091646_result.json`
- **Structured JSON:** [`4f2c28072d8e701d1c83.json`](../../sessions/4f/4f2c28072d8e701d1c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM Eval 4 路任务进度

| # | GPU | 配置 | 进度 | Acc | 速度 | 预计剩余 |
|---|-----|------|------|-----|------|----------|
| 1 | cuda:0 | s456 / ckpt300 / seq2048 | **7968/9784** (81.4%) | 66.2% | ~8 samples/57s | ~3.6h |
| 2 | cuda:1 | s42 / ckpt300 / seq2048 | **6672/9784** (68.2%) | 68.3% | ~8 samples/54s | ~5.8h |
| 3 | cuda:2 | s123 / ckpt300 / seq2048 | **7800/9784** (79.7%) | 64.0% | ~8 samples/58s | ~4.0h |
| 4 | cuda:3 | s42 / ckpt6100 / seq8192 | **4808/9784** (49.1%) | 70.3% | ~4 samples/21s | ~7.3h |

**要点：**
- 4 路全部运行中，GPU 利用率 60-94%
- 任务 1/3 有 resumed 样本（断点续跑），任务 2/4 是全新跑
- 任务 4 配置不同（ckpt6100 + seq8192 + batch4），速度最慢但 acc 最高（70.3%）
- 最快完成：任务 1（~21:00），全部完成：任务 4（~次日 00:30）

---
