# diag westd28034 gpu0

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd28034_gpu0_20260518T134142_result.json`
- **Structured JSON:** [`5388e839a289c9f1efa7.json`](../../sessions/53/5388e839a289c9f1efa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**GPU 0 已自行恢复正常。** 执行 CUDA 计算后，GPU 0 从异常状态（P0 / 100% util / 121W / 无进程）回落到正常空闲状态（P8 / 0% util / 12W）。

| GPU | 状态 | 计算测试 | 显存测试 (2.1GB) |
|-----|------|---------|-----------------|
| 0 | 已恢复正常 (P8, 0%, 12W) | PASSED | PASSED |
| 1 | 正常 | PASSED | — |
| 2 | 正常 | PASSED | — |
| 3 | 正常 | PASSED | — |

**原因分析**：GPU 0 之前可能有进程异常退出（crash/kill），导致 GPU 卡在 P0 高功耗状态但无实际进程。执行新的 CUDA 操作触发了驱动状态重置，GPU 恢复正常。

**结论**：4 张 GPU 全部可用，无需排除 GPU 0。如果此问题反复出现，可考虑 `nvidia-smi -r -i 0` 手动重置 GPU 状态。

---
