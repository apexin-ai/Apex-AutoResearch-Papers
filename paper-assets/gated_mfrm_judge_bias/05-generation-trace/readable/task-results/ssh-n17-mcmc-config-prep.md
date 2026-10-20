# ssh n17 mcmc config prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_mcmc_config_prep_20260523T151354_result.json`
- **Structured JSON:** [`d2d413d01d5f6fc6b24e.json`](../../sessions/d2/d2d413d01d5f6fc6b24e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建完成。

## 产出总结

### 1. `run_exp003_n17.py`
位置：`/root/gated_mfrm_judge_bias/exp003/run_exp003_n17.py`

关键修改：
- `--warmup` 默认值 2000 → **6000**
- 其余 MCMC 参数不变（samples=4000, chains=4, target_accept=0.95）
- 在 `joint_gmfrm` idata 保存后自动执行 **convergence stop-loss**：R-hat > 1.1 或 ESS < 50 触发失败，写 `CONVERGENCE_FAILED` 标记文件，`sys.exit(1)`

运行命令：
```bash
cd /root/gated_mfrm_judge_bias/exp003
python run_exp003_n17.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp001_n17/results \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17
```

### 2. 数据路径
- **data_loader.py 是数据驱动的**：动态构建 model/item/judge 索引，N=17 自动适配
- N=17 judge 评测数据在 rtx6000-4x 产出后需 **scp 到 autodl-8gpu**，放到 `/root/gated_mfrm_judge_bias/exp001_n17/results/` 目录
- exposure_scores.csv（exp002）可复用，exposure 按 item_id 对齐，与 judge 数量无关

### 3. `run_n17_downstream.py`
位置：`/root/gated_mfrm_judge_bias/exp003/run_n17_downstream.py`

6 个分析步骤：

| # | 分析 | 接口类型 | 处理方式 |
|---|------|----------|----------|
| 1 | WAIC/LOO (compute_waic_loo.py) | 硬编码路径 | monkey-patch 模块常量 |
| 2 | Bootstrap Δτ (bootstrap_delta_tau.py) | 硬编码路径+MODEL_NAMES | subprocess wrapper 覆盖路径 |
| 3 | Baselines (exp004/run_exp004.py) | argparse | 直接传 CLI args ✅ |
| 4 | Δθ table (exp019/run_exp019.py) | 硬编码 EXP003B_DIR | subprocess wrapper 覆盖 |
| 5 | Facet fit (exp008/run_exp008.py) | 硬编码路径 | subprocess wrapper 重写 main() |
| 6 | Full posterior (analyze_003b.py) | argparse `--output-dir` | 直接传 CLI args ✅ |

### 4. 各脚本接口检查结果
- **可直接用**：exp004（argparse）、analyze_003b.py（argparse）
- **需 monkey-patch**：compute_waic_loo.py、bootstrap_delta_tau.py、exp019、exp008 — 全部硬编码 `output_003b` 路径，master 脚本通过 wrapper 子进程覆盖
- **bootstrap_delta_tau.py 额外注意**：硬编码了 `MODEL_NAMES`（8 个模型）和 `ARENA_ELO` 字典，如果 N=17 的模型集有变化需同步更新

---
