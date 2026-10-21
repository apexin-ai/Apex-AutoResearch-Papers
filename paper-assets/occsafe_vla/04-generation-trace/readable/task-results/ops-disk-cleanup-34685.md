# ops disk cleanup 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-34685_20260526T085806_result.json`
- **Structured JSON:** [`2e337ac8267ba48a2a62.json`](../../sessions/2e/2e337ac8267ba48a2a62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 汇总

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| `/dev/md127` 已用 | 246G (71%) | 142G (41%) |
| 可用空间 | 105G | 209G |
| **释放空间** | | **104G** |

### 删除明细

| 删除项 | 释放 |
|--------|------|
| `cutoff_45k_s1_v3/` (整目录，失败实验) | ~30G |
| `reverse_cutoff_s2_v3/` (整目录，失败实验) | ~30G |
| `cutoff_15k_s2/`, `cutoff_45k_s1/`, `cutoff_45k_s1_v2/` (空目录) | ~0 |
| `detach_bn_v2_s0/` 40000_chkpt | ~15G |
| `detach_bn_v2_s1/` 40000_chkpt | ~15G |
| `detach_bn_v2_s2/` 40000_chkpt | ~15G |

### 保留的 checkpoint

- `detach_bn_v2_s0/s1/s2`: latest + 50000_chkpt (各15G)
- `full_occ_retrain_s0`: latest + 50000_chkpt (15G)
- `vanilla_retrain_s0`: latest + 50000_chkpt (15G)
- `cutoff_15k_s1`: latest + 50000_chkpt (15G)
- 4个运行中实验目录未触碰

---
