# check server 10894 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-10894-urgent_20260527T040945_result.json`
- **Structured JSON:** [`3a30c02eb530ff9ca127.json`](../../sessions/3a/3a30c02eb530ff9ca127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 状态：**
```
GPU0: 99%, 62203 MiB
GPU1: 49%, 62203 MiB
GPU2: 99%, 62209 MiB
GPU3: 99%, 62203 MiB
```

**4 个训练进程运行中：**

| 实验 | GPU | 进度 | 速度 | ETA |
|------|-----|------|------|-----|
| full_occ_ln_v2_s1c (seed43) | cuda:0 | 12911/50005 (26%) | ~1.08 it/s | ~9.5h |
| full_occ_ln_v2_s2 (seed44) | cuda:1 | 12900/50005 (26%) | ~1.08 it/s | ~9.5h |
| full_occ_ln_v2_s0d (seed42) | cuda:3 | 10358/50005 (21%) | ~1.08 it/s | ~10.2h |
| detach_ln_v2_s0c (seed42) | cuda:2 | 12883/50005 (26%) | ~1.08 it/s | ~9.5h |

**Checkpoints：** `/root/occsafe_vla/checkpoints/` 不存在，checkpoints 在 `/root/autodl-tmp/checkpoints/` 下（暂无 checkpoint_50000.pt，均未到 50k）。

**关键指标（最近 AUX log）：**
- full_occ_ln_v2_s1c step=12900: occ_loss=0.0117, action_loss=0.1377
- full_occ_ln_v2_s0d step=10300: occ_loss=0.0143, action_loss=0.1167

---
