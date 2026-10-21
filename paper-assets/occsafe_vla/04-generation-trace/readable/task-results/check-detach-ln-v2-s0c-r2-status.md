# check detach ln v2 s0c r2 status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_detach-ln-v2-s0c-r2-status_20260527T071137_result.json`
- **Structured JSON:** [`c07c17ffe65b9770ec14.json`](../../sessions/c0/c07c17ffe65b9770ec14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。同时注意到 GPU 3 上的 `full_occ_ln_v2_s0d` 也标记为 RUNNING 但 GPU 3 同样空闲，很可能也崩了（同样的磁盘满问题）。

## 报告

| 项目 | 结果 |
|------|------|
| **状态** | **CRASHED** — 进程已死，GPU 2 空闲 |
| **崩溃原因** | `No space left on device (os error 28)` — 保存 step 20000 checkpoint 时磁盘满 |
| **崩溃时间** | 2026-05-27 14:29 UTC（约 46 分钟前） |
| **训练进度** | ~20000/50005 steps（40%） |
| **有效 checkpoint** | step 10000 (`detach_ln_v2_s0c--10000_chkpt`) |
| **损坏 checkpoint** | step 20000（仅 1/4 model shards，不可用） |
| **磁盘** | `/root/autodl-tmp` **250G/250G, 100% 满** |
| **Registry** | 已更新为 DONE(failed) |

**紧急问题**: 磁盘 100% 满会影响所有使用 `/root/autodl-tmp` 保存 checkpoint 的实验。`full_occ_ln_v2_s0d`（cuda:3）同样 GPU 空闲但 registry 标 RUNNING，大概率也因磁盘满崩溃。需要清理磁盘空间后才能重启这些训练。

---
