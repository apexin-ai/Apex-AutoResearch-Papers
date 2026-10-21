# code ctrl contam pilot deploy

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ctrl-contam-pilot-deploy_20260520T144815_result.json`
- **Structured JSON:** [`75593e4000c16bcec806.json`](../../sessions/75/75593e4000c16bcec806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型下载仍在进行中，4个 shard 并行下载：

| Shard | Progress | Speed | ETA |
|-------|----------|-------|-----|
| 1/4 (3.67G) | 41% (1.50G) | 838 KB/s | ~46 min |
| 2/4 (3.60G) | 41% (1.47G) | 806 KB/s | ~47 min |
| 3/4 (3.60G) | 41% (1.49G) | 869 KB/s | ~43 min |
| 4/4 (3.31G) | 48% (1.59G) | 933 KB/s | ~33 min |

瓶颈是 shard 2，预计还需约 **45-50 分钟**完成。下载完成后我会继续执行 dry-run → 提交训练。

需要我定期轮询状态，还是你下载完成后再叫我继续？

---
