# Running Experiments Progress — 2026-05-21 11:50 UTC

## Summary

| # | Experiment | Server | PID | Status | Tasks Done | Rollouts | ETA |
|---|-----------|--------|-----|--------|------------|----------|-----|
| 1 | eval-adaptive-k-spatial-p90-seed44 | bjb2-28827 | 975409 | ✅ ALIVE | 2/10 | 10/task | ~1h16m |
| 2 | eval-pi05-baseline-object-seed42 | bjb2-40593 | 802639* | ✅ ALIVE | 2/10 | 20/task | ~6h24m |
| 3 | norm003-seed66 | bjb1-18228 | 642428 | ✅ ALIVE | 5/10 | 20/task | ~1h51m |
| 4 | norm005-seed66 | bjb1-18228 | 642506 | ✅ ALIVE | 5.25/10 | 20/task | ~1h40m |
| 5 | norm01-seed66 | bjb1-18228 | 642775 | ✅ ALIVE | 5.25/10 | 20/task | ~1h40m |
| 6 | norm003-seed67 | bjb2-28827 | 969788 | ✅ ALIVE | 3/10 | 10/task | ~1h26m |
| 7 | norm005-seed67 | bjb1-32546 | 805840 | ✅ ALIVE | 3.5/10 | 10/task | ~1h26m |
| 8 | norm01-seed67 | bjb1-18228 | 666593 | ✅ ALIVE | 3/10 | 10/task | ~1h26m |

*PID 802634 is bash wrapper; actual python child PID = 802639

## Per-Experiment Details

### 1. eval-adaptive-k-spatial-p90-seed44 (bjb2-28827, cuda:0)
- Uptime: 19 min, CPU 508%
- Completed tasks:
  - pick_up_black_bowl_between...: **80%** (8/10)
  - pick_up_black_bowl_next_to...: **100%** (10/10)
- Currently on task 3

### 2. eval-pi05-baseline-object-seed42 (bjb2-40593, cuda:0)
- Uptime: 1h36m, CPU 334%
- ⚠️ **0% success rate on both completed tasks** (0/40 rollouts)
  - alphabet_soup: 0% (0/20)
  - cream_cheese: 0% (0/20)
- Model loaded with 437 key remapping ("Fixed 437 vision tower keys")
- GPU: 47% util, 13039/24564 MiB — model is loaded and running
- ~48 min/task → ~6h24m remaining

### 3. norm003-seed66 (bjb1-18228, cuda:0, norm=0.03, 20 rollouts)
- Uptime: 1h51m, CPU 376%
- Tasks done: 5/10
  - alphabet_soup: 0%, cream_cheese: 10%, salad_dressing: 15%, bbq_sauce: 15%, ketchup: 10%
- Running avg: **10.0%**

### 4. norm005-seed66 (bjb1-18228, cuda:2, norm=0.05, 20 rollouts)
- Uptime: 1h51m, CPU 387%
- Tasks done: 5/10, currently on task 6 (tomato_sauce 5/20)
  - alphabet_soup: 0%, cream_cheese: 5%, salad_dressing: 10%, bbq_sauce: 20%, ketchup: 5%
- Running avg: **8.0%**

### 5. norm01-seed66 (bjb1-18228, cuda:3, norm=0.1, 20 rollouts)
- Uptime: 1h51m, CPU 383%
- Tasks done: 5/10, currently on task 6 (tomato_sauce 5/20)
  - alphabet_soup: 0%, cream_cheese: 5%, salad_dressing: 25%, bbq_sauce: 25%, ketchup: 5%
- Running avg: **12.0%**

### 6. norm003-seed67 (bjb2-28827, cuda:5, norm=0.03, 10 rollouts)
- Uptime: 37 min, CPU 594%
- Tasks done: 3/10
  - alphabet_soup: 0%, cream_cheese: 10%, salad_dressing: 10%
- Running avg: **6.7%**

### 7. norm005-seed67 (bjb1-32546, cuda:2, norm=0.05, 10 rollouts)
- Uptime: 37 min, CPU 390%
- Tasks done: 3/10, currently on task 4 (bbq_sauce 5/10)
  - alphabet_soup: 0%, cream_cheese: 0%, salad_dressing: 10%
- Running avg: **3.3%**

### 8. norm01-seed67 (bjb1-18228, cuda:1, norm=0.1, 10 rollouts)
- Uptime: 37 min, CPU 369%
- Tasks done: 3/10
  - alphabet_soup: 0%, cream_cheese: 0%, salad_dressing: 20%
- Running avg: **6.7%**

## GPU Utilization

| Server | GPU | Util | VRAM Used/Total | Used By |
|--------|-----|------|-----------------|---------|
| bjb2-28827 | 0 | 18% | 5202/24564 MiB | eval-adaptive-k-seed44 |
| bjb2-28827 | 1-4 | 25-31% | 5730/24564 MiB | (other jobs) |
| bjb2-28827 | 5 | 31% | 4801/24564 MiB | norm003-seed67 |
| bjb2-40593 | 0 | 47% | 13039/24564 MiB | pi05-baseline |
| bjb1-18228 | 0 | 36% | 3408/24564 MiB | norm003-seed66 |
| bjb1-18228 | 1 | 27% | 4334/24564 MiB | norm01-seed67 |
| bjb1-18228 | 2 | 37% | 3408/24564 MiB | norm005-seed66 |
| bjb1-18228 | 3 | 29% | 3408/24564 MiB | norm01-seed66 |
| bjb1-32546 | 0 | 0% | 2/24564 MiB | idle |
| bjb1-32546 | 2 | 26% | 4335/24564 MiB | norm005-seed67 |
| bjb1-32546 | 1,3-5 | 29-35% | 5731/24564 MiB | (other jobs) |

## Anomalies

1. **⚠️ pi05-baseline 0% success (0/40 rollouts)** — 两个 task 全部失败。模型加载时有 437 key remapping，日志显示已修复。norm sweep 在相同 task 上成功率也很低 (0-10%)，object benchmark 本身难度高。建议等更多 task 完成后再判断。

2. **pi05 速度极慢** — 每个 task 约 48 min（20 rollouts），预计总计约 8h。SmolVLA norm sweep 每 task 约 22 min (20 rollouts) 或 12 min (10 rollouts)。pi05 模型 13GB VRAM vs SmolVLA 3-5GB，推理慢是预期的。

3. **所有 8 个实验正常运行，无 OOM、无进程死亡、无停滞。**
