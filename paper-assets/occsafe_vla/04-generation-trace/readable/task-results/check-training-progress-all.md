# check training progress all

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-progress-all_20260527T031345_result.json`
- **Structured JSON:** [`2bf17d99fd57df0b887a.json`](../../sessions/2b/2bf17d99fd57df0b887a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`ps | grep` 被 read_only 模式拦截，但 GPU 利用率和日志活跃增长已足够确认进程状态。

## westd-10894 (4x GPU, 全部 62GB/98GB 使用中)

| 实验 | 当前 step | 进度 | 速率 | 最新 loss (AUX) | 预估剩余 | 进程 |
|------|----------|------|------|-----------------|---------|------|
| **full_occ_ln_v2_s1c** | ~9551/50005 | 19% | 1.08 it/s | occ=0.0118, act=0.1523 (step 9500) | ~10.4h | 存活 |
| **full_occ_ln_v2_s2** | ~9539/50005 | 19% | 1.08 it/s | occ=0.0170, act=0.1138 (step 9500) | ~10.4h | 存活 |
| **detach_ln_v2_s0c** | ~9520/50005 | 19% | 1.08 it/s | occ=0.0100, act=0.1533 (step 9500) | ~10.4h | 存活 |
| **full_occ_ln_v2_s0d** | ~6998/50005 | 14% | 1.08 it/s | (未在 tail 中可见) | ~11.1h | 存活 |

## westd-34685 (4x GPU, 全部 62-63GB/98GB 使用中)

| 实验 | 当前 step | 进度 | 速率 | 最新 loss (AUX) | 预估剩余 | 进程 |
|------|----------|------|------|-----------------|---------|------|
| **detach_ln_v2_s1** (_35) | ~13683/50005 | 27% | 1.09 it/s | (截断区域内) | ~9.3h | 存活 |
| **detach_ln_s4** | ~13744/50005 | 27% | 1.09 it/s | occ=0.0142, act=0.0996 (step 13700) | ~9.2h | 存活 |
| **ablation_occ_detach_s4** | ~10900/50005 | 22% | 1.06 it/s | (刚存 ckpt@10000) | ~10.2h | 存活 |
| **mvp_occ_s4** | ~10886/50005 | 22% | 1.08 it/s | (刚存 ckpt@10000) | ~10.1h | 存活 |

## 关键发现

1. **Registry 标记错误**: full_occ_ln_v2_s1c、full_occ_ln_v2_s2、detach_ln_v2_s0c 的 registry 标记为 DONE，但实际只跑到 19%，仍在活跃训练中。需更正 registry。

2. **DDL 风险评估**: 所有实验预估还需 9-11h。假设当前是 5/27 下午，所有实验应在 5/28 12:00 UTC 前完成。**full_occ_ln_v2_s0d 是最慢的**（14%, 需 ~11h），裕量最小。

3. **Checkpoint 已保存**:
   - `ablation_occ_detach_s4`: `/root/autodl-tmp/checkpoints/ablation_occ_detach_s4/...-10000_chkpt`
   - `mvp_occ_s4`: `/root/autodl-tmp/checkpoints/mvp_occ_s4/...-10000_chkpt`

4. 8 张 GPU 全部满载运行，无异常。

---
