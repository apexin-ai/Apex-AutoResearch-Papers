# status threshold q07 exit check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_threshold-q07-exit-check_20260516T191551_result.json`
- **Structured JSON:** [`6f76107cca30de0fb630.json`](../../sessions/6f/6f76107cca30de0fb630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**状态：失败（第 3 次）**

| 项目 | 结果 |
|------|------|
| 进程 355121 | 已退出 |
| step_metrics 最后 step | 5999（无进展） |
| final/ 目录 | 不存在 |
| eval 结果 | 不存在 |
| 失败原因 | `ValueError: Your setup doesn't support bf16/gpu` |
| 根因 | 恢复脚本启动时 4x GPU 全被其他进程占满，CUDA 不可用 |

**Checkpoint-5500 完好**，只剩 604 steps（5500→6104）。等 GPU 释放后可再次恢复。

**已完成**：
- Registry 更新：conclusion=failed，notes 记录原因
- Cron 已不存在（之前已被清除）

---
