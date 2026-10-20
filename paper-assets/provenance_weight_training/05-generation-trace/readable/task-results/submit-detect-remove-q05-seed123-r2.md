# submit detect remove q05 seed123 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_detect_remove_q05_seed123_r2_20260518T083626_result.json`
- **Structured JSON:** [`4529ed19afa99746aefe.json`](../../sessions/45/4529ed19afa99746aefe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 项目 | 值 |
|---|---|
| **PID** | 22336 |
| **GPU** | cuda:0, 41757MiB (~41GB) |
| **速度** | ~2.10s/it (~28 steps/min) |
| **总步数** | 6103 |
| **ETA** | ~3h33min（约 20:30 北京时间） |
| **Registry** | RUNNING，spec 已更新 |

显存 41GB 符合预期（之前是 70GB）。速度 ~28 steps/min，比之前的 12 steps/min 快 2.3x，但未达到 50+ steps/min——可能是因为 gradient_accumulation_steps=4 使每个 logging step 包含 4 个 forward+backward，2.10s/step 对应每个 micro-batch ~0.53s，属于合理范围。

---
