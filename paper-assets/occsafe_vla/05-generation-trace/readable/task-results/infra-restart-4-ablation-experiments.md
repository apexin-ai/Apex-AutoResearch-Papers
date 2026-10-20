# infra restart 4 ablation experiments

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_restart-4-ablation-experiments_20260521T062404_result.json`
- **Structured JSON:** [`9a4847e803ce9cae9bb0.json`](../../sessions/9a/9a4847e803ce9cae9bb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 实验 | GPU | 内存 | 速度 | 恢复方式 | PID |
|------|-----|------|------|----------|-----|
| ablation_occ_detach_s0 | cuda:0 | 63GB | 1.08 it/s | resume 2500_chkpt | 494161 |
| ablation_random_occ_s0 | cuda:1 | 62GB | 1.07 it/s | resume 2500_chkpt | 494372 |
| ablation_occ_detach_s1 | cuda:2 | 62GB | 1.08 it/s | 从头 | 494649 |
| ablation_random_occ_s1 | cuda:3 | 62GB | 1.08 it/s | 从头 | 494992 |

4 个实验全部在训练，CRON 已注册（120s 间隔），registry notes 已更新。预计 ~13h 完成（约 UTC 19:25，北京时间 5/22 凌晨 3:25）。

---
