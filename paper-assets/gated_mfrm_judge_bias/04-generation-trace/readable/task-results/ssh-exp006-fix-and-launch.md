# ssh exp006 fix and launch

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp006_fix_and_launch_20260522T201520_result.json`
- **Structured JSON:** [`d60217e1b0f2e29b0bd1.json`](../../sessions/d6/d60217e1b0f2e29b0bd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种 MCMC 方法的 InferenceData 都成功保存。汇报如下：

---

### 1. 代码修改内容

| 修改 | 说明 |
|------|------|
| **修复 import bug** | `from exp003_models import` → `from models import`（两处：`fit_methods_on_subset` L182, `main()` L518） |
| **添加 `import arviz as az`** | L33 |
| **`fit_methods_on_subset`** 新增 `idata_dir`, `idata_label` 参数 | 每个 MCMC fit 后调 `az.from_numpyro(mcmc).to_netcdf(...)` |
| **`run_sensitivity_analysis`** 新增 `output_dir` 参数 | 创建 `{output_dir}/idata/` 子目录，传 `idata_label=f"k{k}_s{s_idx}"` |
| **安装 `h5netcdf`** | NetCDF4 后端依赖 |

### 2. InferenceData 保存路径模式

```
results_full/idata/idata_{method}_k{judge_count}_s{subset_idx}.nc
```
例：`idata_joint_gmfrm_k2_s1.nc`（~5.7MB），`idata_sequential_k2_s1.nc`（~5.4MB）

### 3. 启动命令

```bash
CUDA_VISIBLE_DEVICES=1 JAX_PLATFORMS=cuda,cpu XLA_PYTHON_CLIENT_PREALLOCATE=false XLA_PYTHON_CLIENT_MEM_FRACTION=0.25 \
python run_exp006.py --methods raw_average joint_gmfrm sequential \
  --judge-counts 2 4 6 9 --run-loocv --output-dir results_full
```
tmux session: `exp006_full`

### 4. 初始日志确认

- MCMC warmup/sample 正常运行，acc. prob=0.93-0.96
- Subset 1 的 idata 保存失败（h5netcdf 尚未安装），subset 2 开始后全部正常保存
- 当前进度：k=2 的 subset 2 已完成

### 5. 预估完成时间

- 每 subset: sequential (~30s) + joint_gmfrm (~50s) ≈ **~1.3 min**
- 31 subsets × 1.3 min ≈ 40 min
- LOOCV (10 fits) ≈ 13 min
- **总计 ≈ 1 小时**

> **注意**：subset 1（k=2, s=0）的 2 个 idata 文件丢失。如需补跑可后续单独处理。

---
