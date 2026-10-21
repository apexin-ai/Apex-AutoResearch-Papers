# ssh full cluster scan v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-cluster-scan-v2_20260520T030929_result.json`
- **Structured JSON:** [`2b3a5dd67a450432d22a.json`](../../sessions/2b/2b3a5dd67a450432d22a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全集群扫描结果

### bjb2-28827 (6× GPU)

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 29% | 4718/24564 MiB | eval-crm-spatial-k10-seed49 |
| 1 | 21% | 5606/24564 MiB | eval-vla-only-long-seed49 |
| 2 | **0%** | **1 MiB** | **空闲** — P25-seed43 已完成 (JSON 11:05) |
| 3 | 26% | 5158/24564 MiB | eval-crm-goal-seed47 |
| 4 | 17% | 5606/24564 MiB | eval-crm-goal-seed48 |
| 5 | **99%** | 10397/24564 MiB | **calibrate_crm_signal.py** (启动 11:02, 已跑 ~45min) |

- eval-vla-only-long-seed50 也在跑 (cuda:1 上两个进程复用)
- 新实验 JSON: 全部 NOT YET

---

### bjb1-18228 (4× GPU)

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 20% | 1907/24564 MiB | eval-vla-only-object-seed49-r2 (since 09:19) |
| 1 | 19% | 1971/24564 MiB | eval-vla-only-spatial-seed50 (since 09:42) |
| 2 | **0%** | **1 MiB** | **空闲** — 原实验已完成 |
| 3 | **0%** | **1 MiB** | **空闲** — 原实验已完成 |

- 近期完成: `eval_spatial_obs_only_norm02_seed47` (11:00), `eval_adaptive_k_p50_seed43` (10:55)
- 新实验 JSON: 全部 NOT YET

---

### bjb1-32546 (6× GPU)

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 24% | 4719/24564 MiB | eval-crm-spatial-k10-seed50 |
| 1 | **0%** | **2 MiB** | **空闲** — 原实验已完成 |
| 2 | 21% | 4703/24564 MiB | eval-crm-long-seed48 |
| 3 | 21% | 1972/24564 MiB | eval-vla-only-spatial-seed47 (since 09:39) |
| 4 | 29% | 5031/24564 MiB | eval-vla-only-object-seed51 / eval-crm-long-seed49 |
| 5 | 38% | 5031/24564 MiB | (同上，另一个) |

- 近期完成: `eval_spatial_obs_only_norm02_seed48` (10:53)
- 新实验 JSON: 全部 NOT YET

---

### bjb2-40593 (1× GPU)

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 34% | 9524/24564 MiB | **P25-seed44 仍在跑** (since 08:44, ~2.5h) + calibrate_crm_signal.py (since 11:08, ~9min) |

---

### 重点回答

1. **空闲卡:** bjb2-28827 cuda:2, bjb1-18228 cuda:2/3, bjb1-32546 cuda:1 — 共 **4 张空闲 GPU**

2. **Calibration:** bjb2-28827 cuda:5 上 calibrate_crm_signal.py 正常运行，99% 利用率，已跑 ~45min。bjb2-40593 上也有一个 calibration 实例刚启动 (~9min)。

3. **新部署实验:** 9 个目标 JSON **全部未完成**，但对应进程都在跑（spatial-seed49/50, long-vla-seed49/50, long-obs-seed48/49, object-vla-seed51, goal-obs-seed47/48）。

4. **P25-seed43** (bjb2-28827 cuda:2): **已完成**，JSON 11:05 写出。**P25-seed44** (bjb2-40593 cuda:0): **仍在跑**，已 ~2.5 小时。

5. **bjb1-18228 cuda:2/3 和 bjb1-32546 cuda:1:** 原实验均已完成，GPU 已空闲。

---
