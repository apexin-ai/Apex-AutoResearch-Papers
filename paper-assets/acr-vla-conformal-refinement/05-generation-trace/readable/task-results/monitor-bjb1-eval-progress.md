# monitor bjb1 eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-eval-progress_20260514T181921_result.json`
- **Structured JSON:** [`4f1d27c7934e8eb5e018.json`](../../sessions/4f/4f1d27c7934e8eb5e018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 路 Eval 状态汇总

### 进程存活
全部 4 个进程存活：`197057, 197803, 231421, 232815`

| PID | Eval | 运行时间 |
|-----|------|---------|
| 197057 | eval-acr-spatial-v3 | 6h 02m |
| 197803 | eval-acr-object-v3 | 6h 02m |
| 231421 | eval-argmin-only-spatial | 31m |
| 232815 | eval-tiny-correction-spatial | 31m |

### Eval 进度

**eval-acr-spatial-v3** — 4/10 tasks 完成，正在跑 task 5
| Task | Success Rate |
|------|-------------|
| pick_up_bowl_between_plate_and_ramekin | 10% (1/10) |
| pick_up_bowl_next_to_ramekin | 0% (0/10) |
| pick_up_bowl_from_table_center | 0% (0/10) |
| pick_up_bowl_on_cookie_box | 0% (0/10) |
| **累计** | **2.5% (1/40)** |

**eval-acr-object-v3** — 4/10 tasks 完成，正在跑 task 5
| Task | Success Rate |
|------|-------------|
| alphabet_soup → basket | 0% (0/10) |
| cream_cheese → basket | 0% (0/10) |
| salad_dressing → basket | 0% (0/10) |
| bbq_sauce → basket | 0% (0/10) |
| **累计** | **0% (0/40)** |

**eval-argmin-only-spatial** (mode=reconvla) — 10 tasks 已加载，**0 个 rollout 输出**，31 分钟无进度日志。进程存活且 GPU 有占用，可能在跑第一个 task 的 rollout。

**eval-tiny-correction-spatial** (max_correction_norm=0.05) — Task 1 进行中
- rollout 5/10，success 4/5（当前 80%）

### GPU 利用率

| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| 0 | RTX 4090 | 24% | 21888 / 24564 MiB (89%) |
| 1 | RTX 4090 | 99% | 2878 / 24564 MiB |
| 2 | RTX 4090 | 99% | 2914 / 24564 MiB |
| 3 | RTX 4090 | 20% | 1459 / 24564 MiB |

GPU 0 显存接近满载（6 个 python 进程共享），GPU 1/2 计算利用率 99%。

### 磁盘
数据盘 `/root/autodl-tmp/`: **137GB 可用**（250GB 中已用 114GB，46%）

### 值得注意
- acr-spatial-v3 和 acr-object-v3 跑了 6 小时才完成 4/10 tasks，按此速率预计还需 ~9 小时
- argmin-only-spatial 31 分钟无 rollout 日志，建议稍后复查是否卡住
- tiny-correction-spatial 第一个 task 表现很好（4/5 success），但样本量太小待观察

---
