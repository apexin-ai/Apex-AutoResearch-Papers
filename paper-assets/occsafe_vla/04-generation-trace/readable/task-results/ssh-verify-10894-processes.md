# ssh verify 10894 processes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_10894_processes_20260526T120709_result.json`
- **Structured JSON:** [`e1de969ab1c05b867c86.json`](../../sessions/e1/e1de969ab1c05b867c86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 占用（4/4 全满）

| PID | 实验 | 进度 | GPU 显存 | 启动时间 |
|-----|------|------|---------|---------|
| 170698 | **reverse_cutoff_s2_v2** | 11129/50005 (22%), ~10h剩余 | 62194 MiB | 17:02 |
| 341771 | **full_occ_ln_v2_s0** | 126/50005 (0.25%) | 63028 MiB | 20:05 |
| 341987 | **full_occ_ln_v2_s1** | 124/50005 (0.25%) | 62194 MiB | 20:05 |
| 342341 | **detach_ln_v2_s0** | 115/50005 (0.23%) | 62194 MiB | 20:05 |

3 个新实验均在正常训练，速度 ~1.08 it/s。

### 旧 PID 状态

6 个旧 PID (340237, 340452, 340735, 341693, 341843, 342191) 均不在进程列表中 → **全部已死**。当前运行的是重新提交的进程。

### full_occ_ln_s3_v2_eval

**已完成**，EXIT_CODE=0。结果：

- **TSR = 84.2%** | **CAR = 74.0%**
- 结果文件：`/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260526_191143.json`
- 10 个 task 中 T9 最后完成，单 task TSR 从 0.98 到 1.0 不等

### reverse_cutoff_s2_v2

运行中，step 11129/50005 (22%)，已跑约 3h，预计还需 ~10h。

---
