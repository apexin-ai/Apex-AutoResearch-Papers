# diagnose gpu audit 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_audit_10894_20260527T174100_result.json`
- **Structured JSON:** [`1ec4fae2958ba45f1ad0.json`](../../sessions/1e/1ec4fae2958ba45f1ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| cuda:0 | 0% | 0/98GB | 空闲 |
| cuda:1 | 0% | 0/98GB | 空闲 |
| cuda:2 | 99% | 62GB/98GB | detach_ln_v2_s0c_r3 (PID 543255) |
| cuda:3 | 99% | 63GB/98GB | full_occ_ln_s4 (PID 553813) |

### 训练进度

| 实验 | 当前 step | 进度 | 速度 | 预计完成 (UTC) |
|------|-----------|------|------|----------------|
| detach_ln_v2_s0c_r3 | 30564/50005 | 61% | ~1.08 it/s | ~07:00 May 28 |
| full_occ_ln_s4 | 28790/50005 | 58% | ~1.08 it/s | ~07:30 May 28 |

- detach_ln_v2_s0c_r3 最近指标 (step 30500): occ_loss=0.0113, action_loss=0.0942
- 两个实验均在 DDL (12:00 UTC May 28) 前完成，无风险

### libero_object 数据拉取

- **31/32 tfrecord 已下载**（每个 77-91MB），总计 2.6GB
- **tfrecord-00018-of-00032 仍是 LFS 指针**（133 bytes），git lfs pull 仍在运行（PID 796437）
- 即将完成

### 磁盘

- `/root/autodl-tmp`: 176GB / 250GB (71%)，剩余 75GB，充足

### 异常

- 无异常。cuda:0/1 空闲待命，等 libero_object 最后 1 个文件下载完即可启动 vanilla_object_s1。

---
