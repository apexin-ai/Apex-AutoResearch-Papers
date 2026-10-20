# infra training progress panorama

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_training_progress_panorama_20260520T215439_result.json`
- **Structured JSON:** [`db36a381c634eab644cf.json`](../../sessions/db/db36a381c634eab644cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

```
| exp_id         | server      | PID    | current_step | total_steps | speed (it/s) | ETA (UTC)        |
|----------------|-------------|--------|--------------|-------------|--------------|------------------|
| mvp_vanilla_s0 | westd-10894 | 100203 | 46993        | 50005       | 1.11         | 2026-05-20 02:45 |
| mvp_vanilla_s1 | westd-10894 | 97847  | 46658        | 50005       | 1.09         | 2026-05-20 02:51 |
| mvp_vanilla_s2 | westd-10894 | 225562 | 39773        | 50005       | 1.09         | 2026-05-20 04:37 |
| mvp_occ_s0     | westd-34685 | 27667  | 20208        | 50005       | 1.05         | 2026-05-20 10:20 |
| mvp_occ_s1     | westd-34685 | 28827  | 20155        | 50005       | 1.07         | 2026-05-20 10:06 |
| mvp_occ_s2     | westd-34685 | 29970  | 20148        | 50005       | 1.07         | 2026-05-20 10:10 |
```

**备注：**
- 所有 6 个进程存活，GPU 利用率正常（westd-10894 GPU 0/1/2: 90%/45%/97%；westd-34685 GPU 0/1/2: 82%/38%/53%）
- vanilla_s2 的 step 计算：tqdm 显示 4773/50005（从 0 开始），实际 step = 35000 + 4773 = **39773**
- vanilla_s0/s1 预计 ~45-51 分钟完成；vanilla_s2 预计 ~2.5h 完成
- occ_s0/s1/s2 均刚过 20000 checkpoint，预计还需 ~8h，occ 因额外 occ_head 计算略慢于 vanilla（1.05 vs 1.09 it/s）
- occ 实验打印了 OCC loss：occ_s0 `occ_loss=0.0098, action_loss=0.0854`；occ_s1 `occ_loss=0.0109, action_loss=0.1016`；occ_s2 `occ_loss=0.0079, action_loss=0.1079`
- 当前 UTC 时间估算 ≈ 2026-05-20 02:00（基于进程 etime 反推）

---
