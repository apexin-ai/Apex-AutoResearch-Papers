# Experiment Status Report — 2026-05-23

## bjb1-32546 (6 GPUs active)

### 1. train-crm-4suite-resume (cuda:3) — CRM 4-suite Training r5
- **Status**: RUNNING — epoch 38/50, batch 3850/6316 (61%)
- **Val loss**: 0.005903 (best, epoch 37) — steadily improving from 0.006075 at resume
- **Checkpoints**: epoch 33–37 saved (~25 min/epoch)
- **ETA**: ~5 hours (12 epochs remaining × 25 min)

### 2. crm_norm02 (cuda:0) — CRM norm=0.2 always-on, spatial
- **Status**: RUNNING — task 2/10, rollout 5/20
- **Completed**: task 1 = 100.0% (20/20)
- **ETA**: ~4 hours

### 3. adapt_tau015 (cuda:1) — Adaptive tau=0.15, spatial
- **Status**: RUNNING — task 2/10, rollout 5/20
- **Completed**: task 1 = 100.0% (20/20)
- **ETA**: ~4 hours

### 4. adapt_tau025 (cuda:2) — Adaptive tau=0.25, spatial
- **Status**: RUNNING — task 2/10, rollout 5/20
- **Completed**: task 1 = 95.0% (19/20)
- **ETA**: ~4 hours

### 5. adapt_tau035 (cuda:4) — Adaptive tau=0.35, spatial
- **Status**: RUNNING — task 2/10, rollout 5/20
- **Completed**: task 1 = 95.0% (19/20)
- **ETA**: ~4 hours

### 6. obj_crm005 (cuda:5) — CRM norm=0.05, object
- **Status**: RUNNING — task 1/10, rollout 10/20
- **ETA**: ~5 hours

---

## bjb2-28827 (6 GPUs active)

### 1. obj_vla_s42 (cuda:3) — Object VLA-only seed42
- **Status**: RUNNING — task 7/10, rollout 5/20
- **Completed** (6 tasks):
  | Task | Success |
  |------|---------|
  | alphabet_soup | 85.0% (17/20) |
  | cream_cheese | 75.0% (15/20) |
  | salad_dressing | 85.0% (17/20) |
  | bbq_sauce | 85.0% (17/20) |
  | ketchup | 90.0% (18/20) |
  | tomato_sauce | 75.0% (15/20) |
- **Running avg**: 82.5%
- **ETA**: ~2.5 hours

### 2. obj_vla_s43 (cuda:4) — Object VLA-only seed43
- **Status**: RUNNING — task 7/10 (between tasks)
- **Completed** (6 tasks):
  | Task | Success |
  |------|---------|
  | alphabet_soup | 70.0% (14/20) |
  | cream_cheese | 70.0% (14/20) |
  | salad_dressing | 75.0% (15/20) |
  | bbq_sauce | 85.0% (17/20) |
  | ketchup | 80.0% (16/20) |
  | tomato_sauce | 85.0% (17/20) |
- **Running avg**: 77.5%
- **ETA**: ~2.5 hours

### 3. obj_vla_s44 (cuda:5) — Object VLA-only seed44
- **Status**: RUNNING — task 7/10 (between tasks)
- **Completed** (6 tasks):
  | Task | Success |
  |------|---------|
  | alphabet_soup | 70.0% (14/20) |
  | cream_cheese | 70.0% (14/20) |
  | salad_dressing | 75.0% (15/20) |
  | bbq_sauce | 90.0% (18/20) |
  | ketchup | 90.0% (18/20) |
  | tomato_sauce | 80.0% (16/20) |
- **Running avg**: 79.2%
- **ETA**: ~2.5 hours

### 4. obj_adapt (cuda:0) — Object Adaptive tau=0.074855 seed42
- **Status**: RUNNING — task 1/10, rollout 10/20
- **ETA**: ~5 hours

### 5. obj_reconvla (cuda:1) — Object Reconvla K=10 seed42
- **Status**: RUNNING — task 1/10, rollout 10/20
- **ETA**: ~5 hours

### 6. goal_crm005 (cuda:2) — Goal CRM norm=0.05 seed42
- **Status**: RUNNING — task 1/10, rollout 10/20
- **ETA**: ~5 hours

---

## Key Observations

### Object VLA-only Baseline (Priority)
- 3-seed run progressing well: all 3 at task 7/10, ~65% complete
- Preliminary cross-seed average: **79.7%** (s42=82.5%, s43=77.5%, s44=79.2%)
- Expected completion: ~14:30 today
- No crashes or anomalies

### CRM 4-suite Training r5
- Healthy convergence — val_loss dropping: 0.006075 → 0.005903 over 5 epochs
- On epoch 38/50, expected completion: ~16:30 today
- Loss still improving, no signs of overfitting

### Spatial Eval Sweep (bjb1)
- All 4 spatial experiments (crm_norm02, adapt_tau015/025/035) running in sync
- All on task 2/10, just started ~35 min ago
- Task 1 results: norm=0.2 and tau=0.15 at 100%; tau=0.25 and tau=0.35 at 95%

### Alerts
- **None** — all 12 experiments running normally, no crashes, no abnormal GPU usage
