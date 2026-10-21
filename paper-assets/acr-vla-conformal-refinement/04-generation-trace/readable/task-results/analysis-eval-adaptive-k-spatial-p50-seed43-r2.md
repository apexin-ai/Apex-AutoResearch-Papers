# analysis eval adaptive k spatial p50 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-adaptive-k-spatial-p50-seed43-r2_20260520T091527_result.json`
- **Structured JSON:** [`75a134edc1cd84c37d43.json`](../../sessions/75/75a134edc1cd84c37d43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成（EXIT_CODE=0）。结果如下：

## 总体指标

| 指标 | 值 |
|------|-----|
| **success_rate** | **33.0%** (33/100) |
| n_tasks | 10 |
| n_rollouts | 10 per task |
| total_rollouts | 100 |
| **avg_K** | **6.33** |
| **fast_path_ratio** | **45.8%** |
| adaptive_trigger_rate | 54.2% |
| mean_l2_distance | 0.0903 |
| threshold (τ) | 0.074855 |
| total_steps | 23,414 |
| fast_steps (K=2) | 10,728 |
| full_steps (K=10) | 12,686 |

## Per-task SR

| Task | SR |
|------|-----|
| bowl_next_to_ramekin → plate | **100%** (10/10) |
| bowl_next_to_cookie_box → plate | **90%** (9/10) |
| bowl_between_plate_and_ramekin → plate | **80%** (8/10) |
| bowl_on_cookie_box → plate | 40% (4/10) |
| bowl_in_top_drawer → plate | 10% (1/10) |
| bowl_next_to_plate → plate | 10% (1/10) |
| bowl_from_table_center → plate | 0% (0/10) |
| bowl_on_ramekin → plate | 0% (0/10) |
| bowl_on_stove → plate | 0% (0/10) |
| bowl_on_wooden_cabinet → plate | 0% (0/10) |

## 与 Baseline 对比

| 配置 | SR | avg_K | fast_path |
|------|-----|-------|-----------|
| **Spatial K=10 固定** | **34.4±1.5%** | 10.0 | 0% |
| **Spatial Adaptive P50 (本次)** | **33.0%** | 6.33 | 45.8% |
| Object Adaptive P50 (参考) | 15.3% | ~3.8 | ~77% |

## Checkpoint

- CRM: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- SmolVLA: `/root/autodl-tmp/models/smolvla_libero/`
- max_correction_norm: 0.2

## 关键发现

1. **SR 33.0% vs K=10 baseline 34.4%** — 仅损失 1.4pp，在 ±1.5% 的 baseline 方差范围内，可认为**无显著差异**
2. **avg_K=6.33，节省 36.7% 推理次数**（vs K=10 固定），但远不如 Object benchmark 的 avg_K=3.8
3. **fast_path=45.8%** 远低于 Object 的 77% — Spatial 任务的 L2 divergence 更频繁超过 P50 阈值，说明 Spatial 场景 CRM 修正需求更大
4. 任务极化严重：3 个 task ≥80% SR，4 个 task = 0%，与 K=10 固定模式的 task 分布应基本一致

---
