# ssh exp003 dryrun autodl

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_dryrun_autodl_20260522T120246_result.json`
- **Structured JSON:** [`8acbc4c0b28a40d00cd1.json`](../../sessions/8a/8acbc4c0b28a40d00cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

| 项目 | 状态 |
|------|------|
| JAX | 0.10.1, CUDA, 4× CudaDevice ✓ |
| NumPyro | 0.21.0 ✓ |
| ArviZ | 1.1.0（刚装）✓ |
| Blackwell 兼容性 | 无问题 ✓ |

**代码位置**: `/root/gated_mfrm_judge_bias/mvp/` — `run_mvp_003.py` + `models_v3.py` + 依赖文件齐全

**Pipeline 验证**（50wu + 50s，minimal params）:

| 方法 | 耗时 | RMSE | Kendall τ |
|------|------|------|-----------|
| raw_average | 0.0s | 0.7595 | 0.8129 |
| mfrm_only_v3 | 10.4s | 0.3014 | 0.8122 |
| joint_gmfrm_v3 | 6.8s | 0.1215 | 0.9184 |

**4-chain 并行**（`set_host_device_count(4)`）: Rhat=1.42, ESS=9 — 数值符合极少样本预期，4 GPU 并行正常。

**代码就绪，可以启动 exp-003 正式拟合。** 完整 run_mvp_003.py（20 seeds × 4 methods × 2000wu+4000s×4chains）预计需要较长时间。

---
