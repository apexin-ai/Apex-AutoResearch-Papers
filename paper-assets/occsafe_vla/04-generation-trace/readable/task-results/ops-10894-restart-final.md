# ops 10894 restart final

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-restart-final_20260526T182405_result.json`
- **Structured JSON:** [`60114c18ae9484e95b22.json`](../../sessions/60/60114c18ae9484e95b22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

reverse_cutoff_s2_v2 已保存 30000 步 checkpoint，GPU 0 仍在运行（99% 利用率），正常。tmux capture 为空可能是因为训练输出重定向到了日志或进度条覆盖了 buffer。

---

## 汇报

### 1. 进程 PID
| 实验 | GPU | PID |
|------|-----|-----|
| reverse_cutoff_s2_v2 | cuda:0 | 170698 |
| full_occ_ln_v2_s0 | cuda:1 | 390852 |
| full_occ_ln_v2_s1 | cuda:2 | 391060 |
| detach_ln_v2_s0 | cuda:3 | 391402 |

### 2. GPU 利用率
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 62203 MiB | 99% |
| 1 | 62203 MiB | 99% |
| 2 | 63013 MiB | 99% |
| 3 | 62203 MiB | 99% |

### 3. 训练进度（启动 ~2.5 分钟后）
| 实验 | 当前 step | 速度 | occ_loss | action_loss |
|------|----------|------|----------|-------------|
| full_occ_ln_v2_s0 | ~147/50005 | 1.07 it/s | 0.0369 | 0.4648 |
| full_occ_ln_v2_s1 | ~145/50005 | 1.06 it/s | 0.0340 | 0.3828 |
| detach_ln_v2_s0 | ~143/50005 | 1.07 it/s | 0.0357 | 0.3672 |

预计训练时长: 50005 steps / 1.07 it/s ≈ **13 小时**，约在 5/27 15:30 UTC 完成，在 deadline (5/28 12:00 UTC) 之前。

### 4. tmux ls
```
detach_ln_v2_s0: 1 windows (created Wed May 27 02:25:05 2026)
full_occ_ln_v2_s0: 1 windows (created Wed May 27 02:24:58 2026)
full_occ_ln_v2_s1: 1 windows (created Wed May 27 02:25:02 2026)
reverse_cutoff_s2_v2: 1 windows (created Tue May 26 17:02:24 2026)
```

### 5. reverse_cutoff_s2_v2 状态
正常运行中。GPU 0 占用 62203 MiB / 99%。已保存 30000 步 checkpoint（01:46 UTC），当前应在 30000+ 步继续训练。

### 6. 磁盘
```
/dev/md0  250G  127G  124G  51%  /root/autodl-tmp
```
124GB 可用，充足。

---
