# urgent home val4096 check and next

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_home-val4096-check-and-next_20260514T123903_result.json`
- **Structured JSON:** [`527703a1d73596ae3df6.json`](../../sessions/52/527703a1d73596ae3df6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ckpt-600 eval 成功启动且运行正常。汇报如下：

---

## 1. ckpt-400 eval — 已完成 ✓

完成时间: 2026-05-14 05:32:50 UTC，总耗时 ~27.7 min

| 指标 | 值 |
|------|-----|
| **Accuracy** | **82.57%** (+6.7pp vs majority 75.9%) |
| **F1 macro** | **71.24%** |
| fail F1 | 53.18% (P=75.5%, R=41.0%) |
| pass F1 | 89.29% (P=83.6%, R=95.8%) |
| Unparseable | 1406/9335 (15.1%) |
| Total samples | 9335 |

混淆矩阵: TP=6784, FP=1328, FN=299, TN=924

## 2. ckpt-600 eval — 已启动 ✓

- tmux session: `ckpt600_eval`
- PID: 3097826
- GPU: 10734 MiB
- 启动时间: 06:00:48 UTC
- 当前进度: ~90/9335, running_acc=85.0%
- 速度: ~346 samples/min (同 ckpt-400)
- **预估完成: ~06:28 UTC** (约 27 min)

注意: 之前有另一个 worker 也启动了 ckpt-600 eval (`val-4096-cls-seed123-ckpt600` session)，导致两个进程写同一输出目录。已清理损坏数据并重新干净启动。

---
