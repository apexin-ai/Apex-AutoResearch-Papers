# fix 10894 disk cleanup restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_10894_disk_cleanup_restart_20260528T014157_result.json`
- **Structured JSON:** [`773570968450b663a58a.json`](../../sessions/77/773570968450b663a58a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕，汇总报告：

---

## 10894 磁盘清理 + 状态报告

### 1. 磁盘清理

| | 容量 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| **清理前** | 250G | 250G | 400K | **100%** |
| **清理后** | 250G | 102G | 149G | **41%** |

**释放约 148G。** 删除了以下目录：

| 目录 | 大小 |
|---|---|
| detach_ln_v2_s0c_r3 | 30G |
| full_occ_ln_s4 | 30G |
| full_occ_ln_v2_s1c | 30G |
| full_occ_ln_v2_s2 | 30G |
| detach_ln_s3 | 15G |
| vanilla_v2_s1 | 15G |
| cutoff_15k_s1 | 463M |
| 11个空/4K目录 | ~0 |

剩余 checkpoint 目录仅 4 个：vanilla_object_s1（运行中）、detach_ln_v2_s4（运行中）、full_occ_bn_object_s0（崩溃待重启）、detach_bn_object_s0（崩溃待重启）。

### 2. 存活实验确认

| 实验 | PID | GPU | 运行时间 | 状态 |
|---|---|---|---|---|
| vanilla_object_s1 | 798980 | cuda:0 (73%, 63G/96G) | 7h51m | **ALIVE** |
| detach_ln_v2_s4 | 822480 | cuda:1 (49%, 62G/96G) | 3h03m | **ALIVE** |

GPU 2-3 空闲。

### 3. 崩溃实验重启评估

- 磁盘可用：**149G >= 60G** ✅
- `full_occ_bn_object_s0/...5000_chkpt` ✅ 存在
- `detach_bn_object_s0/...5000_chkpt` ✅ 存在
- **可以重启。** GPU 2-3 空闲，磁盘充足。

### 4. 34685 磁盘状况

| 容量 | 已用 | 可用 | 使用率 |
|---|---|---|---|
| 350G | 300G | 51G | 86% |

Checkpoint 分布（按大小）：

| 目录 | 大小 |
|---|---|
| detach_ln_v2_s2 | 30G |
| detach_ln_v2_s3 | 30G |
| full_occ_ln_v2_s3 | 30G |
| vanilla_object_s0 | 30G |
| cutoff_25k_s1_v2 | 15G |
| detach_bn_v2_s0 | 15G |
| detach_bn_v2_s1 | 15G |
| detach_bn_v2_s2 | 15G |
| detach_ln_s3 | 15G |
| full_occ_bn_v2_s1 | 15G |
| mvp_occ_s4 | 15G |
| vanilla_v2_s1 | 15G |
| vanilla_v2_s2 | 15G |
| **合计** | **~255G** |

34685 如需更多空间，有大量已完成实验 checkpoint 可清理。

---
