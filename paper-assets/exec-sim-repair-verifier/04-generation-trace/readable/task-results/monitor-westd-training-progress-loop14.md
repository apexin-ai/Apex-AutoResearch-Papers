# monitor westd training progress loop14

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-training-progress-loop14_20260515T020040_result.json`
- **Structured JSON:** [`fba8f6e9aabbcaaaf8a8.json`](../../sessions/fb/fba8f6e9aabbcaaaf8a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/westd_status_loop14.md`。关键结果：

**ckpt-1000 Test Eval 已完成** — Accuracy 83.52%, F1 macro 77.50%
- fail: P=74.9% R=58.7% F1=65.8%
- pass: P=85.8% R=92.7% F1=89.1%
- GPU 0 已空闲

**三个训练正常运行**：
| 训练 | GPU | Step | 进度 | 预估完成 |
|------|-----|------|------|---------|
| cls-8b seed123 | 3 | 5400/6633 | 81% | ~13:00 今天 |
| cwm-8b s42 | 2 | 2900/6633 | 44% | ~23:00 今天 |
| cls-8b s42 resume | 1 | 1811/6633 | 27% | ~02:00 明天 |

无异常。磁盘 56% 充足。

---
