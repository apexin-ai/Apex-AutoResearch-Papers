# ssh cluster scan session init

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cluster-scan-session-init_20260520T033213_result.json`
- **Structured JSON:** [`72acca36fd92ea7b4b25.json`](../../sessions/72/72acca36fd92ea7b4b25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now compiling the full cluster report.

---

## 集群状态总览 (2026-05-20)

---

## bjb2-28827 (6×4090) — 全满

| GPU | VRAM | Util | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 4190/24564 | 29% | 129425 | `crm_obs_only --benchmark spatial --seed 49 --K 10 --norm 0.2` |
| 1 | 4662/24564 | 16% | 129700 | `vla_only --benchmark long --seed 49` |
| 2 | 5315/24564 | 11% | 154335 | `vla_only --benchmark long --seed 51` |
| 3 | 4253/24564 | 28% | 145404 | `crm_obs_only --benchmark goal --seed 48 --K 10 --norm 0.2` |
| 4 | 4662/24564 | 18% | 129973 | `vla_only --benchmark long --seed 50` |
| 5 | 8566/24564 | 99% | 137179 | `crm_obs_only --benchmark goal --seed 47 --K 10 --norm 0.2` |
| 5 | ↑ 共享 | ↑ | 148827 | **calibrate_crm_signal.py** |

### CRM Calibration (bjb2-28827): 运行中
- 进度: Task 3/10, ep 3/10 (23/100 episodes done)
- 已运行 ~32 min, 速率 ~83s/ep
- **预计还需 ~1.8h** 完成
- 1 次 OK (cream_cheese ep4, 193 steps), 其余全 FAIL
- 输出 JSON: **未生成** (crm_magnitude_calibration.json 不存在)

### 最近完成的 JSON (bjb2-28827, 24h):

| 文件 | overall_success_rate |
|------|---------------------|
| eval_adaptive_k_p75_seed42.json | **0.12** |
| eval_adaptive_k_p75_seed43.json | **0.13** |
| eval_adaptive_k_p90_seed43.json | **0.14** |
| eval_adaptive_k_p90_seed44.json | **0.14** |
| eval_adaptive_k_p50_seed42.json | **0.16** |
| eval_adaptive_k_p25_seed43.json | **0.13** |
| eval_crm_goal_seed46.json | **0.72** |
| eval_crm_goal_seed44_r2.json | **0.64** |
| eval_crm_goal_seed45_r2.json | **0.65** |
| eval_crm_long_seed47.json | **0.17** |
| eval_long_obs_only_norm02_seed42.json | **0.17** |
| + 25 more eval/calibration JSONs | |

---

## bjb1-18228 (4×4090) — 3/4 occupied, GPU 1 空闲

| GPU | VRAM | Util | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 5221/24564 | 18% | 239026 | `adaptive_k --threshold 0.054959 --k_full 10 --benchmark object --seed 44` (p25) |
| 1 | 1/24564 | **0%** | — | **空闲** |
| 2 | 5248/24564 | 29% | 235421 | `crm_obs_only --benchmark spatial --seed 51 --K 10 --norm 0.2` |
| 3 | 5606/24564 | 20% | 235691 | `vla_only --benchmark long --seed 52` |

### 最近完成的 JSON (bjb1-18228, 24h):

| 文件 | overall_success_rate |
|------|---------------------|
| eval_adaptive_k_p50_seed43.json | **0.16** |
| + 22 more eval JSONs | |

---

## bjb1-32546 (6×4090) — 全满

| GPU | VRAM | Util | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 3660/24564 | 27% | 199984 | `crm_obs_only --benchmark spatial --seed 50 --K 10 --norm 0.2` |
| 1 | 5149/24564 | 19% | 216401 | `vla_only --benchmark spatial --seed 51` |
| 2 | 3771/24564 | 20% | 200256 | `vla_only --benchmark object --seed 51` |
| 3 | 5707/24564 | 37% | 219383 | `crm_obs_only --benchmark long --seed 50 --K 10 --norm 0.2` |
| 4 | 4400/24564 | 37% | 200532 | `crm_obs_only --benchmark long --seed 48 --K 10 --norm 0.2` |
| 5 | 4399/24564 | 28% | 201124 | `crm_obs_only --benchmark long --seed 49 --K 10 --norm 0.2` |

### 最近完成的 JSON (bjb1-32546, 24h):

| 文件 | overall_success_rate |
|------|---------------------|
| eval_adaptive_k_p75_seed44.json | **0.16** |
| eval_adaptive_k_p90_seed42.json | **0.12** |
| eval_adaptive_k_p50_seed44.json | **0.14** |
| eval_adaptive_k_p25_seed42.json | **0.15** |
| + 38 more eval JSONs | |

---

## bjb2-40593 (1×4090) — GPU 共享两进程

| GPU | VRAM | Util | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 9057/24564 | 79% | 647880 | `adaptive_k --threshold 0.054959 --k_full 10 --benchmark object --seed 44` (p25) |
| 0 | ↑ 共享 | ↑ | 660279 | **calibrate_crm_signal.py** (SCREEN session) |

### CRM Calibration (bjb2-40593): 运行中
- 进度: Task 1/10, ep 8/10 (8/100 episodes done)
- 已运行 ~17 min, 速率 ~125s/ep (共享 GPU 较慢)
- **预计还需 ~3h** 完成
- 输出 JSON: **未生成**

### 最近完成的 JSON (bjb2-40593, 24h):
- eval_object_scalar_seed45_r2.json, eval_spatial_obs_only_norm02_seed44.json, eval_object_vla_only_seed48.json

---

## 关键发现

1. **CRM Calibration 在两台机器上并行运行** — bjb2-28827 (cuda:5, 独立进程但与 goal-seed47 共享) 和 bjb2-40593 (cuda:0, 与 adaptive_k 共享)。两处均未生成最终 JSON，都还在早期阶段。

2. **bjb1-18228 GPU 1 空闲** — 可以调度新任务。

3. **adaptive_k 全系列 (object benchmark) 结果**: p25/p50/p75/p90 全在 0.12–0.16 区间，相互无显著差异。

4. **CRM goal benchmark 表现优秀**: seed44=0.64, seed45=0.65, seed46=0.72。

5. **CRM long benchmark 表现较差**: seed47=0.17, long_obs_only_norm02 seed42=0.17。

6. **集群总计**: 17 GPU 中 16 个在跑实验，全力运转。

---
