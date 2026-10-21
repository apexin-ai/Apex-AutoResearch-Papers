# audit vtc health check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_vtc-health-check_20260521T152701_result.json`
- **Structured JSON:** [`255f7927d0f49ce1d703.json`](../../sessions/25/255f7927d0f49ce1d703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有三个训练进程都在正常运行。nvidia-smi 的 0% utilization 只是采样瞬间。

## westd-41074
- **GPU2 (M96)**: 存活 | step=63000/100000 | 日志最后更新=23:27:38 | sps=0.5 | loss=2.97
- **GPU3 (M64v6)**: 存活 | step=12350/100000 | 日志最后更新=23:26:50 | sps=0.6 | loss=2.98

## westd-27271
- **GPU1 (M32)**: 存活 | step=63550/100000 | 日志最后更新=23:26:58 | sps=0.5 | loss=2.37

三个进程日志均在 1 分钟内有更新，training step 持续推进，无挂起迹象。GPU util 0% 是 nvidia-smi 采样时恰好在 data loading / step 间隙。

---
