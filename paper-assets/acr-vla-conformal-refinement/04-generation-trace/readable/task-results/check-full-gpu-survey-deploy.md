# check full gpu survey deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-gpu-survey-deploy_20260517T182416_result.json`
- **Structured JSON:** [`dad89801d3692afbc28f.json`](../../sessions/da/dad89801d3692afbc28f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 摸底

### bjb2-28827 (6 GPUs)
| GPU | Mem Used | Status | Task |
|-----|---------|--------|------|
| cuda:0 | 1 MiB → 7.5 GiB | **已部署 latency profile** | plan_602 latency profiling (已完成) |
| cuda:1 | 5664 MiB | BUSY | obs_only norm=0.1 seed47 |
| cuda:2 | 4269 MiB | BUSY | perdof norm=0.2 seed47 |
| cuda:3 | 5664 MiB | BUSY | obs_only norm=0.1 seed46 |
| cuda:4 | 3804 MiB | BUSY | perdof norm=0.2 seed46 |
| cuda:5 | 5664 MiB | BUSY | perdof norm=0.2 seed43 r3 |

### bjb1-32546 (6 GPUs)
| GPU | Mem Used | Status | Task |
|-----|---------|--------|------|
| cuda:0 | 3805 MiB | BUSY | obs_only norm=0.05 seed43 r2 |
| cuda:1 | 2876 MiB | BUSY | perdof norm=0.1 seed47 r2 |
| cuda:2 | 3343 MiB | BUSY | obs_only norm=0.3 seed46 |
| cuda:3 | 3342 MiB | BUSY | obs_only default seed46 |
| cuda:4 | 1943 MiB | BUSY | perdof norm=0.1 seed46 |
| cuda:5 | 3343 MiB | BUSY | perdof default seed46 |

### bjb1-18228 (4 GPUs)
| GPU | Mem Used | Status | Task |
|-----|---------|--------|------|
| cuda:0 | 4269 MiB | BUSY | perdof norm=0.2 seed45 |
| cuda:1 | 4268 MiB | BUSY | obs_only norm=0.05 seed43 r3 |
| cuda:2 | 2875 MiB | BUSY | obs_only norm=0.2 K=5 seed42 |
| cuda:3 | 5201 MiB | BUSY | obs_only norm=0.2 K=20 seed42 |

### bjb2-40593 (1 GPU)
| GPU | Mem Used | Status | Task |
|-----|---------|--------|------|
| cuda:0 | 4663 MiB | BUSY | random_selection seed42 |

## 部署结果

| exp_id | server | GPU | 状态 |
|--------|--------|-----|------|
| plan_602-latency-profile | bjb2-28827 | cuda:0 | **DONE** (PID 455788) |

### P1 Latency Profile 结果

| Component | Mean (ms) | Std |
|-----------|-----------|-----|
| VLA encode_prefix | 33.5 | 1.0 |
| VLA sample K=1 | 192.6 | 1.9 |
| VLA sample K=5 | 965.3 | 9.2 |
| VLA sample K=10 | 1913.7 | 17.6 |
| VLA sample K=20 | 3858.2 | 32.9 |
| CGS compute_features | 6.2 | 0.4 |
| **CRM forward** | **0.3** | 0.0 |
| Full pipeline K=10 | 1908.2 | 30.5 |

**关键发现**: ACR-VLA 的 CGS+CRM 额外开销仅 6.5ms（占 VLA K=10 采样的 0.34%）。VLA 采样线性扩展 ~193ms/sample。

### P2-P4 部署情况
- **P2**: random_selection seed42 已在 bjb2-40593 运行中，跳过
- **P3**: K=5 和 K=20 sweep 已在 bjb1-18228 运行中
- **P4**: 无空闲 GPU 可用

**所有 17 张 GPU 满载运行，无法部署额外实验。**

---
