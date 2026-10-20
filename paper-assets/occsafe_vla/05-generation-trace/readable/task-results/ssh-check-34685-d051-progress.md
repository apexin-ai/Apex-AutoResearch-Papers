# ssh check 34685 d051 progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_34685_d051_progress_20260525T183656_result.json`
- **Structured JSON:** [`9d7cf6264dd0e857f8b7.json`](../../sessions/9d/9d7cf6264dd0e857f8b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D051 训练进度汇报 (westd-34685)

| exp_id | 当前 step / 50005 | 进度 | 进程 | 速度 | ETA |
|--------|-------------------|------|------|------|-----|
| detach_bn_v2_s0 | ~3552 / 50005 | **7.1%** | alive (57m) | 1.08 it/s | ~+12h → May 26 ~07:00 UTC |
| detach_bn_v2_s1 | ~3591 / 50005 | **7.2%** | alive (58m) | 1.09 it/s | ~+11.8h → May 26 ~07:00 UTC |
| detach_bn_v2_s2 | ~3596 / 50005 | **7.2%** | alive (58m) | 1.08 it/s | ~+12h → May 26 ~07:00 UTC |
| full_occ_bn_v2_s1 | ~2056 / 50005 | **4.1%** | alive (34m) | 1.08 it/s | ~+12.3h → May 26 ~07:00 UTC |

**GPU 使用**：4 卡全部正常工作（62/98 GB 显存占用，GPU 利用率 49-99%）

**Checkpoint**：尚无保存（save_freq=10000，首个 checkpoint 约在 ~2.5h 后产生）

**Loss（最近）**：
- detach_bn_v2_s0 @ step 3500: occ_loss=0.0140, action_loss=0.1797
- full_occ_bn_v2_s1 @ step 2000: occ_loss=0.0199, action_loss=0.2227

**结论**：4 个实验刚启动约 1 小时，进展正常，ETA 符合预期 May 26 ~07:00 UTC。

---
