# ops cleanup 34685 exec

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_34685_exec_20260529T103214_result.json`
- **Structured JSON:** [`0bcfeb0abc736880ad68.json`](../../sessions/0b/0bcfeb0abc736880ad68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理汇报

### 每步释放量

| # | 目录 | 操作 | 释放 |
|---|------|------|------|
| 1 | `full_occ_bn_v2_s2/` | DEL-ALL | ~44G |
| 2 | `full_occ_bn_v2_s2_r2/` | DEL-ALL | ~15G |
| 3-4 | `full_occ_bn_v2_s2_r3/`, `r4/` | DEL-ALL | ~0 (空目录) |
| 5 | `detach_bn_v2_s3/`, `full_occ_bn_v2_s4/`, `full_occ_ln_v2_s0c/`, `vanilla_v2_s3/` | DEL-ALL | ~0 (空目录) |
| 6 | `detach_ln_v2_s2/` | DEL-MID (保留 50000_chkpt) | ~45G |
| 7 | `detach_ln_v2_s3/` | DEL-MID (保留 50000_chkpt) | ~29G |
| 8 | `full_occ_ln_v2_s3/` | DEL-MID (保留 50000_chkpt) | ~16G |
| 9 | `vanilla_object_s0/` | DEL-MID (保留 25000_chkpt) | ~30G |

### 总结

- **总释放量**: ~179G（316G → 137G）
- **最终磁盘**: 137G/350G used (40%)，可用 214G
- **`full_occ_bn_v2_s2_r5/` 完好**: 包含 base + 20000/30000/40000 三个 checkpoint，未受影响
- 剩余目录：5 个实验目录（含 r5）+ 6 个 log 文件

---
