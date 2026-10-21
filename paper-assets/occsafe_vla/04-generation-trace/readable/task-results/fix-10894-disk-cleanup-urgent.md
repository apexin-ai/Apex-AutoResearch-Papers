# fix 10894 disk cleanup urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_10894-disk-cleanup-urgent_20260527T073428_result.json`
- **Structured JSON:** [`7574dfc86a290d5123b7.json`](../../sessions/75/7574dfc86a290d5123b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果汇总：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 磁盘使用 | 250G/250G (100%) | 201G/250G (81%) |
| 可用空间 | 1.7MB | **50GB** |
| 释放空间 | — | **~49GB** |

**删除内容：**
- `full_occ_ln_v2_s0d` outputs + checkpoints
- `detach_ln_v2_s0c_r2` outputs
- `detach_ln_v2_s0c` checkpoints（损坏）
- `reverse_cutoff_s2_v2` 40000_chkpt（中间 checkpoint）

**存活实验状态：**
- `full_occ_ln_v2_s1c` (cuda:0, seed=43) — 运行中，已有 10000 + 20000 checkpoint
- `full_occ_ln_v2_s2` (cuda:1, seed=44) — 运行中，已有 10000 + 20000 checkpoint

两个实验各还需保存 30000/40000/50000 三个 checkpoint，每个约 7.5G，共需 ~45G。当前 50G 可用空间足够支撑到训练结束。

---
