# fix kill stale tmux 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_stale_tmux_10894_20260525T174128_result.json`
- **Structured JSON:** [`e20dfa1167a940606115.json`](../../sessions/e2/e20dfa1167a940606115.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**tmux 清理结果：** `mvp_occ_s3_v2` 已 kill。剩余 4 个活跃 session：
- `cutoff_45k_s2_v2` — GPU 0
- `full_occ_bn_v2_s1` — GPU 1
- `full_occ_ln_s3_v2` — GPU 2
- `ablation_occ_detach_s3_v2` — GPU 3

**GPU 状态：**

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 62209 MiB | 43% |
| 1 | 62203 MiB | 99% |
| 2 | 63037 MiB | 99% |
| 3 | 62209 MiB | 99% |

4 张卡全部被占用，各跑一个 finetune 任务，无残留/孤立进程。

---
