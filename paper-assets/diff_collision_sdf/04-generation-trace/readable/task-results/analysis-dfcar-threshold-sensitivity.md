# analysis dfCAR threshold sensitivity

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dfCAR_threshold_sensitivity_20260526T010133_result.json`
- **Structured JSON:** [`97c43a909664ac547ea4.json`](../../sessions/97/97c43a909664ac547ea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. Results are saved both on the server and locally.

---

## 汇报

### 1. 数据覆盖

**6 个 eval JSON** 含 `max_ee_displacement`，均为 A1 SDF-trained Pi0.5 条件，共 **1200 episodes**（4 tasks × 50 episodes × 6 files）：

| 条件 | Episodes | 文件 |
|------|----------|------|
| s0_lam0.05_30k | 200 | `eval_s0_l005_30k_r4.json` |
| s0_lam0.1_30k | 200 | `eval_s0_l01_30k_disp.json` |
| s1_lam0.05_30k | 400 | `eval_30k_s1_l005_disp.json` + `eval_s1_l005_30k_disp.json` (2次eval) |
| s1_lam0.05_best | 200 | `eval_s1_l005_best_16k.json` |
| s2_lam0.05_best | 200 | `eval_s2_l005_best_10k.json` |

### 2. 核心发现：EE displacement 分布

**NOT bimodal — unimodal, right-skewed.** 所有 1200 episodes 的 `max_ee_displacement` 范围为 **[239mm, 1222mm]**，均值 498mm，中位数 428mm。

**关键结论：0 个 episode 的 ee_disp < 100mm。** 最小值 239mm 远大于 δ=100mm。换言之，在这些 SDF-trained 模型上没有 "frozen episode"（机器人不动/微动）。

### 3. Threshold sensitivity — 完全 robust

filtered_CAR 在 δ ∈ [2mm, 200mm] 范围内**完全不变**（与 raw CAR 完全相同）。直到 δ=300mm 才开始有少量 episode (65/1200 = 5.4%) 被过滤掉。

这意味着 **δ=100mm 的选择极其 robust**：δ 可以是 2mm 到 200mm 之间的任何值，结果完全相同。δ=100mm 落在一个巨大的 "safe zone" 内。

### 4. 输出文件

**服务器端** (`/root/colliforce-vla/analysis/threshold_sensitivity/`):
- `threshold_sensitivity.csv` — 完整数值表
- `ee_displacement_combined.png` — 全局 EE displacement 分布直方图
- `ee_displacement_distribution.png` — 按条件分面直方图
- `sensitivity_curves.png` — filtered_CAR vs δ 曲线
- `analysis_summary.json` — 机器可读摘要

**本地** (`artifacts/threshold_sensitivity/` 下有相同文件副本)

### 5. 缺失数据

以下条件**没有** `max_ee_displacement`，无法分析：
- **Pi0.5 baseline** (4 seeds): `eval_safelibero_object_all_levelII__lora_baseline_seed{0,1,2,3}.json`
- **Pi0.5 baseline (spatial)**: `eval_safelibero_spatial_all_levelII_best_lora_baseline_seed0.json`
- **Oracle** (3种): `oracle_true_gt_*.json`, `oracle_force_refine_*.json`, `oracle_m024fix_*.json`
- **早期 SDF eval** (`_final.json`, `_v3.json`, `_v4.json`) — 这些是修复 ee_displacement 记录之前的 eval 运行
- **Pi0.5 safelibero object s1/s2**: `pi05_safelibero_object_v11_s{1,2}.json`

baseline 是最可能出现低 ee_disp（frozen episodes）的条件，如果需要展示 "baseline 有 fake-safe 而 dfCAR 能过滤它们"，需要对 baseline 重新跑一次带 ee_displacement 记录的 eval。

---
