# infra check ablation status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-ablation-status-10894_20260521T114249_result.json`
- **Structured JSON:** [`7be760fc384c9d147140.json`](../../sessions/7b/7be760fc384c9d147140.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 个 Ablation 实验状态汇总

| 实验 | 实际 PID | GPU | Step | 速度 | tqdm ETA | 预计完成 (UTC) |
|------|---------|-----|------|------|----------|---------------|
| ablation_occ_detach_s0 | 523492 | cuda:0 (99%, 62G/98G) | **2377**/50005 | 1.08 it/s | ~12h14m | ~May 22 08:00 |
| ablation_random_occ_s0 | 522013 | cuda:1 (41%, 63G/98G) | **2758**/50005 | 1.08 it/s | ~12h09m | ~May 22 07:50 |
| ablation_occ_detach_s1 | 523704 | cuda:2 (99%, 62G/98G) | **2375**/50005 | 1.08 it/s | ~12h16m | ~May 22 08:00 |
| ablation_random_occ_s1 | 524055 | cuda:3 (99%, 62G/98G) | **2371**/50005 | 1.08 it/s | ~12h15m | ~May 22 08:00 |

**关键信息：**
- **全部 4 个实验正常运行**，进度 ~5%
- PID 与预期不完全一致（预期的是 bash wrapper PID，实际 python worker PID 不同，但 wrapper 进程存活）
- `ablation_random_occ_s0` 比其他 3 个早启动 7 分钟（18:55 vs 19:02），所以 step 稍领先
- GPU 1 利用率瞬时 41%（其余 99%），可能是采样抖动，不影响训练速度
- **Checkpoint**: 4 个实验目录均只有 run 子目录，尚无编号 checkpoint（step < 10000，save_freq=10000，符合预期）
- **磁盘**: `/root/autodl-tmp/` 52G/250G 已用（21%），空间充足
- **Cron 监控**: 无（无 cron_*.pid 文件）
- **Warning**: `ablation_occ_detach_s0` 和 `ablation_random_occ_s0` 日志中有 occ index missing 的 WARNING（`pick_up_the_black_bowl...` task 无 occ 数据），不影响训练但该 task 的 occ 数据缺失

---
