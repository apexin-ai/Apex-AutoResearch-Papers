# diagnose 10894 processes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_processes_20260525T172721_result.json`
- **Structured JSON:** [`22717e18d7c4deb39071.json`](../../sessions/22/22717e18d7c4deb39071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10894 进程诊断

**根因：服务器被重启**（PID 1 = boot.sh 启动于 01:18，所有训练 PID 不存在，4 张 GPU 全部空闲 0%/0MiB）。

| exp_id | pid | 存活? | 最后step | 状态判断 | checkpoint |
|--------|-----|-------|---------|---------|------------|
| mvp_occ_s3 | 256611 | ❌ | ~20423/50005 (41%) | 服务器重启被杀 | 10k, 20k merged chkpt ✅ |
| cutoff_45k_s2 | 74225 | ❌ | ~26480/50005 (53%) | 服务器重启被杀 | 10k, 20k merged chkpt ✅ |
| full_occ_ln_s3 | 256695 | ❌ | ~20398/50005 (41%) | 服务器重启被杀 | 10k, 20k merged chkpt ✅ |
| ablation_occ_detach_s3 | 257041 | ❌ | ~20376/50005 (41%) | 服务器重启被杀 | 10k, 20k merged chkpt ✅ |

**关键发现：**

- **4 个实验全部非正常完成**，均未到达 step 50005，是被服务器重启中断的
- **mvp_occ_s3** 不是正常完成后被误判 — 它确实在 step ~20423 处被杀，只完成了 41%
- **cutoff_45k_s2** 进度最高（53%，step ~26480），但受 C002 约束不能 --resume，需从头重训
- 每个实验都有 `latest` + `10000_chkpt` + `20000_chkpt` 三个 checkpoint 目录
- 日志中最后一条 AUX 输出均正常（无 OOM/CUDA error），纯粹是进程被外部杀死

---
