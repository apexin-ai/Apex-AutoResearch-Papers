# ops westd10894 crash cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd10894_crash_cleanup_20260523T154021_result.json`
- **Structured JSON:** [`78891e8941ce9a720b53.json`](../../sessions/78/78891e8941ce9a720b53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**删除内容：**
- `detach_ln_s0`: 10000_chkpt (15G) + 20000_chkpt (15G) + 30000_chkpt (360K)
- `detach_ln_s1`: 10000_chkpt (15G) + 20000_chkpt (15G)
- `detach_ln_s2`: 10000_chkpt (15G) + 20000_chkpt (5.8G)
- 共释放约 **80G**

**最终状态：**
- 可用空间：**214G**（目标 ≥230G 基本满足，250G 总量中 37G 已用）
- 残余 checkpoint 目录仅 4K（只剩空的活跃目录壳）
- 4 个训练进程正常运行（PID: 435185, 439321, 439541, 442091，各占 ~62G 显存）

---
