# code d012 calibrate restart

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d012_calibrate_restart_20260517T131032_result.json`
- **Structured JSON:** [`9cf24c3c8372e984790d.json`](../../sessions/9c/9cf24c3c8372e984790d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Here's the complete report:

---

## Step 1: PID 88161
Killed (force_killed=false, graceful termination). GPU 1 confirmed free (0MiB).

## Step 2: report_actual 修复

**Before** (lines 174-181):
```python
# 实际比例（整数截断后）
actual_ratio = num_real / total_per_gen if total_per_gen > 0 else 0.0

# Bug #1 fix: 回传实际值给 controller 修正预算
if controller is not None and gen >= 2:
    controller.report_actual(actual_ratio)
elif controller is not None and gen == 1:
    controller.report_actual(actual_ratio)

# ... [generation happens] ...

if num_real > 0:
    num_real = min(num_real, len(real_train_data))  # CAP happens AFTER report
```

**After** (report moved to line 201, after cap):
```python
# actual_ratio computed after pool cap (see below)

# ... [generation happens] ...

if num_real > 0:
    num_real = min(num_real, len(real_train_data))
    indices = torch.randperm(len(real_train_data))[:num_real].tolist()
    real_subset = [real_train_data[i] for i in indices]
else:
    real_subset = []

# Actual ratio after pool cap
actual_ratio = len(real_subset) / (len(real_subset) + len(synthetic_data)) if (len(real_subset) + len(synthetic_data)) > 0 else 0.0
if controller is not None:
    controller.report_actual(actual_ratio)
```

## Step 3: k/tau 参数更新

| File | Field | Before | After |
|------|-------|--------|-------|
| `src/config.py:46` | controller_k | 1.0 | **20.0** |
| `src/config.py:47` | controller_tau | 0.005 | **0.002** |
| `src/controller.py` | `__init__` default k | 1.0 | **20.0** |
| `src/controller.py` | `__init__` default tau | 0.005 | **0.002** |
| `run_phase1.py:85` | --k default | 1.0 | **20.0** |
| `run_phase1.py:83` | --tau default | 0.005 | **0.002** |

## Step 4: sensitivity grid

| | Before | After |
|---|--------|-------|
| K_VALUES | [0.5, 1.0, 2.0] | **[5, 10, 20, 50]** |
| TAU_VALUES | [0.002, 0.005, 0.01] | **[0.001, 0.002, 0.005]** |
| Grid size | 9 combos | **12 combos** |

## Step 5: Dry-run 表格

```
Gen  S_tilde      delta      triggered  r_req    r_actual   B_rem    real     synth
------------------------------------------------------------------------------------------
0    2366.684     N/A        N/A        0.5000   0.5000     4.5000   25000    25000
1    2415.723     -0.020721  False      0.5000   0.5000     4.0000   25000    25000
2    2442.825     -0.011452  False      0.5000   0.5000     3.5000   25000    25000
3    2441.696     0.000477   False      0.5000   0.5000     3.0000   25000    25000
4    2423.373     0.007742   True       0.6148   0.6148     2.3852   30742    19258
5    2396.773     0.011239   True       0.6618   0.6618     1.7234   33090    16910
6    2365.969     0.013016   True       0.6512   0.6511     1.0722   32557    17443
7    2335.079     0.013052   True       0.5784   0.5784     0.4938   28922    21078
8    2293.599     0.017527   True       0.2938   0.2938     0.2000   14688    35312
```

**确认**:
1. ✅ Ratio 有意义变化: 0.50 → 0.66 (peak Gen 5), 范围 [0.29, 0.66]
2. ✅ 信号从 Gen 4 开始触发 (delta=0.0077 > tau=0.002), 5/8 gens triggered
3. ✅ 预算正确消耗: 5.0 → 0.2000 (恰好为最后一代预留 r_min)

## Step 6: exp_003 重启

- **PID**: 116947 (child of nohup 116942)
- **GPU**: cuda:1 确认 (19034MiB, 422W, 36% util)
- **参数**: `--condition adaptive --seed 42 --generations 10 --signal log_det --tau 0.002 --k 20`
- **日志**: `logs/exp_003_v3_adaptive_k20_s42.log` — 正在 Gen 0 evaluation + Gen 1 synthetic generation

## Step 7: exp_001

- **PID 59365**: 活跃, GPU 0 (65900MiB, 94% util, 300W)
- **命令**: `python run_phase0.py --resume_from_gen 4`
- **进度**: Gen 8/9 已完成 (results + hellaswag gen0-8), 当前跑 Gen 9
- **1b run**: 失败 (`No space left on device` on /overlay, 25GB/30GB used)

**Phase 0 metrics (gen 0-8)**:
```
Gen  eff_rank   log_det     ppl
0    417.55     2366.684    9.55
1    491.77     2464.762    11.38
2    496.44     2469.928    13.58
3    493.31     2440.566    16.25
4    485.67     2405.050    19.80
5    479.21     2370.173    24.59
6    473.00     2335.165    30.91
7    464.20     2304.190    38.89
8    456.76     2252.119    49.29
```

---
