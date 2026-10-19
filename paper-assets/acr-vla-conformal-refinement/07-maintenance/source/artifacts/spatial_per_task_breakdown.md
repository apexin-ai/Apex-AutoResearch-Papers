# Spatial Per-Task SR Breakdown (P0: Reviewer Response)

Generated: 2026-05-24
Eval regime: LIBERO-Spatial, n_rollouts=20 per task, 10 tasks, 8 seeds (42-49)
Methods: VLA-only (baseline_mode=single) vs Adaptive Conformal CRM (τ=0.25, norm=0.2)

## Data Sources (canonical files used)

| Seed | VLA-only source | Adaptive source |
|------|-----------------|-----------------|
| 42 | cqa1-32758 | bjb1-32546 |
| 43 | cqa1-32758 | bjb1-32546 |
| 44 | bjb2-40593 | bjb1-32546 |
| 45 | cqa1-32758 | cqa1-32758 |
| 46 | cqa1-32758 | cqa1-32758 |
| 47 | cqa1-32758 | cqa1-32758 |
| 48 | cqa1-32758 | bjb2-28827 |
| 49 | cqa1-32758 | bjb2-28827 |

All files: `logs/eval_spatial_vla_only_seedXX.json`,
`logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seedXX.json`.

## Per-Task SR (mean over 8 seeds × 20 rollouts = 160 trials per cell)

| Task | VLA-only SR | Adaptive SR | Δ | 备注 |
|------|-------------|-------------|-----|------|
| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |
| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |
| from_table_center | 95.6% | 98.8% | **+3.12pp** | |
| on_cookie_box | 95.6% | 98.8% | **+3.12pp** | |
| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | Adaptive 反降；唯一负 Δ task |
| on_ramekin | 0.0% | 0.0% | 0.00pp | **always-0%** (任务自身极难) |
| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | 接近天花板 |
| on_stove | 81.3% | 82.5% | +1.25pp | |
| next_to_plate | 78.8% | 81.3% | +2.50pp | |
| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |
| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |

## Per-Seed Overall SR and Trigger Rate (all 10 tasks)

| Seed | VLA-only | Adaptive | Δ | trigger_rate |
|------|----------|----------|-----|--------------|
| 42 | 78.50% | 79.50% | +1.00pp | 19.65% |
| 43 | 79.00% | 80.00% | +1.00pp | 19.45% |
| 44 | 78.50% | 80.50% | +2.00pp | 19.98% |
| 45 | 77.00% | 80.00% | +3.00pp | 19.96% |
| 46 | 80.50% | 80.00% | -0.50pp | 19.92% |
| 47 | 81.00% | 81.50% | +0.50pp | 20.46% |
| 48 | 79.50% | 81.00% | +1.50pp | 19.77% |
| 49 | 78.50% | 82.00% | +3.50pp | 19.52% |

## Paired t-test

| Analysis | n_seeds | VLA-only | Adaptive | Δ | t | df | p |
|----------|---------|----------|----------|-----|------|------|-------|
| 全部 10 task | 8 | 79.06% | 80.56% | +1.50pp | 3.240 | 7 | **0.0142** |
| 剔除 always-0% (9 task) | 8 | 87.85% | 89.51% | +1.67pp | 3.240 | 7 | **0.0142** |

注：剔除 on_ramekin 不改变 p-value（恒零任务在 paired t-test 中两 arm 都减去相同值，
方差结构不变；只把 SR base 从 200 缩到 180，Δ 在 pp 单位上等比放大 1.111 倍）。

## Mechanism Analysis

### Per-task Δ vs VLA-only baseline difficulty (sorted)

| Task | VLA-only SR | Δ | bucket |
|------|-------------|-----|--------|
| on_ramekin | 0.0% | +0.00 | impossible |
| in_top_drawer | 71.9% | **-2.50** | hardest non-zero — Adaptive hurts |
| next_to_plate | 78.8% | +2.50 | mid |
| on_stove | 81.3% | +1.25 | mid |
| on_wooden_cabinet | 83.8% | +1.25 | mid |
| between_plate_and_ramekin | 92.5% | +3.75 | high |
| next_to_ramekin | 94.4% | +1.88 | high |
| from_table_center | 95.6% | +3.12 | high |
| on_cookie_box | 95.6% | +3.12 | high |
| next_to_cookie_box | 96.9% | +0.62 | ceiling |

### Trigger-rate observations

- 8 seeds 的 overall trigger_rate 集中在 **19.45%–20.46%**（mean 19.84%, σ=0.31pp），
  几乎不随 seed 变化 → conformal threshold 在 calibration 后表现稳定。
- Per-task trigger_rate 未在 JSON 中输出，无法直接做 task-level trigger ↔ Δ correlation。
- Per-seed corr(trigger_rate, Δ) = **-0.298** (n=8)，weak negative 但 trigger 跨 seed
  几乎不变（range 1pp），相关性极不稳定，不作为证据。

### 结论性观察

1. **9/10 task 上 Adaptive ≥ VLA-only**（含一个 ties，on_ramekin 都是 0%）；
   唯一例外是 **in_top_drawer（−2.50pp）**——也是 VLA-only 最弱的 non-zero task。
   假设：该 task 视觉/几何挑战大（深抽屉里取物），CRM 可能放大了不可靠的 observation refinement。
2. **on_ramekin always-0%** 的根因是任务本身（黑碗放在 ramekin 顶部），与方法无关；
   该 task 完全不被任何方法救起，剔除后 Adaptive 的相对优势绝对值更大（87.85% → 89.51%）。
3. Adaptive 改进 **不集中在最难 task** 上（top_drawer 反而变差），而是 **均匀分布于
   mid-到-high SR task**，最大单 task gain 出现在 between_plate_and_ramekin (+3.75pp)
   和 from_table_center/on_cookie_box (+3.12pp)。
4. 8 个 seed 中 **7/8 Δ ≥ 0**（s46 = -0.5pp 为唯一例外），符号方向稳定，paired
   t-test p=0.0142 显著。
