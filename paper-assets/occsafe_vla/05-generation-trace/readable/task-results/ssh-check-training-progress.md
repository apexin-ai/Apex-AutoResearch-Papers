# ssh check training progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-training-progress_20260527T010000_result.json`
- **Structured JSON:** [`23b0579189c53b66d160.json`](../../sessions/23/23b0579189c53b66d160.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部正常工作，4 个 PID 均存活。

```
exp_id                | GPU    | step/50005    | occ_loss | action_loss | tqdm剩余     | 速度
─────────────────────────────────────────────────────────────────────────────────────────────
detach_ln_v2_s1       | cuda:0 |  5418/50005 (11%) | 0.0129  | 0.1367     | ~11h19m     | 1.09 it/s
detach_ln_s4          | cuda:1 |  5500/50005 (11%) | 0.0118  | 0.1582     | ~11h22m     | 1.09 it/s
ablation_occ_detach_s4| cuda:2 |  2643/50005 ( 5%) | 0.0183  | 0.1445     | ~12h02m     | 1.09 it/s
mvp_occ_s4            | cuda:3 |  2634/50005 ( 5%) | 0.0119  | 0.1689     | ~12h02m     | 1.09 it/s
```

**关键信息**:
- GPU 型号: NVIDIA RTX PRO 6000 Blackwell (96GB), 利用率 48%/99%/99%/96%
- detach_ln_v2_s1 的 log 文件名是 `detach_ln_v2_s1.log`（非 `_35`）
- cuda:0 利用率偏低 (48%)，但训练速度与其他 GPU 一致，可能是采样时刻波动
- 4 个实验预计还需 **11-12 小时**完成。DDL 是 05-28 12:00 UTC，时间较紧——如果当前已过 05-27 00:00 UTC，需确保不中断

---
