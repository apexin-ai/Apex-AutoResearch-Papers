# analysis per task spatial breakdown

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per-task-spatial-breakdown_20260524T222035_result.json`
- **Structured JSON:** [`f93480e2de296107f830.json`](../../sessions/f9/f93480e2de296107f830.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Spatial 10-Task SR Breakdown (VLA-only vs Adaptive τ=0.25, 8 seeds × 20 rollouts)

| Task | VLA-only | Adaptive | Δ | 备注 |
|------|----------|----------|-----|------|
| between_plate_and_ramekin | 92.5% | 96.3% | **+3.75pp** | |
| next_to_ramekin | 94.4% | 96.3% | +1.88pp | |
| from_table_center | 95.6% | 98.8% | +3.12pp | |
| on_cookie_box | 95.6% | 98.8% | +3.12pp | |
| in_top_drawer | 71.9% | 69.4% | **-2.50pp** | 唯一负 Δ |
| **on_ramekin** | **0.0%** | **0.0%** | **0.00pp** | **always-0%** |
| next_to_cookie_box | 96.9% | 97.5% | +0.62pp | |
| on_stove | 81.3% | 82.5% | +1.25pp | |
| next_to_plate | 78.8% | 81.3% | +2.50pp | |
| on_wooden_cabinet | 83.8% | 85.0% | +1.25pp | |
| **10-task overall** | **79.06%** | **80.56%** | **+1.50pp** | |

### Paired t-test (n=8 seeds)

| 范围 | VLA-only | Adaptive | Δ | t | df | p |
|------|----------|----------|-----|----|------|-------|
| 全部 10 task | 79.06% | 80.56% | +1.50pp | 3.240 | 7 | **0.0142** |
| 剔除 always-0% (9 task) | 87.85% | 89.51% | +1.67pp | 3.240 | 7 | **0.0142** |

注：剔除 on_ramekin 不改 p-value——恒零 task 在 paired diff 上贡献为 0，仅把 SR base 从 200 缩到 180，Δ 在 pp 单位上等比放大 ~1.11 倍。

### Mechanism

- **9/10 task Adaptive ≥ VLA-only**（含一个 ties）；唯一例外 in_top_drawer（−2.50pp）是 VLA-only 最弱的非零 task，推测深抽屉视觉挑战大、CRM 在此放大了不可靠 refinement。
- **on_ramekin always-0%** 是任务本身（黑碗放在 ramekin 顶部不可达），与方法无关。
- **trigger_rate 跨 8 seed 极稳定**：19.45%–20.46%（mean 19.84%，σ=0.31pp），conformal threshold 在 calibration 后稳定。
- Per-task trigger_rate 在 JSON 中**未输出**——无法直接做 task-level trigger↔Δ correlation；per-seed corr(trigger_rate, Δ)=-0.30（n=8）不显著且 trigger 几乎不变，不作证据。
- Adaptive gain **不集中在最难 task**（top_drawer 反降），而是均匀分布在 mid→high SR task，最大 gain 在 between_plate_and_ramekin (+3.75pp) 和 from_table_center / on_cookie_box (+3.12pp)。
- 8/8 seed 中 **7/8 Δ ≥ 0**（s46 = −0.5pp 是唯一例外），符号方向稳定。

数据源已记录到 `artifacts/spatial_per_task_breakdown.md`。

---
