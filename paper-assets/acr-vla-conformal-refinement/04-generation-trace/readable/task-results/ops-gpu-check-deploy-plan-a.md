# ops gpu check deploy plan a

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-deploy-plan-a_20260520T212341_result.json`
- **Structured JSON:** [`fd6c2c27a07639f6526b.json`](../../sessions/fd/fd6c2c27a07639f6526b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GPU 状态总览：17/17 全部占用

#### bjb2-40593 (1×4090) — 0 空闲
| GPU | VRAM | Util | 实验 |
|-----|------|------|------|
| 0 | 2.2/24 GB | 19% | `random_selection` object seed48 |

#### bjb1-18228 (4×4090) — 0 空闲
| GPU | VRAM | Util | 实验 |
|-----|------|------|------|
| 0 | 2.0/24 GB | 36% | `crm_obs_only` object norm=0.05 seed45 |
| 1 | 3.4/24 GB | 28% | `crm_perdof` object norm=0.05 seed46 |
| 2 | 2.0/24 GB | 38% | `crm_obs_only` object norm=0.1 seed50 |
| 3 | 2.0/24 GB | 30% | `crm_obs_only` object norm=0.03 seed46 |

#### bjb1-32546 (6×4090) — 0 空闲
| GPU | VRAM | Util | 实验 |
|-----|------|------|------|
| 0 | 2.4/24 GB | 18% | `vla_only` object seed50 |
| 1 | 2.4/24 GB | 33% | `random_selection` object seed49 |
| 2 | 2.5/24 GB | 36% | `crm_obs_only` object norm=0.2 seed52 |
| 3 | 2.1/24 GB | 22% | `crm_obs_only` **spatial** norm=0.2 seed52 |
| 4 | 2.0/24 GB | 0% | `crm_obs_only` object norm=0.1 seed49 |
| 5 | 2.5/24 GB | 32% | `crm_obs_only` object norm=0.05 seed48 |

#### bjb2-28827 (6×4090) — 0 空闲
| GPU | VRAM | Util | 实验 |
|-----|------|------|------|
| 0 | 2.0/24 GB | 27% | `crm_obs_only` object norm=0.2 seed53 |
| 1 | 2.0/24 GB | 25% | `crm_obs_only` object norm=0.03 seed45 |
| 2 | 3.9/24 GB | 26% | `crm_obs_only` object norm=0.03 seed44 |
| 3 | 2.0/24 GB | 18% | `crm_obs_only` object norm=0.05 seed47 |
| 4 | 2.5/24 GB | 30% | `crm_obs_only` object norm=0.1 seed48 |
| 5 | 2.5/24 GB | 29% | `crm_obs_only` object norm=0.2 seed54 |

---

### 2. Plan A 部署：**无法执行** — 没有空闲 GPU

所有 17 张 GPU 都在跑实验（主要是不同 norm 和 seed 的 crm_obs_only/perdof 消融实验）。

### 3. Checkpoint 状态

| Checkpoint | 路径 | 状态 |
|-----------|------|------|
| CRM obs_only (SmolVLA) | `/root/acr-vla-conformal-refinement/checkpoints/crm_obs_only_best.pt` | **不存在** |
| CRM obs_only (SmolVLA) 备选 | `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` | **存在** (1.3 MB) |
| CRM obs_only (OpenVLA) | `/root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt` | **存在** (4.5 MB) |

OpenVLA CRM checkpoint 已就绪，但 bjb2-28827 的 6 张 GPU 全占，同样无法部署 eval。

---

### 4. 当前 RUNNING 实验汇总（17 个）

共跑 17 个 evaluate.py 实验，分布：
- **crm_obs_only**: 13 个（norm=0.03/0.05/0.1/0.2 × 多 seed，覆盖 object + spatial）
- **crm_perdof**: 1 个（norm=0.05 seed46）
- **random_selection**: 2 个（seed48, seed49）
- **vla_only**: 1 个（seed50）

---

### 下一步建议

需要等当前批次实验完成后才能部署 Plan A 和 OpenVLA eval。是否需要我：
1. 检查当前实验的进度（查 log 看跑到第几个 rollout）？
2. 等有 GPU 空出来后自动部署？

---
