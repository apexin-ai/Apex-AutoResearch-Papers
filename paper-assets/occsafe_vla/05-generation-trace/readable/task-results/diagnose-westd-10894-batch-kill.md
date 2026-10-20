# diagnose westd 10894 batch kill

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-10894-batch-kill_20260521T045347_result.json`
- **Structured JSON:** [`db378cb28b001d783899.json`](../../sessions/db/db378cb28b001d783899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_westd10894_batch_kill.md`。

**根因**: 平台级外部 SIGTERM — 4 个进程在 17ms 内同时被杀（12:52:12 UTC+8），非 OOM、非重启、非磁盘满、非手动 kill。最可能是 SeetaCloud 平台维护/资源调度触发的容器级信号广播。

**各实验状态**:
- `ablation_occ_detach_s0`: 跑到 step ~4006，有 step 2500 checkpoint，可 resume
- `ablation_random_occ_s0`: 跑到 step ~3993，有 step 2500 checkpoint，可 resume
- `ablation_occ_detach_s1`: 跑到 step ~1546，无 checkpoint，需从头重启
- `ablation_random_occ_s1`: 跑到 step ~1545，无 checkpoint，需从头重启

**服务器当前可用**：4× RTX PRO 6000 Black 全部空闲，磁盘充足，可立即重启实验。

---
