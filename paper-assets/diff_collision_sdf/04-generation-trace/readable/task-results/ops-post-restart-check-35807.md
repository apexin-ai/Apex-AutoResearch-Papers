# ops post restart check 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_check_35807_20260524T042544_result.json`
- **Structured JSON:** [`55f69c9625abcee8e74f.json`](../../sessions/55/55f69c9625abcee8e74f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807 状态

### 训练

| 实验 | PID | GPU | 存活 | 最新 ckpt step | 日志当前 step | 进度 | ETA |
|------|-----|-----|------|---------------|--------------|------|-----|
| s1_l005 (seed1, λ_sdf=0.005) | 349005 | cuda:0 | ✅ | 22000 | ~23040 | 77% (23040/30000) | ~9h |
| s1_l01 (seed1, λ_sdf=0.01) | 349007 | cuda:1 | ✅ | 22000 | ~23036 | 77% (23036/30000) | ~9h |
| s2_l005 (seed2, λ_sdf=0.005) | 349009 | cuda:2 | ✅ | 22000 | ~22996 | 77% (22996/30000) | ~9h |
| s2_l01 (seed2, λ_sdf=0.01) | 349011 | cuda:3 | ✅ | 22000 | ~22968 | 77% (22968/30000) | ~9h |

速度 ~4.63s/it，4 个实验全部存活，进度一致。

### GPU

| GPU | 型号 | 显存 | 利用率 | 温度 | 功耗 |
|-----|------|------|--------|------|------|
| 0 | RTX PRO 6000 | 27045/97887 MiB (28%) | 100% | 70°C | 466/600W |
| 1 | RTX PRO 6000 | 27045/97887 MiB (28%) | 100% | 66°C | 474/600W |
| 2 | RTX PRO 6000 | 27045/97887 MiB (28%) | 100% | 69°C | 487/600W |
| 3 | RTX PRO 6000 | 27045/97887 MiB (28%) | 100% | 67°C | 466/600W |

### 磁盘

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` | 350G | 126G | 225G | 36% |
| `/` | 30G | 21G | 9.2G | 70% |

**结论**：服务重启后 4 个训练进程均正常恢复，GPU 满载运行，磁盘充足。预计 ~9 小时后（约今晚 21:30）全部完成 30000 步。

---
