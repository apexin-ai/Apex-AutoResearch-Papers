# analyze ssh check and d102 17855 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_ssh-check-and-d102-17855-v3_20260522T010620_result.json`
- **Structured JSON:** [`c1282fb5cef563cd7944.json`](../../sessions/c1/c1282fb5cef563cd7944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts already copied on 19828. Here's the complete summary:

---

## westd-17855 全部实验

### 已完成 + d102 已分析
| 实验 | Gens | 状态 |
|---|---|---|
| t05_a045_s42_fp32 | 6/6 | COMPLETED, d102 ✓ |
| t05_a050_s42_fp32 | 6/6 | COMPLETED, d102 ✓ |
| t05_a060_s42_fp32 | 6/6 | COMPLETED, d102 ✓ |
| t05_a075_s42_fp32 | 6/6 | COMPLETED, d102 ✓ |
| t15_a050_s42_fp32 | 16/16 | COMPLETED, d102 ✓ |
| t15_a060_s42_fp32 | 16/16 | COMPLETED, d102 ✓ |
| t15_a075_s42_fp32 | 16/16 | COMPLETED, d102 ✓ |
| t15_a045_s43_fp32 | gen_14-15 only (earlier gens cleaned) | COMPLETED, d102 ✓ |
| t15_a060_s43_fp32 | no gen dirs (cleaned), has analysis | COMPLETED, d102 ✓ |
| t25_a045_s42_fp32 | no gen dirs (cleaned), has analysis | COMPLETED, d102 ✓ |

### 运行中 (多个进程活跃)
| 实验 | Gens | 进度 |
|---|---|---|
| **t25_a050_s42_fp32 ★** | **15/26** | **~58% RUNNING** |
| **t25_a060_s42_fp32 ★** | **15/26** | **~58% RUNNING** |
| t20_a060_s43_fp32 | 16/21 | ~76% RUNNING |
| t25_a045_s43_fp32 | 4/26 | ~15% RUNNING |
| t15_a075_s43_fp32 | 2/16 | ~13% RUNNING |

---

## westd-19828 全部实验

### 已完成 + d102 已分析 + artifacts 已复制
| 实验 | Gens | PermG fwd | Robust K≥3 |
|---|---|---|---|
| t25_a075_s42_fp32 | 26/26 | **6/8** | 6/8 |
| t20_a045_s43_fp32 | 21/21 | **4/8** | 5/8 |
| t15_a045_s42_fp32 | 16/16 | **6/8** | 5/8 |

### 运行中
| 实验 | Gens | 进度 |
|---|---|---|
| t25_a075_s43_fp32 | 4/26 | ~15% RUNNING |

---

## 关键发现

**t25_a060★ 尚未完成** — 15/26 gens (~58%)，无法判定 Scenario A vs B。预计还需数小时完成，之后需跑 d102。

**t25_a050★ 同样 15/26**，两个 Phase Diagram 最后两格都在约 58% 进度。

19828 三个已完成实验的 d102 分析和 artifacts 均已就绪，无需额外操作。17855 的 5 个目标实验全部仍在运行中。

---
