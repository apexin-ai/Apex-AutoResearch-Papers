# ops 34685 speed check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-speed-check_20260526T111348_result.json`
- **Structured JSON:** [`b0232e42c04e4112f60e.json`](../../sessions/b0/b0232e42c04e4112f60e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总如下：

**CKA 进程状态：已 kill，ps aux 中无 PID 460707，无 cka 相关进程。**

**GPU 利用率：4 卡均 99%（GPU2 为 81%），显存各占用 ~62GB/98GB，正常。**

| GPU | 实验 | 当前步数 | 速度 | 恢复? | 剩余步数 | ETA |
|-----|------|---------|------|-------|---------|-----|
| 0 | vanilla_v2_s1 | 8459/50005 | ~1.09 it/s | **Y** | 41546 | ~10.6h |
| 1 | vanilla_v2_s2 | 8499/50005 | ~1.10 it/s | **Y** | 41506 | ~10.5h |
| 2 | detach_ln_s3 | 8456/50005 | ~1.08 it/s | **Y** | 41549 | ~10.7h |
| 3 | cutoff_25k_s1_v2 | 7067/50005 | ~1.08 it/s | **Y** | 42938 | ~11.0h |

4 个训练速度全部恢复到正常水平（~1.08-1.10 it/s），CKA 进程已确认被 kill。预计所有实验明天早上 5-7 点左右完成。

---
