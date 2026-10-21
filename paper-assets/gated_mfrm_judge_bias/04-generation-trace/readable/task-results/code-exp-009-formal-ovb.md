# code exp 009 formal ovb

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_009_formal_ovb_20260521T223155_result.json`
- **Structured JSON:** [`2efdf26f60bdb46a2426.json`](../../sessions/2e/2efdf26f60bdb46a2426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。汇报结果：

---

**代码路径**: `/root/gated_mfrm_judge_bias/exp009/`

| 文件 | 行数 | 说明 |
|------|------|------|
| `run_exp009.py` | 420 | 主脚本 |

**输出文件**（dry-run 生成）:
- `bias_vs_rho.csv` — 8 rows (2 seeds × 2 rhos × 2 methods)
- `bias_vs_rho.png` — 双面板折线图（signed bias + RMSE vs ρ）
- `cn_recovery.csv` — 100 rows (2 seeds × 50 models)
- `cn_recovery_scatter.png` — c_true vs c_hat scatter

**Dry-run 结果** (2 seeds × 2 rhos):
- Part A 耗时 808s，Part B 耗时 293s，总计 ~18 min
- 每个 (rho, seed) pair 平均 ~200s（含 2 次 MCMC fit）
- Part B 每 seed ~150s（1 次 MCMC fit）
- mean_bias ≈ 0（centering 约束导致，符合理论预期）
- RMSE: sequential 0.22-0.26 vs joint 0.12-0.15
- c_n recovery: RMSE=0.54, coverage=0.80, corr=0.81

**预估全量运行时间**:
- Part A: 400 pairs × 200s ≈ **22 小时**
- Part B: 50 seeds × 150s ≈ **2 小时**
- 总计: **~24 小时**（CPU-only，无 CUDA jaxlib）

**注意**: 服务器有 RTX PRO 6000 Blackwell GPU 但 JAX 未安装 CUDA 版本，全程在 CPU 上运行。安装 `jax[cuda]` 可显著加速。

**全量运行命令**:
```bash
cd /root/gated_mfrm_judge_bias/exp009 && rm -f bias_vs_rho.csv cn_recovery.csv && \
nohup /root/miniconda3/bin/python3 run_exp009.py --part both > /tmp/exp009_full.log 2>&1 &
```

支持中断恢复（逐 seed 保存 checkpoint）。

---
