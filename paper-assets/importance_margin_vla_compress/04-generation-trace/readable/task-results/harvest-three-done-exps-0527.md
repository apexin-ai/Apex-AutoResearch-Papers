# harvest three done exps 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_three_done_exps_0527_20260527T012735_result.json`
- **Structured JSON:** [`6b833611a165eb38223a.json`](../../sessions/6b/6b833611a165eb38223a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个已完成实验已收割，3 个"未注册"实验实际均已在 registry 中。现在汇总 cliff curve 数据。

---

## 任务 1 结果：3 个实验收割完毕

| 实验 | Overall SR | 状态 |
|------|-----------|------|
| eval_openvla_attn_k05_long_seed42 | **14.6%** (73/500) | DONE ✅ |
| eval_pi05_random_k07_long_seed42 | **62.4%** (312/500) | DONE ✅ |
| eval_openvla_random_k075_goal_seed42 | **72.0%** (360/500) | DONE ✅ |

## 任务 2 结果：注册检查

3 个指定实验均已在 registry 中存在（非新发现的未注册实验）：
- `eval_openvla_attn_k07_long_seed42_v2` — DONE, 24.0%
- `eval_openvla_l2norm_k075_long_seed42` — DONE (failed/timeout), 仍在重跑中
- `eval_openvla_random_k05_object_seed42_v2` — DONE (killed)

当前 RUNNING 实验 12 个，全部已注册。

## 任务 3：OpenVLA Cliff Curves

### OpenVLA Long (LIBERO-10) Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | — | 14.6% | 18.6% | 52.8% |
| 0.70 | 31.2% | 24.0% | 38.8% | 52.8% |
| 0.75 | 🏃 running | 🏃 running | 🏃 running | 52.8% |
| 0.85 | 38.8% | 45.8% | 45.0% | 52.8% |
| 0.90 | 43.6% | 44.0% | 46.8% | 52.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 52.8% |

### OpenVLA Goal Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | 43.4% | 44.2% | 52.2% | 74.8% |
| 0.70 | 68.4% | 66.4% | 68.4% | 74.8% |
| 0.75 | 70.2% | — | **72.0%** | 74.8% |
| 0.85 | 75.4% | 74.6% | 78.6% | 74.8% |
| 0.90 | 74.8% | 73.2% | 79.6% | 74.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 74.8% |

### OpenVLA Object Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.30 | 25.0% | — | — | 74.0% |
| 0.50 | 39.2% | — | 35.8% | 74.0% |
| 0.70 | 49.8% | 43.8% | 44.4% | 74.0% |
| 0.75 | 57.4% | 53.2% | — | 74.0% |
| 0.85 | — | 55.0% | — | 74.0% |
| 0.90 | 70.6% | — | 64.6% | 74.0% |
| 0.95 | 70.6% | 🏃 running | 🏃 running | 74.0% |

---

**关键观察：**
- **Goal Random** cliff：k=0.75 → 72.0% 填入后，斜率清晰：79.6% → 78.6% → 72.0% → 68.4%，下降主要在 k=0.85→0.75 区间（6.6pp drop）
- **Long** suite 三种方法在 k=0.85~0.9 趋于收敛（43.6~46.8%），离 baseline 52.8% 仍有 gap
- **Goal Random 在 k≥0.85 超过 baseline**（78.6~79.6% vs 74.8%），暗示 moderate random pruning 可能有正则化效果
- k=0.75 和 k=0.95 的 Long/Goal/Object 数据点正在跑，预计 3-6h 内完成

---
