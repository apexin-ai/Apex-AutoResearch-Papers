# check 10894 disk capacity for s4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_10894-disk-capacity-for-s4_20260527T090440_result.json`
- **Structured JSON:** [`8ad81a7e10db83eb5e32.json`](../../sessions/8a/8ad81a7e10db83eb5e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 当前进度与 checkpoint 占用

| 实验 | GPU | 当前 Step | 总 Steps | 速度 | Checkpoints | 占用 |
|---|---|---|---|---|---|---|
| full_occ_ln_v2_s1c (r2) | cuda:0 | ~29,894 | 50,005 | ~1.05 it/s | 10000, 20000 | 30G |
| full_occ_ln_v2_s2 (r2) | cuda:1 | ~29,971 | 50,005 | ~1.08 it/s | 10000, 20000 | 30G |
| detach_ln_v2_s0c_r3 | cuda:2 | ~1,330 | 50,005 | ~1.07 it/s | 无 | 0G |

### 2. 峰值磁盘推算（keep=3）

| 实验 | 当前占用 | 峰值占用 | 增量 |
|---|---|---|---|
| s1c_r2 | 30G | 45G（step 30000 后） | +15G |
| s2_r2 | 30G | 45G（step 30000 后） | +15G |
| s0c_r3 | 0G | 45G（step 30000 时） | +45G |
| **s4（新）** | 0G | 45G（step 30000 时） | +45G |
| **合计增量** | | | **+120G** |

当前可用空间：**95G**，缺口 **25G**。

### 3. 启动 full_occ_ln_s4 是否安全

**否。** 4 个实验同时到达 3-checkpoint 峰值时需要额外 120G，当前只有 95G 可用，会导致磁盘满。

### 4. 替代方案

**方案 A — 清理已完成实验 checkpoint 腾出空间：**

服务器上有 6 个已完成训练（含 50000_chkpt）的实验：

| 实验 | 占用 |
|---|---|
| ablation_occ_detach_s3_v2 | 15G |
| cutoff_15k_s1 | 463M |
| detach_ln_s3 | 15G |
| full_occ_ln_s3_v2 | 15G |
| mvp_occ_s3_v2 | 15G |
| vanilla_v2_s1 | 15G |

清理其中任意 2 个（≥30G），即可安全启动 s4。

**方案 B — 用 cuda:3 跑 eval：**

上述 6 个已完成实验均可做 50-rollout eval（~50 min/个，磁盘写入极小）。如果其中有未 eval 的，可以立刻利用 cuda:3。

**方案 C — 等 s1c/s2 完成再启动 s4：**

s1c/s2 均还需 ~20,100 步，预计 ~5.3h 后完成（约 UTC 13:40）。完成后清理其 checkpoint 可释放 90G。s4 训练需 ~13h，仍能在 deadline（May 28 12:00 UTC）前完成。

---
