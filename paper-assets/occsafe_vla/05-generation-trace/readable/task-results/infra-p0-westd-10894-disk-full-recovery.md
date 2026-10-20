# infra P0 westd 10894 disk full recovery

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0-westd-10894-disk-full-recovery_20260521T080318_result.json`
- **Structured JSON:** [`1b8ea14ff2bb0caaaa8b.json`](../../sessions/1b/1b8ea14ff2bb0caaaa8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

速度仍在 warmup 阶段（前 10 步不稳定，JIT 编译 + 数据管道预热）。4 个实验都在运行，20 个进程活跃。

---

## 产出汇总

| 项目 | 结果 |
|------|------|
| **磁盘诊断** | 250G/250G = 100% 满。checkpoints 214G, runs 15G, models 15G |
| **清理释放** | ~49G（vanilla 35000_chkpt ×3 = 45G + 损坏的 s1 5000_chkpt ×2 = 4G）→ 磁盘 81%, 50G 可用 |
| **Rotation 脚本** | PID 504685，每 10 分钟轮转，保护运行中实验的 vla_path |
| **s0 两组存活** | ablation_occ_detach_s0 (cuda:0, 63GB) + ablation_random_occ_s0 (cuda:1, 62GB) 正常运行 |
| **s1 重启** | 首次尝试 5000_chkpt 失败（磁盘满导致 checkpoint 损坏，缺 model shard），回退到 2500_chkpt 成功 |
| **ablation_occ_detach_s1** | PID 505677, cuda:2, 62GB, resume_step=2500, 训练中 |
| **ablation_random_occ_s1** | PID 505824, cuda:3, 61GB, resume_step=2500, 训练中 |
| **Cron 监控** | 两组 s1 已注册，120s 轮询 |

**注意**：s1 两组因损坏的 5000_chkpt 损失了 2500 步（从 step 2500 而非 5000 恢复），预计多 ~40 分钟训练时间。速度待 warmup 后稳定到 ~1 it/s。

---
