# research d088 data survey

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d088-data-survey_20260520T161525_result.json`
- **Structured JSON:** [`1f774fdcb375bf4fd967.json`](../../sessions/1f/1f774fdcb375bf4fd967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

---

## K=10 Precompute 数据

- **不存在 K=10 precompute cache**
- 仅有 K=1 cache：
  - `crm_cache_k1/object/` (SmolVLA): 65,223 files, 1.5GB, indices 7284–72506
  - `crm_cache_k1_openvla/object/` (OpenVLA): 43,903 files, 3.6GB, indices 0–43902
- `crm_cache_k1/spatial/` 为空

### SmolVLA K=1 cache 字段 (每个 ~21KB):
| 字段 | shape | dtype |
|------|-------|-------|
| `multi_scale_obs` | (4, 960) | fp32 |
| `obs_features` | (960,) | fp32 |
| `vla_action` | (5, 6) | fp32 (h_eff=5 chunks) |
| `expert_action` | (5, 6) | fp32 |
| `task_name` | str | — |

### OpenVLA K=1 cache 字段:
| 字段 | shape | dtype |
|------|-------|-------|
| `multi_scale_obs` | (4, 4096) | fp32 |
| `obs_features` | (4096,) | fp32 |
| `vla_action` | (6,) | fp32 |
| `expert_action` | (6,) | fp32 |
| `task_name` | str | — |

## K=10 Eval 输出

- per-step 数据可用性：**不可用**
- eval JSON 只保存 per-task SR、per_step_K（选了哪个 K）、adaptive_stats
- 不包含 per-step obs_features 或 action variance

## Calibration JSON（最接近的数据源）

`crm_magnitude_calibration.json` — 27,626 steps:
```
{step, task, episode, env_step, k10_variance, k1_correction_magnitude, k2_correction_magnitude, k2_l2_distance, episode_success}
```

`fmvd_calibration.json` — 14,512 steps:
```
{step, task, episode, env_step, fmvd, k10_variance, episode_success}
```

两者有 k10_variance 标量 label，但 **没有 obs_features 向量**。

## 训练数据构建方案

- 来源：**无法直接使用现有数据**
  - K=1 cache 有 obs_features 无 K=10 variance
  - Calibration JSON 有 K=10 variance 无 obs_features
  - 两者数据源不同（offline demos vs online rollouts），无法配对
- 提取方式：需写新脚本 `precompute_uncertainty_labels.py`，类似现有 K=1 precompute 流程但改为 K=10：
  1. 对每个 demo timestep，SmolVLA forward 提取 `obs_features` (960D)
  2. 共享 KV cache 生成 K=10 action samples
  3. 计算 action variance 作为 label
  4. 保存 `{obs_features, action_variance, task_name}`
- 预估数据量：~65K steps（Object benchmark，与现有 K=1 cache 同源）
- 计算开销：每步共享 obs encoding，只多 10 次 action decoding，约 2-3x K=1 precompute 时间
- 需要额外收集：**是**，必须跑新的 precompute 脚本

## SmolVLA 特征

- 维度：obs_features 960D（mean-pooled VLM hidden states），multi_scale 4×960
- 数据类型：fp32
- 存储方式：每步一个 `.pt` 文件，~21KB/步
- SmolVLA wrapper 已有 `get_obs_features_and_samples()` 方法，一次 forward pass 同时返回 obs_features 和 K 个 action samples，可直接复用

---
