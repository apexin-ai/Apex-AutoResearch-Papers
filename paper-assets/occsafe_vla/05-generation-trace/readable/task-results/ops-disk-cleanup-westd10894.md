# ops disk cleanup westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-westd10894_20260521T190421_result.json`
- **Structured JSON:** [`1aabe4606ace38340be1.json`](../../sessions/1a/1aabe4606ace38340be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总报告：

## 清理结果

### 删除明细
| Step | 目标 | 释放空间 |
|------|------|----------|
| 1 | `vanilla_s2/` | **15G** |
| 2 | `ablation_occ_detach_s0` 10000_chkpt | **15G** |
| 2 | `ablation_random_occ_s0` 10000_chkpt | **15G** |
| 2 | `ablation_occ_detach_s1` 10000_chkpt | **15G** |
| 2 | `ablation_random_occ_s1` 10000_chkpt | **15G** |
| **合计** | | **~75G** |

### 磁盘状态
- **清理前**: 171G used / 80G avail (69%)
- **清理后**: 97G used / 154G avail (39%)

### 4 个 ablation 训练状态（确认未中断）
| 实验 | 当前 step | 状态 |
|------|-----------|------|
| ablation_occ_detach_s0 | ~27066 | 正常训练 |
| ablation_random_occ_s0 | ~27418 | 正常训练 |
| ablation_occ_detach_s1 | ~27104 | 正常训练 |
| ablation_random_occ_s1 | ~27082 | 正常训练 |

每个 ablation 保留了 20000_chkpt 和当前训练目录（含 latest checkpoint）。

### 其他大目录（仅报告）
| 目录 | 大小 |
|------|------|
| `/root/autodl-tmp/runs/` | 15G |
| `/root/autodl-tmp/models/` | 15G |
| `/root/autodl-tmp/libero_datasets/` | 5.9G |
| `/root/autodl-tmp/data/` | 2.0G |

---
