# audit bjb2 28827 cleanup r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-cleanup-r2_20260519T122231_result.json`
- **Structured JSON:** [`4d4f70c9355f68689e5e.json`](../../sessions/4d/4d4f70c9355f68689e5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整报告。

---

## bjb2-28827 进程排查报告

**服务器确认**: 6 张 GPU，连接正确。

---

### 1. reconvla K=5 seed42 — **已完成** ✓

| 项目 | 值 |
|---|---|
| 状态 | 已完成，JSON 写入于 May 19 20:21 |
| GPU | GPU 4 — 现已空闲 (0%, 1 MiB) |
| tmux | 无活跃 session |
| Overall SR | **13%** |

**Per-task SR:**
| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 30% (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 0% (0/10) |
| butter | 10% (1/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 20% (2/10) |
| orange_juice | 30% (3/10) |

---

### 2. perdof norm005 seed45 — **运行中，9/10 tasks 完成**

| 项目 | 值 |
|---|---|
| PID | 664406 (启动 05:56, ~14.5h) |
| GPU | GPU 0 — 18% util, 1942 MiB |
| tmux | eval-perdof-norm005-seed45-t16 |
| 当前进度 | orange_juice rollout 3/10 |
| 预计剩余 | ~1h |

**已完成 9 tasks:**
| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 30% (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 0% (0/10) |
| butter | 10% (1/10) |
| milk | 0% (0/10) |
| chocolate_pudding | 30% (3/10) |

---

### 3. perdof norm03 seed43 — **运行中，9/10 tasks 完成**

| 项目 | 值 |
|---|---|
| PID | 657632 (启动 05:25, ~15h) |
| GPU | GPU 5 — 19% util, 1942 MiB |
| tmux | eval-perdof-norm03-seed43-t16 |
| 当前进度 | orange_juice rollout 4/10 |
| 预计剩余 | ~1h |
| 注意 | 无 log 文件（cwd=/root，tee 输出丢失），仅 tmux scrollback 可见 |

已完成 9 tasks，tmux 可见: chocolate_pudding 10% (1/10)

---

### 4. obs_only norm003 seed44 — **运行中，9/10 tasks 完成**

| 项目 | 值 |
|---|---|
| PID | 657432 (启动 05:25, ~15h) |
| GPU | GPU 2 — 99% util, 1923 MiB（与 random_selection_seed46 共享） |
| tmux | eval-obs-only-norm003-seed44-t16 |
| 当前进度 | orange_juice rollout 6/10 |
| 预计剩余 | ~30min |
| 注意 | 无 log 文件（cwd=/root，tee 输出丢失） |

已完成 9 tasks，tmux 可见: chocolate_pudding 30% (3/10)

---

### 5. random_selection seed46 — **运行中，6/10 tasks 完成**

| 项目 | 值 |
|---|---|
| PID | 693631 (启动 09:34, ~11h) |
| GPU | GPU 2 — 2820 MiB（与 obs_only 共享，合计 4777 MiB） |
| tmux | eval-random-seed46-t16 |
| 当前进度 | butter rollout 3/10 |
| 预计剩余 | ~4-5h |

**已完成 6 tasks:**
| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 10% (1/10) |
| ketchup | 10% (1/10) |
| tomato_sauce | 0% (0/10) |

---

### 额外发现：2 个未在任务列表中的进程

**6. reconvla/argmin K=5 seed44** — GPU 1, 运行中
| 项目 | 值 |
|---|---|
| PID | 758237 (启动 16:21, ~4h) |
| GPU | GPU 1 — 17% util, 3749 MiB |
| tmux | eval-argmin-object-k5-seed44 |
| 进度 | 4/10 tasks 完成, 当前 ketchup rollout 5/10 |
| 已完成 SR | alphabet_soup 0%, cream_cheese 10%, salad_dressing 10%, bbq_sauce 20% |

**7. spatial obs_only norm02 seed44** — GPU 3, 运行中
| 项目 | 值 |
|---|---|
| PID | 697045 (启动 09:51, ~10.5h) |
| GPU | GPU 3 — 19% util, 1987 MiB |
| tmux | eval-spatial-obs-only-norm02-seed44 |
| 进度 | 8/10 tasks 完成, 当前 black_bowl_next_to_plate rollout 8/10 |

---

### GPU 总览

| GPU | 进程 | Util | Memory |
|---|---|---|---|
| 0 | perdof_norm005_seed45 | 18% | 1942 MiB |
| 1 | argmin_k5_seed44 (额外) | 17% | 3768 MiB |
| 2 | obs_only_norm003_seed44 + random_selection_seed46 | 99% | 4777 MiB |
| 3 | spatial_obs_only_norm02_seed44 (额外) | 19% | 2006 MiB |
| 4 | **空闲** | 0% | 1 MiB |
| 5 | perdof_norm03_seed43 | 19% | 1942 MiB |

perdof_norm005_seed45、perdof_norm03_seed43、obs_only_norm003_seed44 三个都在最后一个 task (orange_juice)，预计 0.5-1h 内全部完成。random_selection_seed46 还需 4-5h。GPU 4 空闲可用。

---
