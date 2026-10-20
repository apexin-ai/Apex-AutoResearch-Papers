# ops training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260521T191236_result.json`
- **Structured JSON:** [`97266b19f7f0705a5d63.json`](../../sessions/97/97266b19f7f0705a5d63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

---

### westd-10894（4 个 ablation）

#### 训练进度

| 实验 | Step | 进度 | Speed | tqdm 剩余 | ETA (UTC) |
|---|---|---|---|---|---|
| ablation_occ_detach_s0 | 27586/50005 | 55% | 1.07 it/s | ~5h49m | May 22 ~01:00 |
| ablation_random_occ_s0 | 27937/50005 | 56% | 1.07 it/s | ~5h42m | May 22 ~00:55 |
| ablation_occ_detach_s1 | 27626/50005 | 55% | 1.07 it/s | ~5h47m | May 22 ~01:00 |
| ablation_random_occ_s1 | 27601/50005 | 55% | 1.07 it/s | ~5h48m | May 22 ~01:01 |

**Loss**: 4 个 ablation 日志中**没有 loss 输出**（grep "loss"/"OCC"/"step=" 均无匹配）。训练脚本仅输出 tqdm 进度条，未打印 loss 值。

#### GPU 利用率

| GPU | 利用率 | 显存 |
|---|---|---|
| 0 | 47% | 62203 / 97887 MiB |
| 1 | 99% | 63037 / 97887 MiB |
| 2 | 50% | 62203 / 97887 MiB |
| 3 | 99% | 62203 / 97887 MiB |

4 卡均在使用，GPU 0/2 利用率偏低（47%/50%），可能是 IO wait。

#### 磁盘
97G / 250G (39%)

#### 20K checkpoint 清理
**4 个实验的 20000_chkpt 均未删除**（仍然存在）。当前 step ~27.5K，未到 30K 触发点，符合预期。

---

### westd-34685（occ_s1_fresh）

#### 训练进度

| 实验 | Step | 进度 | Speed | tqdm 剩余 | ETA (UTC) |
|---|---|---|---|---|---|
| occ_s1_fresh | 16648/50005 | 33% | 1.08 it/s | ~8h35m | May 22 ~03:48 |

**最新 loss** (step 16600): `occ_loss=0.0096, action_loss=0.1172`

已保存 checkpoints: 7500, 10000, 12500, 15000（save_freq=2500）

#### GPU 利用率

| GPU | 利用率 | 显存 |
|---|---|---|
| 0 | 99% | 62203 / 97887 MiB |
| 1 | 0% | 0 MiB |
| 2 | 0% | 0 MiB |
| 3 | 0% | 0 MiB |

cuda:0 在跑，cuda:1-3 空闲，符合预期。

#### 磁盘
113G / 350G (33%)

---
