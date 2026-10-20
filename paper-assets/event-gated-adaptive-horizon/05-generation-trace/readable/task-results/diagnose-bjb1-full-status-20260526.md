# diagnose bjb1 full status 20260526

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1_full_status_20260526_20260525T235122_result.json`
- **Structured JSON:** [`0adfd6ab7d0d0358186f.json`](../../sessions/0a/0adfd6ab7d0d0358186f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-45299 GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|----------|----------|------|
| 0 | RTX PRO 6000 Blackwell | 3801 / 97887 MiB (3.9%) | 27% | PID 313538 (exp_092, 3257M) + PID 313815 (515M) |
| 1 | RTX PRO 6000 Blackwell | 2751 / 97887 MiB (2.8%) | 27% | PID 313815 (exp_093, 2742M) |

## 实验进度
| exp_id | PID | Step/Total | 进度 | eval_return | FPS | gate_dt |
|--------|-----|-----------|------|-------------|-----|---------|
| exp_092_cheetah_no_dt_emb_s1 | 313538 (cuda:0) | 36K / 500K | 7.2% | 59.70 @35K | 9.82 | 100% dt=2 |
| exp_093_cheetah_no_dt_emb_s2 | 313815 (cuda:1) | 36K / 500K | 7.2% | 73.53 @35K | 9.80 | 100% dt=2 |

两个实验约 1 小时前启动，eval_return 从 ~99 (exp_092@25K) 和 ~65 (exp_093@25K) 变化到当前值。gate 完全锁定在 dt=2，entropy=0。

## tmux sessions
```
exp_092_cheetah_no_dt_emb_s1  (created Tue May 26 06:52:49 2026)
exp_093_cheetah_no_dt_emb_s2  (created Tue May 26 06:52:52 2026)
```

## 磁盘
| 挂载点 | 容量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (根分区) | 30G | 17G | 14G | 57% |
| /root/autodl-tmp (数据盘) | 250G | 93G | 158G | 38% |

---
