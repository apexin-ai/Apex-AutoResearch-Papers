# harvest cqa1 32758 spatial k2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-32758-spatial-k2-results_20260525T053608_result.json`
- **Structured JSON:** [`cfb53ecc6f780d36a13d.json`](../../sessions/cf/cfb53ecc6f780d36a13d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cqa1-32758 上不存在预期的 6 个 K=2 Spatial 配对实验。**

实际情况：

1. **没有找到** 命名为 `eval-k2-spatial-*-paired` 或含 `k2` + `spatial` + `adapt` 的 JSON 文件
2. **没有** Adaptive spatial 实验使用种子 42/43/44
3. 6 张 GPU 全部空闲（0% 利用率，0 MiB 显存），无 Python 进程运行
4. 最近活动是 **K=10 canonical** 实验（`.log` 文件 May 25），但全部中途被杀——无 JSON 产出，log 显示只跑了部分 task

**服务器上实际存在的 Spatial 配对数据**（seeds 45/46/47，非用户期望的 42/43/44）：

| 文件 | mode | seed | SR | trigger_rate | mean_unc | total_steps | crm_applied | 状态 |
|---|---|---|---|---|---|---|---|---|
| adaptive_conformal_crm_norm0.2_tau0.25_seed45 | adaptive | 45 | 0.800 | 0.1995 | 0.1863 | 28429 | 5673 | 完成 |
| adaptive_conformal_crm_norm0.2_tau0.25_seed46 | adaptive | 46 | 0.800 | 0.1992 | 0.1846 | 28598 | 5696 | 完成 |
| adaptive_conformal_crm_norm0.2_tau0.25_seed47 | adaptive | 47 | 0.815 | 0.2046 | 0.1873 | 28099 | 5748 | 完成 |
| vla_only_seed45 | vla_only | 45 | 0.770 | — | — | — | — | 完成 |
| vla_only_seed46 | vla_only | 46 | 0.805 | — | — | — | — | 完成 |
| vla_only_seed47 | vla_only | 47 | 0.810 | — | — | — | — | 完成 |

**配对 Δ（Adaptive − VLA-only）：**

| seed | Adaptive SR | VLA-only SR | Δ SR |
|---|---|---|---|
| 45 | 0.800 | 0.770 | **+0.030** |
| 46 | 0.800 | 0.805 | **−0.005** |
| 47 | 0.815 | 0.810 | **+0.005** |
| **均值** | **0.805** | **0.795** | **+0.010** |

另有一个无 norm 的 adaptive seed47（SR=0.790）和额外的 VLA-only seeds 42/43/48/49（无配对 adaptive）。

**结论**：用户预期的 K=2 seeds 42/43/44 配对实验未在此服务器上部署或运行过。现有配对数据是 seeds 45/46/47（已完成但可能不是本次部署目标）。K=10 canonical 实验已全部异常终止。

---
