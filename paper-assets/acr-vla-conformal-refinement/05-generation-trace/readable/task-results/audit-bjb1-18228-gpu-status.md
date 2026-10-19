# audit bjb1 18228 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-18228-gpu-status_20260520T140259_result.json`
- **Structured JSON:** [`14413ffa9ee814dd9e41.json`](../../sessions/14/14413ffa9ee814dd9e41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 GPU 审计报告

### 当前实际进程（全部于 21:07 今天启动）

| GPU | PID | 实验 | 输出文件 | 状态 |
|-----|-----|------|----------|------|
| **0** | 384503 | `adaptive_k` spatial p90 seed44 | `eval_adaptive_k_spatial_p90_seed44.json` | **RUNNING** — 正在跑 spatial tasks |
| **1** | 384777 | `random_selection` spatial seed42 **r2** | `eval_random_selection_spatial_seed42_r2.json` | **RUNNING** — 正在跑 spatial tasks |
| **2** | 385308 | `crm_obs_only` spatial seed48 norm02 | `eval_obs_only_spatial_norm02_seed48.json` | **RUNNING** — 正在跑 spatial tasks |
| **3** | 385902 | `vla_only` spatial seed48 | `eval_vla_only_spatial_seed48.json` | **RUNNING** — 正在跑 spatial tasks |

GPU 利用率 22-34%，显存各占 ~3.1-3.6 GB / 24 GB，均为活跃进程。

---

### Registry 中 4 个实验的状态

| Registry exp_id | 原 GPU | 原 PID | 实际状态 | JSON |
|----------------|--------|--------|----------|------|
| eval-random-selection-spatial-seed42 | cuda:0 | 346801 | **已结束** — PID 不存在 | **COMPLETE** `eval_random_selection_spatial_seed42.json` (May 20 20:27) — overall_sr=**0.34** |
| eval-random-selection-spatial-seed44 | cuda:2 | 348897 | **已结束** — PID 不存在 | **COMPLETE** `eval_random_selection_spatial_seed44.json` (May 20 20:31) — overall_sr=**0.28** |
| eval-perdof-object-norm02-seed45-r3 | cuda:3 | unknown | **已结束** — PID 不存在 | **COMPLETE** `eval_object_perdof_norm02_seed45_r3.json` (May 18 18:14) — overall_sr=**0.12** |
| (unknown harvest-deploy) | cuda:1 | unknown | **已结束** — 无法确认原始进程 | 无法确定对应 JSON |

---

### 推荐操作

- **GPU 0-3**：4 个新实验在正常运行，不要干预。等待完成后收割结果。
- **Registry 3 个命名实验**：全部已完成且有完整 JSON 输出，应标记为 **COMPLETED**。
- **harvest-deploy worker (cuda:1)**：进程已消失，无法回溯。如果 registry 有对应条目，标记为 COMPLETED 或 UNKNOWN。
- **当前 4 个运行实验**：如果 registry 中没有对应条目，需要补录（它们是 21:07 今天部署的新一批）。

---
