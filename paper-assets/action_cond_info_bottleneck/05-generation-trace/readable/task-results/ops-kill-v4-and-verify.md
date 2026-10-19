# ops kill v4 and verify

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-v4-and-verify_20260516T014828_result.json`
- **Structured JSON:** [`0ee62b92dc805c2ab244.json`](../../sessions/0e/0ee62b92dc805c2ab244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**v4 PID 649789**: 已成功 kill (KILL_OK)。Kill 前运行 45:59，命令为 `acib_v4_agg_kl`。

**GPU 释放**:
- GPU 0: 22843/97887 MiB（v4 已释放，剩余进程 PID 675231 6.6GB + PID 682233 16.2GB + PID 508625 2.1GB）
- GPU 1: 2142/97887 MiB（空闲）
- compute-apps 中已无 PID 649789

**v5_div_reg PID 682233**: ✅ 仍存活，运行 18:39，CPU 731%，命令为 `acib_v5_div_reg`，未受影响。

---
