# fix exp006 kill and patch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp006_kill_and_patch_20260514T145235_result.json`
- **Structured JSON:** [`323357e1c0931415be2d.json`](../../sessions/32/323357e1c0931415be2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 1. Kill 确认
4 个 Stan 进程 (386298-386301) 已全部 kill，状态 ALL_DEAD。

### 2. 代码修改摘要

**4 个文件，共 20 处修改：**

| 文件 | 修改内容 |
|------|---------|
| `run_irt_calibration.py` (6处) | 正则 `(_aligned)?$`、`parse_model_dir_name` 加 `is_aligned`、`load_eval_results` 加 3 个过滤参数、argparse 加 `--model-scale/--data-seed/--aligned-only`、main 调用传参 |
| `run_irt_stan.py` (6处) | 同上（独立副本），`run_real_data` 内 `load_eval_results` 调用用 `getattr(args, ...)` 透传 |
| `run_exp006.py` (3处) | argparse 加 3 个参数、`load_eval_results` 调用传参、`run_joint_fit` 调用传参 |
| `joint_fit.py` (4处) | `run_joint_fit` 签名加参数、`load_eval_results` 调用传参、argparse 加参数、main 调用传参 |

注意：用 `--data-seed` 而非 `--seed`，因为 `--seed` 已被 Stan MCMC 采样占用。

### 3. Dry-run 验证结果

`--model-scale 0.5B --data-seed 42 --aligned-only` 过滤后（加上默认 `skip_para=True`），最终 INCLUDE：

```
Qwen2.5-0.5B_d000_s42_aligned   ✓
Qwen2.5-0.5B_d005_s42_aligned   ✓
Qwen2.5-0.5B_d025_s42_aligned   ✓
Qwen2.5-0.5B_d100_s42_aligned   ✓
```

排除的 20 个目录：其他 scale (1.5B/3B)、非 42 seed (s123)、legacy 非 aligned、_raw、_para 全部正确过滤。

### 4. 受影响文件
- `exp006/run_irt_calibration.py`
- `exp006/run_irt_stan.py`
- `exp006/run_exp006.py`
- `exp006/joint_fit.py`

---
