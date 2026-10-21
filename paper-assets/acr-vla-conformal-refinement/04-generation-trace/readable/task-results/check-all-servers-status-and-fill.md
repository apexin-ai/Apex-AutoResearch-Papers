# check all servers status and fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-servers-status-and-fill_20260525T075349_result.json`
- **Structured JSON:** [`abeae5ccaf0bad126fca.json`](../../sessions/ab/abeae5ccaf0bad126fca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## bjb1-18228 (4x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | eval-pi05-adaptive-spatial-s42-r2 | 484291 | 14135 MiB |
| cuda:1 | eval-pi05-vla-only-object-s42-r2 | 484675 | 10365 MiB |
| cuda:3 | precompute-pi05-long-2048-r2 | 114507 | 9883 MiB |

**空闲 GPU:** cuda:2（但有 10429 MiB 泄漏显存，需 GPU reset 回收）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-pi05-vla-only-spatial-s43-r2` (pid 485043, cuda:2) — **已完成** SR=97.5%，进程已退出但显存未释放
- `eval-pi05-vla-only-goal-s42-paired` (pid 446717) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-vla-only-spatial-s42-paired` (pid 446358) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-adaptive-spatial-s42` — conclusion=failed，已死

**用户指定的旧实验:**
- `precompute-pi05-object-2048-r2` — registry 已是 DONE/success，不在 RUNNING 列表

---

## bjb2-28827 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-goal-adapt-s45-paired | 639192 |
| cuda:1 | eval-k2-goal-vla-only-s45-paired | 639189 |
| cuda:2 | eval-k2-goal-adapt-s46-paired | 639190 |
| cuda:3 | eval-k2-goal-vla-only-s46-paired | 639199 |
| cuda:4 | eval-k2-goal-adapt-s47-paired | 639193 |
| cuda:5 | eval-k2-goal-vla-only-s47-paired | 639194 |

**空闲 GPU:** 无（6/6 全满）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-tau010-spatial-s42-r3` (cuda:2) — 被 Goal K=2 配对覆盖
- `eval-k2-tau015-spatial-s42-r2` (cuda:0) — 被 Goal K=2 配对覆盖
- `eval-canonical-adaptive-k10-spatial-s44` (conclusion=killed)
- `eval-canonical-adaptive-k10-spatial-s43` (conclusion=killed)

**用户指定的旧实验:**
- eval-supp-obj-reconvla-s47, eval-supp-goal-reconvla-s47, eval-supp-goal-k2mean-s47, eval-supp-goal-crm-norm005-s47, eval-supp-goal-adapt-tau025-s47 — **全部已是 DONE/success**，不在 RUNNING 列表

---

## bjb1-32546 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-spatial-adapt-s42-paired-r2 | 978848 |
| cuda:1 | eval-k2-spatial-vla-only-s42-paired-r2 | 980371 |
| cuda:2 | eval-k2-spatial-adapt-s43-paired-r2 | 981563 |
| cuda:4 | eval-k2-spatial-adapt-s44-paired-r2 | 984726 |
| cuda:5 | eval-k2-spatial-vla-only-s44-paired-r2 | 986463 |

**空闲 GPU:** cuda:3

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-spatial-vla-only-s43-paired-r2` (cuda:3) — **已完成** SR=79.5%，GPU 3 已释放
- `eval-k2-adaptive-spatial-s49` (cuda:3) — 被 K=2 spatial r2 覆盖
- `eval-k2-adaptive-spatial-s48` (cuda:2) — 被覆盖
- `eval-k2-adaptive-spatial-s46` (cuda:0) — 被覆盖
- `eval-vla-only-spatial-bjb1-s46` — 被覆盖
- `eval-vla-only-spatial-bjb1-s49` (cuda:4) — 被覆盖
- `eval-vla-only-spatial-bjb1-s48` (cuda:1) — 被覆盖
- `eval-k10-tau025-spatial-s46` (killed)
- `eval-canonical-adaptive-k10-spatial-s49` (killed)
- `eval-canonical-adaptive-k10-spatial-s48` (killed)

**用户指定的旧实验:**
- eval-supp-spatial-k2mean-s46, eval-supp-reconvla-obj-s45, eval-smolvla-lerobot-goal-seed43-v3, eval-smolvla-lerobot-spatial-seed43-v3 — **不在 RUNNING registry**（已完成或已终止）

---

## bjb2-40593 (1x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-tau0075-spatial-s42 | 349401 |

**空闲 GPU:** 无

**τ=0.075 状态:** 仍在运行，正在跑最后一个 task（task 10/10，rollout 10/20）。预计很快完成。JSON 文件尚未生成。

---

## cqa1-32758 补充（已禁用但 registry 仍标 RUNNING）

以下 12 个实验挂在 cqa1 上，全是 zombie：
- eval-vla-only-spatial-cqa1-s44/s43/s42
- eval-k2-adaptive-spatial-s44/s43/s42
- eval-canonical-adaptive-k10-spatial-s42 (killed)
- eval-k10-tau025-spatial-s47/s45 (killed)
- eval-long-adaptive-k10-s44/s43/s42 (killed)

---

## 总结

| 服务器 | 在跑 | 空闲GPU | Zombie数 |
|--------|------|---------|----------|
| bjb1-18228 | 3 | 1 (cuda:2, 显存泄漏) | 4 |
| bjb2-28827 | 6 | 0 | 4 |
| bjb1-32546 | 5 | 1 (cuda:3) | 10 |
| bjb2-40593 | 1 | 0 | 0 |
| cqa1-32758 | 0 | — | 12 |

Registry 共 45 个 RUNNING，实际只有 **15 个真正在跑**。**30 个 zombie** 需要清理。

---
