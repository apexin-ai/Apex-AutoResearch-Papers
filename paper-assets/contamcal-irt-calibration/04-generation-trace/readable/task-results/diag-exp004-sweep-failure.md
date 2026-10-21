# diag exp004 sweep failure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp004_sweep_failure_20260514T031255_result.json`
- **Structured JSON:** [`9cbd00df8210d532b5ec.json`](../../sessions/9c/9cbd00df8210d532b5ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### 失败原因：代码从未部署到服务器

服务器 `/root/contamcal-irt-calibration/` 上**没有 `artifacts/` 目录**，没有 `.git`，没有 `run_sweep.py`，没有任何 exp_004 日志。启动命令 `cd artifacts/simulation_sweep && ...` 在服务器上会直接 `No such file or directory` 失败。

服务器现有内容仅：`exp001/`, `exp002/`, `exp006/`, `outputs/`, `stan_models/`, `env_setup.sh`。

### 部分结果存在于本地

`artifacts/simulation_sweep/results/` 有本地执行的部分结果（可能之前在本机跑过）：

| Condition | Seeds完成 | 状态 |
|-----------|----------|------|
| auc0.55_n20_prior1.0_binary | 10/10 | 完成 |
| auc0.55_n50_prior1.0_binary | 10/10 | 完成 |
| auc0.55_n100_prior1.0_binary | 6/10 | 中断 |
| auc0.8_n50_prior1.0_binary | 1/10 | 中断 |
| 其余 8 个 condition | 0/10 | 未开始 |

总进度：27/120 runs (22.5%)，subset 模式 12 conditions × 10 seeds。

### 重跑建议

1. **部署代码到服务器**：`artifacts/simulation_sweep/` 整个目录（含 .stan 文件和已有 results）需同步到服务器
2. **创建 venv 并安装依赖**：服务器上需要 `cmdstanpy`、`numpy`、`scipy`，以及 CmdStan 编译器
3. **脚本支持断点续跑**：`load_checkpoint()` 会跳过已完成的 seed，同步已有 results 后直接 `python run_sweep.py subset` 即可从 seed 6 of auc0.55_n100 继续
4. **CPU only 任务**：不占 GPU，但每个 NUTS fit ~660s，剩余 93 runs 预计 ~17 小时

---
