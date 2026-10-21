# check training progress eta

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-progress-eta_20260527T044611_result.json`
- **Structured JSON:** [`d295c056b9473d0cf0db.json`](../../sessions/d2/d295c056b9473d0cf0db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary:

**采样时间: 2026-05-27 ~04:49 UTC**

### westd-34685 (4 GPU 全占用)

| 实验 | GPU | Step | Total | 速度 | 剩余时间 | 预计完成 (UTC) |
|------|-----|------|-------|------|----------|---------------|
| `detach_ln_v2_s1` | 0 | 19,455 | 50,005 | 1.07 it/s | ~7h57m | **~12:46** |
| `detach_ln_s4` | 1 | 19,512 | 50,005 | 1.07 it/s | ~7h53m | **~12:42** |
| `ablation_occ_detach_s4` | 2 | 16,653 | 50,005 | 1.07 it/s | ~8h38m | **~13:27** |
| `mvp_occ_s4` | 3 | 16,658 | 50,005 | 1.08 it/s | ~8h35m | **~13:24** |
| `cutoff_25k_s1_v2` | - | 50,005 | 50,005 | - | - | **DONE** |

34685 最晚完成: **~13:27 UTC**

### westd-10894 (4 GPU 全占用)

| 实验 | GPU | Step | Total | 速度 | 剩余时间 | 预计完成 (UTC) |
|------|-----|------|-------|------|----------|---------------|
| `full_occ_ln_v2_s1c` | 0 | 15,112 | 50,005 | 1.07 it/s | ~9h04m | **~13:53** |
| `full_occ_ln_v2_s2` | 1 | 15,081 | 50,005 | 1.07 it/s | ~9h05m | **~13:54** |
| `detach_ln_v2_s0c` | 2 | 15,081 | 50,005 | 1.08 it/s | ~8h59m | **~13:48** |
| `full_occ_ln_v2_s0d` | 3 | 12,547 | 50,005 | 1.07 it/s | ~9h44m | **~14:33** |

10894 最晚完成: **~14:33 UTC**

### 对 Reviewer 预期的修正

Reviewer 预期 34685 ~20:40 UTC、10894 ~22:30 UTC — **实际远早于此**。所有 8 个实验预计在 **May 27 ~14:33 UTC** (北京时间 22:33) 前全部完成，距 DDL (May 28 12:00 UTC) 还剩 **~21.5 小时**。`cutoff_25k_s1_v2` 已经跑完。

---
