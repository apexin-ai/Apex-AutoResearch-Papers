# eval occ s1 47500 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_occ-s1-47500-eval_20260521T143250_result.json`
- **Structured JSON:** [`9754984812f0521fb291.json`](../../sessions/97/9754984812f0521fb291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

47500_chkpt 不存在。occ_s1 可用的 checkpoint 为：

- 17500_chkpt
- 30000_chkpt
- 35000_chkpt
- 40000_chkpt
- **45000_chkpt**
- **50000_chkpt**
- 最终 checkpoint（无后缀，应该也是 50000）

没有 47500 步的 checkpoint。最接近的是 45000 和 50000。

要用哪个？如果 s0/s2 是在 47500 eval 的，s1 这里要 apple-to-apple 对比可能需要确认一下步数对齐的问题。

---
