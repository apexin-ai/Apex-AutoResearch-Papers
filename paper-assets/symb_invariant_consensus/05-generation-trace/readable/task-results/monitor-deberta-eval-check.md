# monitor deberta eval check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_deberta-eval-check_20260522T174750_result.json`
- **Structured JSON:** [`5065ad5608a1fb26d3bb.json`](../../sessions/50/5065ad5608a1fb26d3bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况更新：旧进程已死，新训练已启动。**

| 项目 | 详情 |
|------|------|
| **旧进程 (PID 650586)** | 已死亡，停在 step 4341/21820，无 eval 结果 |
| **新进程 (PID 653342)** | 01:47 启动，输出到 `/tmp/deberta_final.log` |
| **新运行参数** | epochs=2, batch-size=16, 本地 JSONL 数据 |
| **当前进度** | step 172/8728（2%），epoch 1 结束于 step 4364 |
| **速度** | ~3.5 it/s |
| **预计 epoch 1 完成** | 约 20 分钟后 |
| **Loss 趋势** | step 50: 0.7526 → step 150: 0.7242（在下降） |
| **Checkpoint** | 目录为空（刚开始，符合预期） |

Epoch 1 eval 还远未触发（差约 4200 步）。要等 ~20 分钟后再查 eval 结果。

---
