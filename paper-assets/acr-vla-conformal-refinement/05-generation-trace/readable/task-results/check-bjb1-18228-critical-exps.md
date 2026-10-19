# check bjb1 18228 critical exps

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-18228-critical-exps_20260524T192333_result.json`
- **Structured JSON:** [`11779e3f3db0384cd96c.json`](../../sessions/11/11779e3f3db0384cd96c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。汇总：

| 实验 | 状态 | 关键指标 |
|------|------|----------|
| **train-crm-pi05-unified-3suite-r2** | RUNNING (epoch 25/50) | best_val_loss=0.004854, 预计再~9h完成 |
| **eval-supp-spatial-vla-only-s42** | DONE | success_rate=**0.80** |
| **eval-supp-obj-vla-only-s50** | DONE | success_rate=**0.74** |
| **precompute-pi05-long-2048-r2** (PID 114507) | RUNNING | 174 .pt files cached, GPU 3 active |
| **precompute-pi05-object-2048-r2** | COMPLETED | 149 .pt files, 训练已在使用 |

**空闲资源**: GPU 1 和 GPU 2 完全空闲，可部署新实验。

Registry 已更新（两个 eval → DONE, CRM training → RUNNING with metrics）。报告已注册为 artifact `art_20260524_a2f605`。

---
