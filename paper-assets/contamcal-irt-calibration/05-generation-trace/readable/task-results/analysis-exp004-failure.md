# analysis exp004 failure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004-failure_20260514T031520_result.json`
- **Structured JSON:** [`e8d1f4cd8976168737b9.json`](../../sessions/e8/e8d1f4cd8976168737b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因
**进程并未失败。** PID 219346 仍在运行（已 10h+，状态 Sl），registry 标记 `DONE/failed` 是误报——可能是监控超时触发。进程正常推进中，当前在第 3 个条件 `auc0.55_n100` 的 seed 6/10。

### 进度：27/120 runs (22.5%)

| Condition | 完成 | 状态 |
|-----------|------|------|
| auc0.55_n20 | 10/10 | ✓ 完成 |
| auc0.55_n50 | 10/10 | ✓ 完成 |
| auc0.55_n100 | 6/10 | 进行中 |
| 其余 9 conditions | 0-1/10 | 待运行 |

预计剩余 ~25h，总计 ~35h 完成。

### 初步结果分析（AUC=0.55 条件，γ_true=0.5）

| N_models | γ_bias | γ_RMSE | CI95 coverage | CI95 width | θ_corr |
|----------|--------|--------|---------------|------------|--------|
| 20 | +0.020 | 0.040 | 80% | 0.133 | 0.958 |
| 50 | +0.015 | 0.026 | 90% | 0.087 | 0.947 |
| 100 | -0.003 | 0.004 | 100% | 0.065 | 0.950 |

**趋势**：
- γ recovery 随 N_models 增大显著改善（RMSE 从 0.04 降到 0.004）
- 即使在最弱信号（AUC=0.55）下，N≥50 即可稳定识别 γ（100% CI95 excludes zero）
- CI95 coverage 在 N=20 时偏低（80%），说明小样本下后验过度自信
- 有趣：AUC=0.8/N=50 的 CI95 width (0.16) 比 AUC=0.55/N=50 (0.087) 更宽——需要更多 seeds 确认

### 修复方案

无需修复，进程正常运行。建议：

1. **更新 registry 状态**为 RUNNING（误报 failed）
2. **不要重跑**——进程有 checkpoint/resume 机制（`load_checkpoint` 在 L225-232），即使中断重跑也会跳过已完成 seeds
3. 如果需要加速，可以起多个进程分别跑不同 AUC 条件（但需修改代码添加 condition filter 参数）

如果进程真的中断了，重跑命令：
```bash
cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep && \
source ../mvp_simulation/.venv/bin/activate && \
nohup python run_sweep.py subset > sweep.log 2>&1 &
```

脚本会自动跳过已完成的 seeds，从断点继续。

---
