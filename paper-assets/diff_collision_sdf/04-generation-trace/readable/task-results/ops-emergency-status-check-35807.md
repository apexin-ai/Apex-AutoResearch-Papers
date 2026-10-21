# ops emergency status check 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_status_check_35807_20260523T135001_result.json`
- **Structured JSON:** [`d68475796e2bab8a3069.json`](../../sessions/d6/d68475796e2bab8a3069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807 状态

### 训练进程
| 实验 | PID | GPU | 存活 | 当前 step | 进度 | loss | 异常 |
|------|-----|-----|------|----------|------|------|------|
| s1_l005 | 349005 | cuda:0 | ✓ | 11710/30000 | 39% | 0.0122 | 无 |
| s1_l01 | 349007 | cuda:1 | ✓ | 11705/30000 | 39% | 0.0200 | 无 |
| s2_l005 | 349009 | cuda:2 | ✓ | 11686/30000 | 39% | 0.0153 | 无 |
| s2_l01 | 349011 | cuda:3 | ✓ | 11680/30000 | 39% | 0.0126 | 无 |

**s1_l005 (PID 349005) 正常运行**，进度甚至略领先其它 3 路。overview 只显示 3 路 running 应为监控侧误报。

### Checkpoint
| 实验 | 最新 ckpt | 时间 |
|------|----------|------|
| s1_l005 | step 10000 | May 23 19:38 |
| s1_l01 | step 10000 | May 23 19:38 |
| s2_l005 | step 10000 | May 23 19:39 |
| s2_l01 | step 10000 | May 23 19:40 |

### GPU
| GPU | 型号 | 显存占用 | 温度 | 功耗 | 利用率 |
|-----|------|---------|------|------|--------|
| 0 | RTX PRO 6000 | 27036/97887 MiB | 69°C | 474/600W | 100% |
| 1 | RTX PRO 6000 | 27036/97887 MiB | 62°C | 405/600W | 63% |
| 2 | RTX PRO 6000 | 27036/97887 MiB | 68°C | 459/600W | 100% |
| 3 | RTX PRO 6000 | 27036/97887 MiB | 68°C | 470/600W | 100% |

### 磁盘
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / | 30G | 21G | 9.3G | 70% |
| /root/autodl-tmp | 350G | 126G | 225G | 36% |

**结论：4 路训练全部正常，s1_l005 无异常。ETA 约 23-24 小时完成剩余 61%。**

---
