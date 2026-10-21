# ssh waic loo check and collect

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_waic_loo_check_and_collect_20260523T004658_result.json`
- **Structured JSON:** [`79eb2778708452128a65.json`](../../sessions/79/79eb2778708452128a65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## WAIC/LOO-CV 任务状态

### G-MFRM 结果（已完成）

```
G-MFRM:
  WAIC:  4544.52 (SE: 38.50)
  p_WAIC: 128.27
  LOOIC: 4545.19 (SE: 38.50)
  p_LOO:  128.61
  Pareto-k > 0.7: 0/5661 (0.0%) — 全部 good
  Pareto-k max: 0.276, mean: 0.027
```

Pareto-k 诊断非常好，所有 5661 个观测点的 k 值都在 0.7 以下，LOO 估计可靠。

### MFRM-only 对比模型（仍在运行）

有两个 MFRM-only fitting 进程同时在跑：

| PID | 脚本 | 启动时间 | 进度 | ETA |
|-----|------|---------|------|-----|
| 249604 | `scripts/waic_loo_comparison.py` | 08:07 | warmup 10% (783/8000) | ~2h22m（约 11:10 完成）|
| 244822 | `compute_waic_loo.py` | 07:52 | 未知（无可见日志）| 未知 |

`waic_loo_comparison.py` 配置为 warmup=2000, samples=2000, chains=2（可能是 4 chains based on 8000 total），每步 ~1.18s，当前仍在 warmup 阶段。

### 其他任务状态

- **exp005**: 已完成
- **exp006_full**: sampling 68%（2035/3000），~3 min 剩余（这是单 chain 进度）
- **refit003b**: 已失败（`TypeError: Invalid comparison between dtype=str and float`）

### 结论

G-MFRM 的 WAIC/LOO 已产出，MFRM-only baseline fitting 预计还需 ~2.5 小时。ΔWAIC 对比需等 MFRM-only 完成后才能计算。两个 MFRM-only 进程可能是重复任务，建议确认是否需要 kill 其中一个以释放 GPU 资源。

---
