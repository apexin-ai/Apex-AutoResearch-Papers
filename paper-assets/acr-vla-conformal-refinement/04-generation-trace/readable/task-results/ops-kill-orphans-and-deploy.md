# ops kill orphans and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-orphans-and-deploy_20260517T234509_result.json`
- **Structured JSON:** [`664c4405e086c1826517.json`](../../sessions/66/664c4405e086c1826517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 和 3 已成功释放。汇总如下：

---

## 汇总

### bjb2-28827 (6× RTX 4090)

| PID | 实验 | 状态 |
|-----|------|------|
| 449059 + 子进程 449068 | mag_obs_only_norm01_seed46 (cuda:3) | **已 kill** |
| 448773 + 子进程 448782 | mag_obs_only_norm01_seed47 (cuda:1) | **已 kill** |
| 422526 | plan_701-crm-k1-train (cuda:1) | 已自然结束 |
| 434871 | train-crm-k1-accg-object-seed42-full (cuda:0) | 已自然结束 |

**GPU 状态：**

| GPU | 状态 | 占用进程 |
|-----|------|----------|
| cuda:0 | 占用 (5628 MiB) | PID 492545 — 合法实验 |
| cuda:1 | **空闲** | — |
| cuda:2 | 占用 (2875 MiB) | PID 404983 — 合法实验 |
| cuda:3 | **空闲** | — |
| cuda:4 | 占用 (1941 MiB) | PID 389051 — 合法实验 |
| cuda:5 | 占用 (5664 MiB) | PID 488665 — 合法实验 |

**可部署新实验：cuda:1, cuda:3**

---

### bjb1-18228 (4× RTX 4090)

| PID | 实验 | 状态 |
|-----|------|------|
| 649967 | plan_701-precompute-k1-spatial (cuda:0) | 已自然结束 |

**GPU 状态：**

| GPU | 状态 | 占用进程 |
|-----|------|----------|
| cuda:0 | 占用 (2410 MiB) | PID 713405 — 合法实验 |
| cuda:1 | 占用 (5645 MiB) | PID 774342 — 合法实验 |
| cuda:2 | 占用 (5645 MiB) | PID 774543 — 合法实验 |
| cuda:3 | 占用 (5182 MiB) | PID 749547 — 合法实验 |

**可部署新实验：无（全部占用）**

---
