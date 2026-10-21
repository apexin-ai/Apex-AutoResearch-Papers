# ops cwm eval bs8 restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-eval-bs8-restart_20260523T201219_result.json`
- **Structured JSON:** [`76f9cdb10a546985c243.json`](../../sessions/76/76f9cdb10a546985c243.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 5: 汇报**

| 项目 | s456 (cuda:0) | s123 (cuda:2) |
|------|--------------|--------------|
| PID | 309505 | 309866 |
| 断点续传 | 跳过 1306 已完成，从 1312/9784 续传 | 跳过 1162 已完成，从 1168/9784 续传 |
| incremental 行数 | 1320 | 1168 |
| 显存占用 | 21124 MiB / 32607 MiB | 21252 MiB / 32607 MiB |
| GPU 利用率 | 88% | 88% |

**断点续传正常**，两个进程都正确跳过了之前 bs=1 已完成的样本。

**ETA 估算**：
- s456：剩余 9784 - 1320 = 8464 样本，bs=8 约每 48s 处理 8 样本，约 **14.1 小时**
- s123：剩余 9784 - 1168 = 8616 样本，同速约 **14.4 小时**
- 预计完成时间：约 5/24 18:30（UTC+8）

GPU 3 上的 ckpt6100 test eval（PID 272025）不受影响，继续运行。GPU 1 空闲。

---
