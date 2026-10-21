# check all servers gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-servers-gpu-status_20260525T045002_result.json`
- **Structured JSON:** [`941d0a7909b897c3af57.json`](../../sessions/94/941d0a7909b897c3af57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux ls 被 ssh_read_only 拒绝，但 ps aux 已提供足够信息。汇总如下：

---

## bjb1-18228 (4x RTX 4090)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0 | 2/24564 MiB | 0% |
| cuda:1 | 10844/24564 MiB | 14% |
| cuda:2 | 10805/24564 MiB | 1% |
| cuda:3 | 9883/24564 MiB | 23% |

**进程:**
| PID | GPU | 命令 |
|-----|-----|------|
| 446360 | cuda:1 | evaluate.py --mode vla_only --benchmark spatial --seed 42 |
| 446719 | cuda:2 | evaluate.py --mode vla_only --benchmark goal --seed 42 |
| 114507 | cuda:3 | train_crm.py --precompute --model pi05 --benchmark long --K 10 |

**空闲GPU:** cuda:0
**异常:** cuda:0 CRM训练不在运行（已完成）

---

## cqa1-32758 (6x RTX 4090 D)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0~5 | 全部 0/24564 MiB | 0% |

**进程:** 无
**空闲GPU:** cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
**异常: 预期6个K=2 Spatial实验全部不在运行，6 GPU 全空闲。实验已完成或异常退出。**

---

## bjb2-28827 (6x RTX 4090)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0 | 1/24564 MiB | 0% |
| cuda:1 | 1977/24564 MiB | 14% |
| cuda:2 | 1/24564 MiB | 0% |
| cuda:3 | 1971/24564 MiB | 18% |
| cuda:4 | 1977/24564 MiB | 18% |
| cuda:5 | 1971/24564 MiB | 19% |

**进程:**
| PID | GPU | 命令 |
|-----|-----|------|
| 573416 | cuda:1 | evaluate.py --mode adaptive_conformal_crm --K 2 --τ=0.25 --spatial --seed 45 |
| 573684 | cuda:3 | evaluate.py --mode vla_only --spatial --seed 45 |
| 573958 | cuda:4 | evaluate.py --mode adaptive_conformal_crm --K 2 --τ=0.25 --spatial --seed 47 |
| 574230 | cuda:5 | evaluate.py --mode vla_only --spatial --seed 47 |

**空闲GPU:** cuda:0, cuda:2
**异常:** tmux session `eval-supp-adapt-tau025-spatial-s48` 已完成（cuda:0空闲）。预期的 τ-sweep τ=0.15/0.10 实验不在运行（已完成）。

---

## bjb1-32546 (6x RTX 4090)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0 | 2/24564 MiB | 0% |
| cuda:1 | 2/24564 MiB | 0% |
| cuda:2 | 1978/24564 MiB | 23% |
| cuda:3 | 1978/24564 MiB | 21% |
| cuda:4 | 2/24564 MiB | 0% |
| cuda:5 | 2/24564 MiB | 0% |

**进程:**
| PID | GPU | 命令 |
|-----|-----|------|
| 918490 | ? | evaluate.py --mode adaptive_conformal_crm --K 2 --τ=0.25 --spatial --seed 49 |

**空闲GPU:** cuda:0, cuda:1, cuda:4, cuda:5
**异常:** 预期6个实验（Adaptive s46/s48/s49 + VLA-only s46/s48/s49），仅1个进程可见（Adaptive s49），但 cuda:2 和 cuda:3 均有显存占用。tmux `eval-obj-vla-s42` 已完成。其余5个实验已完成或异常退出。

---

## bjb2-40593 (1x RTX 4090 D)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0 | 5416/24564 MiB | 11% |

**进程:**
| PID | GPU | 命令 |
|-----|-----|------|
| 349401 | cuda:0 | evaluate.py --mode adaptive_conformal_crm --K 2 --τ=0.075 --spatial --seed 42 |

**空闲GPU:** 无
**异常:** 无，符合预期。

---

## 汇总

| 指标 | 数据 |
|------|------|
| **在跑实验** | **9个**（bjb1-18228: 3, bjb2-28827: 4, bjb1-32546: 1, bjb2-40593: 1） |
| **空闲GPU** | **13个**（bjb1-18228: cuda:0; cqa1-32758: cuda:0~5; bjb2-28827: cuda:0,2; bjb1-32546: cuda:0,1,4,5） |
| **已完成** | CRM训练(bjb1-18228 cuda:0)、cqa1-32758 全部6个实验、bjb2-28827 τ-sweep + supp-s48、bjb1-32546 的5个实验(s46/s48 + VLA-only s46/s48/s49 部分) |

**需关注:**
1. **cqa1-32758** 全部空闲——需检查6个K=2 Spatial实验的日志确认是正常完成还是crash
2. **bjb1-32546** cuda:3 有1978 MiB显存占用但无对应进程可见——可能是残留显存或有隐藏进程

---
